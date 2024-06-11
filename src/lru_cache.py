import abc


class Node:

    def __init__(self, key: int, val: int):
        """
        Function docstring: This function initializes a Node with a key and a value.

        Args:
            key: int : The key of the node.
            val: int : The value of the node.
        """
        if not isinstance(key, int) or not isinstance(val, int):
            raise ValueError("Key and value must be integers.")
        self.key = key
        self.val = val
        self.prev: Node = None
        self.next: Node = None


class Cache(abc.ABC):

    @abc.abstractmethod
    def get(self, key: int) -> int:
        """
        Function docstring: This function gets the value of a key from the cache.

        Args:
            key: int : The key to get the value for.

        Returns:
            int : The value of the key, or -1 if the key is not in the cache.
        """

    @abc.abstractmethod
    def put(self, key: int, value: int) -> None:
        """
        Function docstring: This function adds a key-value pair to the cache.
        If the key already exists, it updates the value and moves the key to the end of the cache.
        If the cache is full, it removes the least recently used key-value pair
        before adding the new one.

        Args:
            key: int : The key to add.
            value: int : The value to add.
        """


class LRUCache(Cache):

    def __init__(self, capacity: int):
        """
        Function docstring: This function initializes an LRUCache with a specified capacity.

        Args:
            capacity: int : The capacity of the cache.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node) -> None:
        """
        Function docstring: This function removes a node from the linked list.

        Args:
            node: Node : The node to be removed.
        """
        if not isinstance(node, Node) or node is self.head or node is self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node(self, node: Node) -> None:
        """
        Function docstring: This function adds a node to the end of the linked list.

        Args:
            node: Node : The node to be added.
        """
        if not isinstance(node, Node):
            return
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        """
        Function docstring: This function gets the value of a key from the cache.

        Args:
            key: int : The key to get the value for.

        Returns:
            int : The value of the key, or -1 if the key is not in the cache.
        """
        if not isinstance(key, int):
            raise ValueError("Key must be an integer.")

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove_node(node)
        self._add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Function docstring: This function adds a key-value pair to the cache.
        If the key already exists, it updates the value and moves the key to the end of the cache.
        If the cache is full, it removes the least recently used key-value pair
        before adding the new one.

        Args:
            key: int : The key to add.
            value: int : The value to add.
        """
        if not isinstance(key, int) or not isinstance(value, int):
            raise TypeError("Key and value must be integers.")

        if key in self.cache:
            self._remove_node(self.cache[key])
        elif len(self.cache) == self.capacity:
            node = self.head.next
            self._remove_node(node)
            del self.cache[node.key]

        node = Node(key, value)
        self._add_node(node)
        self.cache[key] = node


def new_lru_cache(capacity: int) -> Cache:
    """
    Function docstring: This function creates a new LRUCache object with the specified capacity.

    Args:
        capacity: int : The capacity of the cache.

    Returns:
        LRUCache : A new LRUCache object.
    """
    return LRUCache(capacity)
