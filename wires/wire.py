from collections.abc import Callable

type Action[T] = Callable[[], T]

class Wire:

    def __init__(self):
        self.signal_value: int = 0
        self.actions: list[Action[None]] = list()

    def set_signal_value(self, new_value: int) -> None:
        match new_value:
            case v if v != self.signal_value:
                self.signal_value = new_value
                return call_each(self.actions)

            case _:
                print("set signal value done")

    def add_action[T](self, fn: Action[T]) -> None:
        self.actions.append(fn)
        fn()


def call_each(fns: list[Action]) -> None:
    for fn in fns:
        fn()

    print("done")
