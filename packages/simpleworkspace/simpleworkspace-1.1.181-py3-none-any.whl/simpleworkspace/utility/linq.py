from collections.abc import Iterator
from typing import Callable, Iterable, TypeVar, Type, Any
T = TypeVar('T')

class Linq(Iterator[T]):
    """
    A LINQ-inspired wrapper class for Python iterators.
    This class provides LINQ-like functionality for iterating over collections in a concise and expressive manner.
    """
    def __init__(self, iterable: Iterable[T]):
        """ :param iterable: The iterable to be wrapped. """
        self._iterable = iterable

    def Map(self, func: Callable[[T], Any]):
        """
        Transforms each element of an iterable into a new form with the return values of func.
        
        :param func: The function to apply to each item in the collection.
        """
        return Linq(map(func, self))
    
    def Where(self, predicate: Callable[[T], bool]):
        """
        Returns an iterable containing only items that satisfy the given predicate.

        :param predicate: The predicate function used to filter the items.
        """
        return Linq(filter(predicate, self))

    def First(self, predicate: Callable[[T], bool] = None) -> T:
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
    
    def Last(self, predicate: Callable[[T], bool] = None) -> T:
        """
        Returns the last item in the iterable that satisfies the given predicate.
        If no predicate is provided, returns the last item in the iterable.
        """
        if hasattr(self._iterable, "__reversed__"):
            # If the iterable supports __reversed__(), use reversed()
            for item in reversed(self._iterable):
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

    def All(self, predicate: Callable[[T], bool]|T) -> bool:
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

    def Any(self, predicate: Callable[[T], bool]|T) -> bool:
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

    def Distinct(self, predicate: Callable[[T], Any]=None):
        """
        Returns an iterable of distinct elements based on the given condition.

        :param predicate: A function to extract a key from each element for comparison.
                        If not provided, the default is to use the elements themselves.
        """
        if(predicate is None):
            return Linq(set(self))
        seen = set()
        result = []
        for item in self:
            key = predicate(item)
            if key not in seen:
                seen.add(key)
                result.append(item)
        return Linq(result)
    
    def OrderBy(self, predicate: Callable[[T], Any], descending: bool = False):
        """
        Returns a new iterable sorted by the given key function.

        :param predicate: A function to extract a key from each element for sorting.
        :param descending: If True, sorts the elements in descending order. Default is False.
        """
        return Linq(sorted(self, key=predicate, reverse=descending))
    
    def Sorted(self, descending: bool = False):
        return Linq(sorted(self, reverse=descending))

    def ToList(self):
        return list(self)

    def __iter__(self):
        return iter(self._iterable)

    def __next__(self) -> T:
        # Delegating the iteration to the wrapped iterator
        return next(iter(self._iterable))

