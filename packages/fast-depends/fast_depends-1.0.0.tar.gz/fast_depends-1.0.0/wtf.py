import contextlib
from fast_depends import inject, Depends

@contextlib.contextmanager
def dep():
    print("here")
    return 1

@inject
def func(d = Depends(dep)):
    return d

func()