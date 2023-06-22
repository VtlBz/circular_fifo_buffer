from custom_exception import BufferException


class FIFOBuffer:
    def __init__(self, max_size: int):
        self.__max_size: int = max_size
        self.__queue: list = [None] * self.__max_size
        self.__tail: int = 0
        self.__head: int = -1
        self.__size: int = 0

    def put(self, value) -> None:
        if self.__size == self.__max_size:
            raise BufferException('full')
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            raise BufferException('empty')
        self.__head = (self.__head + 1) % self.__max_size
        value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__size -= 1
        return value

    def get_size(self) -> int:
        return self.__size

    def get_queue(self) -> list:
        return self.__queue
