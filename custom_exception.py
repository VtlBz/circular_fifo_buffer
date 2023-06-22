class BufferException(LookupError):
    __error_msg: str = 'Error: Buffer is {msg}'

    def __init__(self, msg):
        super().__init__(self.__error_msg.format(msg=msg))
