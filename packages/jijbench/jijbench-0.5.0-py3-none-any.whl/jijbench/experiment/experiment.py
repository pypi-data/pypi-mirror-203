from __future__ import annotations

import abc
import pathlib
import typing as tp
import uuid
import warnings
from dataclasses import dataclass, field

import pandas as pd

from jijbench.consts.default import DEFAULT_RESULT_DIR
from jijbench.containers.containers import Artifact, Container, Record, Table
from jijbench.elements.base import Callable
from jijbench.elements.id import ID
from jijbench.functions.concat import Concat
from jijbench.functions.factory import ArtifactFactory, TableFactory
from jijbench.io.io import save
from jijbench.solver.base import Parameter, Response
from jijbench.typing import ArtifactDataType, ExperimentDataType


@dataclass
class Experiment(Container[ExperimentDataType]):
    """Stores data related to an benchmark.

    The Experiment class stores the results obtained from a benchmark as Artifact and Table objects and assists in managing the benchmark process.
    With this class, you can add and save experimental results, as well as view them in various formats.

    Attributes:
        data (tuple[Artifact, Table]): A tuple containing an Artifact object and a Table object.
        name (str): The name of the experiment.
        autosave (bool): Whether to automatically save the experiment upon exit.
        savedir (str | pathlib.Path): The directory where the experiment will be saved.
    """

    data: tuple[Artifact, Table] = field(default_factory=lambda: (Artifact(), Table()))
    name: str = field(default_factory=lambda: str(uuid.uuid4()))
    autosave: bool = field(default=True, repr=False)
    savedir: str | pathlib.Path = field(default=DEFAULT_RESULT_DIR, repr=False)

    def __post_init__(self):
        super().__post_init__()

        if self.data[0].name is None:
            self.data[0].name = self.name

        if self.data[1].name is None:
            self.data[1].name = self.name

        self.savedir = pathlib.Path(self.savedir)
        setattr(self, "state", _Created())

    def __len__(self) -> int:
        """
        Perform the operation __len__.
        """
        a_len = len(self.data[0])
        t_len = len(self.data[1])
        if a_len != t_len:
            warnings.warn(
                f"The length of artifact object and table object are different: {a_len} != {t_len}, return the larger one."
            )
        return max(a_len, t_len)

    def __enter__(self) -> Experiment:
        """Set up Experiment.
        Automatically makes a directory for saving the experiment, if it doesn't exist.
        """

        setattr(self, "state", _Running(self.name))
        pathlib.Path(self.savedir).mkdir(parents=True, exist_ok=True)
        return self

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        """Saves the experiment if autosave is True."""
        state = getattr(self, "state")

        if self.autosave:
            state.save(self)

        setattr(self, "state", _Waiting(self.name))

    @property
    def artifact(self) -> ArtifactDataType:
        """Return the artifact of the experiment as a dictionary."""
        return self.data[0].view()

    @property
    def table(self) -> pd.DataFrame:
        """Return the table of the experiment as a pandas dataframe."""
        return self.data[1].view()

    @property
    def params_table(self) -> pd.DataFrame:
        """Return the parameters table of the experiment as a pandas dataframe."""
        bools = self.data[1].data.applymap(lambda x: isinstance(x, Parameter))
        return self.table[bools].dropna(axis=1)

    @property
    def response_table(self) -> pd.DataFrame:
        """Return the returns table of the experiment as a pandas dataframe."""
        bools = self.data[1].data.apply(lambda x: not isinstance(x[0], Response))
        droped_columns = self.data[1].data.columns[bools]
        return self.table.drop(columns=droped_columns)

    @classmethod
    def validate_data(cls, data: ExperimentDataType) -> ExperimentDataType:
        """Validate the data of the experiment.

        Args:
            data (ExperimentDataType): The data to validate.

        Raises:
            TypeError: If data is not an instance of ExperimentDataType or
            if the first element of data is not an instance of Artifact or
            if the second element of data is not an instance of Table.

        Returns:
            ExperimentDataType: The validated data.
        """
        if not isinstance(data, tuple):
            raise TypeError(f"Data must be a tuple, got {type(data)}.")

        if len(data) != 2:
            raise ValueError(f"Data must be a tuple of length 2, got {len(data)}.")

        artifact, table = data
        if not isinstance(artifact, Artifact):
            raise TypeError(
                f"Type of attribute data is {ExperimentDataType}, and data[0] must be Artifact instead of {type(artifact).__name__}."
            )
        if not isinstance(table, Table):
            raise TypeError(
                f"Type of attribute data is {ExperimentDataType}, and data[1] must be Table instead of {type(artifact).__name__}."
            )
        return data

    def view(self) -> tuple[dict, pd.DataFrame]:
        """Return a tuple of the artifact dictionary and table dataframe."""
        return (self.data[0].view(), self.data[1].view())

    def append(self, record: Record) -> None:
        """Append a new record to the experiment.

        Args:
            record (Record): The record to be appended to the experiment.
        """
        state = getattr(self, "state")
        state.append(self, record)

    def save(self):
        """Save the experiment."""
        pathlib.Path(self.savedir).mkdir(parents=True, exist_ok=True)
        state = getattr(self, "state")
        state.save(self)


class _ExperimentState(metaclass=abc.ABCMeta):
    def __init__(self, index: tp.Hashable = 0) -> None:
        self.index = index

    @abc.abstractmethod
    def append(self, context: Experiment, record: Record) -> None:
        pass

    @abc.abstractmethod
    def save(self, context: Experiment) -> None:
        pass


class _Created(_ExperimentState):
    def append(self, context: Experiment, record: Record) -> None:
        record.name = self.index
        _append(context, record)
        if isinstance(self.index, int):
            self.index += 1
        context.state = _Waiting(self.index)

    def save(self, context: Experiment) -> None:
        save(context, savedir=context.savedir)


class _Waiting(_ExperimentState):
    def append(self, context: Experiment, record: Record) -> None:
        record.name = self.index
        _append(context, record)
        if isinstance(self.index, int):
            self.index += 1

    def save(self, context: Experiment) -> None:
        save(context, savedir=context.savedir)


class _Running(_ExperimentState):
    def append(self, context: Experiment, record: Record) -> None:
        run_id = ID().data
        if isinstance(self.index, str):
            record.name = (self.index, run_id)
        elif isinstance(self.index, tp.Iterable):
            record.name = (*self.index, run_id)
        else:
            record.name = (self.index, run_id)
        _append(context, record)

    def save(
        self,
        context: Experiment,
    ) -> None:
        a, t = context.data
        latest = t.index[-1]

        ai = Artifact({latest: a.data[latest]}, a.name)
        ti = Table(t.data.loc[[latest]], t.name)

        experiment = Experiment(
            (ai, ti), context.name, autosave=context.autosave, savedir=context.savedir
        )
        save(experiment, savedir=context.savedir, mode="a")


def _append(context: Experiment, record: Record) -> None:
    concat: Concat[Experiment] = Concat()
    data = (ArtifactFactory()([record]), TableFactory()([record]))
    other = type(context)(
        data, context.name, autosave=context.autosave, savedir=context.savedir
    )
    node = context.apply(
        concat,
        [other],
        name=context.name,
        autosave=context.autosave,
        savedir=context.savedir,
    )
    context._init_attrs(node)
