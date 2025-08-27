
from typing import Callable

class LogMove:

    def __init__(self, message):
        self.message: str = message
        self.function: Callable = None

    def __call__(self, func) -> Callable:
        """called by @ operator with fibonacci as an argument"""
        self.function = func

        def log_message(instance, *args, **kwargs):
            print(
                self.function.__name__,
                "from",
                instance.__class__.__name__,
                "called with",
                args,
            )
            result = self.function(
                instance, *args, **kwargs
            )  # calls the addition function
            print(self.message)  # actions after addition
            return result

        return log_message
