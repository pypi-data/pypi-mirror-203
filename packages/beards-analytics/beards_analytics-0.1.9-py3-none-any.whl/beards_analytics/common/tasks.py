from threading import Thread
import functools
import typing as t
from .types import T, RT, P


class Task(Thread, t.Generic[T]):
    def __init__(self, group=None, target=None, name=None, args=None, kwargs=None):
        args = args or tuple()
        kwargs = kwargs or dict()
        
        Thread.__init__(self, group, target, name, args, kwargs)

        self._result: t.Optional[T] = None

    @property
    def result(self) -> t.Optional[T]:
        return self._result

    def run(self):
        try:
            if self._target is not None:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._result, self._args, self._kwargs

    def wait(self, timeout: t.Optional[float] = None) -> T:
        if self.result:
            return self.result
        Thread.join(self, timeout=timeout)
        return self.result

    @classmethod
    def wait_all(cls, *tasks: "Task[T]") -> t.List[T]:
        results = []
        for task in tasks:
            results.append(task.wait())
        return results

def task(func: t.Callable[P, RT]) -> t.Callable[P, Task[RT]]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Task[RT]:
        thread = Task(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper
