from collections.abc import Iterator
from typing import Callable, Iterable, TypeVar, Type, Any
from itertools import islice

_T = TypeVar('_T')
_K = TypeVar('_K')

class LINQ(Iterator[_T]):
    """
    A LINQ-inspired wrapper class for Python iterators.
    This class provides LINQ-like functionality for iterating over collections in a concise and expressive manner.
    """
    def __init__(self, iterable: Iterable[_T]):
        """ :param iterable: The iterable to be wrapped. """
        self._collection = iterable
        self._iterator = iter(self._collection)
    
    def Map(self, func: Callable[[_T], Any]):
        """
        Transforms each element of an iterable into a new form with the return values of func.
        
        :param func: The function to apply to each item in the collection.
        """
        return LINQ(map(func, self))
   
    def Where(self, predicate: Callable[[_T], bool]):
        """
        Returns an iterable containing only items that satisfy the given predicate.

        :param predicate: The predicate function used to filter the items.
        """
        return LINQ(filter(predicate, self))
   
    def First(self, predicate: Callable[[_T], bool] = None) -> _T:
        """
        Returns the first item in the iterable that satisfies the given predicate.
        If no predicate is provided, returns the first item in the iterable.
        """
        if(predicate is None):
            return next(iter(self))
        for item in self:
            if predicate(item):
                return item
        raise ValueError("No item satisfies the given predicate")
    
    def FirstOrDefault(self, predicate: Callable[[_T], bool] = None) -> _T:
        try:
            return self.First(predicate=predicate)
        except (ValueError, StopIteration):
            return None
   
    def Last(self, predicate: Callable[[_T], bool] = None) -> _T:
        """
        Returns the last item in the iterable that satisfies the given predicate.
        If no predicate is provided, returns the last item in the iterable.
        """
        if hasattr(self._collection, "__reversed__"):
            # If the iterable supports __reversed__(), use reversed()
            for item in reversed(self._collection):
                if predicate is None or predicate(item):
                    return item
            raise ValueError("No item satisfies the given predicate.")
        
        # If the iterable does not support __reversed__(), iterate over all items
        # in forward order and keep track of the last item that satisfies the predicate
        last_item = None
        for item in self:
            if predicate is None or predicate(item):
                last_item = item
        if last_item is not None:
            return last_item
        # Raise an exception if no item satisfies the predicate
        raise ValueError("No item satisfies the given predicate.")
   
    def LastOrDefault(self, predicate: Callable[[_T], bool] = None) -> _T:
        try:
            return self.Last(predicate=predicate)
        except (ValueError, StopIteration):
            return None

    def ElementAt(self, index:int) -> _T:
        return next(islice(self._collection, index, index + 1))

    def ElementAtOrDefault(self, index:int) -> _T:
        try:
            return self.ElementAt(index)
        except (ValueError, StopIteration):
            return None
    
    def Empty(self):
        """
        Determines if the iterable is empty.

        :return: True if the iterable is empty, False otherwise.
        """
        try:
            # Try to advance the iterator and check if it raises a StopIteration exception
            next(self._iterator)
            return False
        except StopIteration:
            return True
    def Skip(self, count: int):
        """
        Bypasses a specified number of elements in the iterable and returns the remaining elements.

        :param count: The number of elements to skip.
        """
        return LINQ(islice(self, count, None))
   
    def Take(self, count: int):
        """
        Returns a specified number of contiguous elements from the iterable.

        :param count: The number of elements to take.
        """
        return LINQ(islice(self, count))
   
    def All(self, predicate: Callable[[_T], bool]|_T) -> bool:
        """    
        Determines whether all elements of the iterable satisfy a given condition.

        :param predicate: A condition function or a value to compare the elements against
        """
        if(not callable(predicate)):
            value = predicate
            predicate = lambda x: x == value
        for item in self:
            if not predicate(item):
                return False
        return True
   
    def Any(self, predicate: Callable[[_T], bool]|_T) -> bool:
        """    
        Determines whether any element of iterable satisfies a given condition.

        :param predicate: A condition function or a value to compare the elements against
        """
        if(not callable(predicate)):
            value = predicate
            predicate = lambda x: x == value
        for item in self:
            if predicate(item):
                return True
        return False
   
    def Distinct(self, predicate: Callable[[_T], Any]=None):
        """
        Returns an iterable of distinct elements based on the given condition.

        :param predicate: A function to extract a key from each element for comparison.
                        If not provided, the default is to use the elements themselves.
        """
        if(predicate is None):
            return LINQ(set(self))
        seen = set()
        result = []
        for item in self:
            key = predicate(item)
            if key not in seen:
                seen.add(key)
                result.append(item)
        return LINQ(result)
   
    def OrderBy(self, predicate: Callable[[_T], Any], descending: bool = False):
        """
        Returns a new iterable sorted by the given key function.

        :param predicate: A function to extract a key from each element for sorting.
        :param descending: If True, sorts the elements in descending order. Default is False.
        """
        return LINQ(sorted(self, key=predicate, reverse=descending))
   
    def GroupBy(self, key_selector: Callable[[_T], _K]) -> dict[_K, list[_T]]:
        """
        Groups the elements of the iterable based on the given key selector function.

        :param key_selector: A function to extract a key from each element for grouping.
        :return: A dictionary where the keys are the group keys and the values are lists of elements in each group.
        """

        from collections import defaultdict

        groups = defaultdict(list)
        for item in self:
            key = key_selector(item)
            groups[key].append(item)
        return dict(groups)
   
    def Aggregate(self, func: Callable[[_T, _T], _T], seed: _T = None) -> _T:
        """
        Applies an accumulator function to the iterable and returns the final result.
        :param func: The accumulator function to apply to the iterable.
        :param seed: The optional seed value for the accumulator. If not provided, the first element of the iterable is used as the seed.
        :return: The final result of the aggregation.
        """
        
        # Iterate over the iterable and apply the accumulator function to each element
        for i, item in enumerate(self):
            # If seed is not provided, use the first element of the iterable as the initial accumulator value
            if(i == 0 and seed is None): 
                seed = item
                continue
            seed = func(seed, item)

        # Return the final accumulator value
        return seed
   
    def Min(self, predicate: Callable[[_T], Any] = None):
        return min(self._collection, key=predicate)
   
    def Max(self, predicate: Callable[[_T], Any] = None):
        return max(self._collection, key=predicate)
   
    def Count(self, predicate: Callable[[_T], bool] = None) -> int:
        """
        Returns the number of elements in the iterable that satisfy the given predicate.
        If no predicate is provided, returns the total number of elements in the iterable.

        :param predicate: The predicate function used to filter the items.
        :return: The number of elements that satisfy the given predicate.
        """
        
        if predicate is None:
            if hasattr(self._collection, "__len__"):
                return len(self._collection)
            # If the iterable does not support __len__(), iterate over all items counting them
            return sum(1 for _ in self)

        return sum(1 for item in self if predicate(item))
   
    def Sorted(self, descending: bool = False):
        return LINQ(sorted(self, reverse=descending))
   
    def ToList(self):
        return list(self)
    
    def __iter__(self):
        return self._iterator
   
    def __next__(self) -> _T:
        # Delegating the iteration to the wrapped iterator
        return next(self._iterator)


