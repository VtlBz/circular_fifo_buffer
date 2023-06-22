from custom_exception import BufferException
from fifo_buffer_v2 import FIFOBuffer as Buffer


def manual_test() -> None:
    buffer_max_size: int = int(input())
    my_buffer = Buffer(buffer_max_size)
    while True:
        command, *value = input().split()
        if command in ('q', 'quit', 'exit'):
            break
        method = getattr(my_buffer, command, None)
        if method:
            try:
                result = method(*value)
                if result is not None:
                    print(result)
            except (BufferException, TypeError) as ex:
                print(ex)
        else:
            print(f'Command "{command}" not recognized')


if __name__ == '__main__':
    manual_test()
