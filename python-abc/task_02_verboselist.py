class VerboseList(list):
    """
    A custom list that provides notifications when items are added or removed.
    It extends the built-in list class and overrides methods to include verbose output.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.
        
        Parameters:
        item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending all items from the iterable and print a notification.
        
        Parameters:
        iterable: An iterable with items to extend the list.
        """
        item_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {item_count} items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a notification.
        
        Parameters:
        item: The item to be removed from the list.
        """
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """
        Pop an item at the specified index from the list and print a notification.
        Defaults to the last item if the index is not specified.
        
        Parameters:
        index: The index of the item to be popped. Default is -1 (last item).
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item

# Testing the VerboseList class
verbose_list = VerboseList()

# Testing append
verbose_list.append('apple')
verbose_list.append('banana')

# Testing extend
verbose_list.extend(['cherry', 'date'])

# Testing remove
verbose_list.remove('banana')

# Testing pop
verbose_list.pop()
verbose_list.pop()
