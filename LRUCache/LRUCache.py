import logging


class DLLNode:
    """Double linked list's node"""

    def __init__(self, key: str, value: str) -> None:
        self.value: str = value
        self.key: str = key
        self.prev: DLLNode
        self.next: DLLNode


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        """Init:
            - hash map of keys (dictionary),
            that makes the time of get() to be O(1)
            - doubly linked list of nodes,
            that makes the nodes add/rem operations O(1)
            - count of nodes

        Args:
            capacity (int): max cache capacity
        """
        self.__capacity: int = capacity
        self.__map: dict[str, DLLNode] = {}
        self.__head: DLLNode = DLLNode("0", "0")
        self.__tail: DLLNode = DLLNode("0", "0")
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__count: int = 0

    def get(self, key: str) -> str:
        if key in self.__map:
            node: DLLNode = self.__map[key]
            result: str = node.value
            self.__deleteNode(node)
            self.__addToHead(node)
            logging.info("got the value : {} for the key: {}".format(result, key))
            return result
        else:
            raise KeyError("no such key exists: {}".format(key))

    def set(self, key: str, value: str) -> None:
        logging.info("going to set the (key, value) : ({}, {})".format(key, value))
        if key in self.__map:
            self.__updateNode(key, value)
        else:
            self.__addNode(key, value)

    def rem(self, key: str) -> None:
        if key in self.__map:
            node: DLLNode = self.__map[key]
            del self.__map[key]
            self.__deleteNode(node)
            self.__count -= 1
            logging.info("node by the key ({}) was deleted".format(key))
        else:
            raise KeyError("no such key exists: {}".format(key))

    def __updateNode(self, key: str, value: str) -> None:
        node: DLLNode = self.__map[key]
        node.value = value
        self.__deleteNode(node)
        self.__addToHead(node)

    def __addNode(self, key: str, value: str) -> None:
        node: DLLNode = DLLNode(key, value)
        self.__map[key] = node
        if self.__count < self.__capacity:
            self.__count += 1
            self.__addToHead(node)
        else:
            del self.__map[self.__tail.prev.key]
            self.__deleteNode(self.__tail.prev)
            self.__addToHead(node)

    def __deleteNode(self, node: DLLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __addToHead(self, node: DLLNode) -> None:
        node.next = self.__head.next
        node.next.prev = node
        node.prev = self.__head
        self.__head.next = node
