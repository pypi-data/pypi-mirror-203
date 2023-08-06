import abc


class Pipe(abc.ABC):
    @abc.abstractmethod
    def __call__(self, string: str) -> str:
        ...

    def __rgt__(self, string: str) -> str:
        return self.__call__(string)

    def __gt__(self, string: str) -> str:
        return self.__call__(string)

    def __rrshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rlshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rlt__(self, string: str) -> str:
        return self.__call__(string)

    def __lt__(self, string: str) -> str:
        return self.__call__(string)

    def __lshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rpow__(self, string: str) -> str:
        return self.__call__(string)

    def __pow__(self, string: str) -> str:
        return self.__call__(string)
