from collections import deque

from custom_exception import BufferException


class FIFOBuffer:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.buffer = deque([], maxlen=max_size)

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def is_full(self) -> bool:
        return len(self.buffer) == self.max_size

    def put(self, value):
        if self.is_full():
            raise BufferException('full')
        self.buffer.append(value)

    def pop(self):
        if self.is_empty():
            raise BufferException('empty')
        return self.buffer.popleft()
