from typing import List, TypeVar, Generic, Callable
from copy import deepcopy

T = TypeVar('T')

# pylint: disable=C0103
TQuery = TypeVar('TQuery', bound='Query')
# pylint: enable=C0103

class Query(Generic[T]):
    def __init__(self: TQuery, sequence: List[T]):
        self._sequence = deepcopy(sequence)

    def filter(self: TQuery, filter_method: Callable[[T], bool]) -> TQuery:
        self._sequence = list(filter(filter_method, self._sequence))
        return self

    def tolist(self: TQuery) -> List[T]:
        return self._sequence
