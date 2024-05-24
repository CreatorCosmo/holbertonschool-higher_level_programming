class CountedIterator:
    """
    An iterator that extends the functionality of a standard iterator to keep track
    of the number of items that have been iterated over.
    """
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Parameters:
        iterable (iterable): The iterable to be iterated over.
        """
        self.iterator = iter(iterable)  # Convert the iterable to an iterator
        self.count = 0  # Initialize the counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        
        Raises:
        StopIteration: When no more items are available in the iterator.
        
        Returns:
        object: The next item from the iterator.
        """
        try:
            item = next(self.iterator)  # Get the next item from the iterator
            self.count += 1  # Increment the count
            return item
        except StopIteration:
            raise  # Re-raise the StopIteration exception

    def get_count(self):
        """
        Get the current count of items iterated over.

        Returns:
        int: The number of items that have been fetched from the iterator.
        """
        return self.count

# Testing the CountedIterator
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(my_list)

    try:
        while True:
            item = next(counted_iter)
            print(item)  # Optionally print each item to verify
    except StopIteration:
        pass

    print("Total items iterated:", counted_iter.get_count())  # Print the count of iterated items
