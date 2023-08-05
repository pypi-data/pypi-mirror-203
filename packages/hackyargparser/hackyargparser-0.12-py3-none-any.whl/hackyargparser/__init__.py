import os
import sys
from ast import literal_eval
from functools import wraps
from itertools import tee

config = sys.modules[__name__]
config.parsedargs = {}
config.allsysargs = [ini for ini, x in enumerate(sys.argv) if x.startswith("-")]
config.helptext = ""
config.stop_after_kill = True


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def iter_split_by_index(iterable, indexes):
    return (iterable[p[0] : p[1]] for p in pairwise([0] + indexes + [len(iterable)]))


def show_and_exit():
    print(config.helptext)
    if config.stop_after_kill:
        input()
    try:
        sys.exit(1)
    finally:
        os._exit(1)


def parse_ar():
    ges = list(iter_split_by_index(iterable=sys.argv, indexes=config.allsysargs))
    checkset = ("-?", "?", "-h", "--h", "help", "-help", "--help")
    for ini, g in enumerate(ges[1:]):
        try:
            there = g[0] in checkset
            if there:
                raise ValueError
            config.parsedargs[g[0].lstrip("- ")] = g[1]
        except Exception:
            show_and_exit()


parse_ar()


def kill_when_not_there(necessary_keys):
    for key in necessary_keys:
        if key.strip("- ") not in config.parsedargs:
            show_and_exit()


def add_sysargv(f_py=None):
    """
    A decorator function that modifies the default arguments of a given function based on the values passed through
    command line arguments.

    :param f_py: A callable function to be decorated.
    :return: A decorated function with modified default arguments.

    The function first checks if the input function is callable or None. It then retrieves the global dictionary of the
    calling frame and defines a decorator function. The decorator function modifies the default arguments of the input
    function based on the values passed through command line arguments. It does this by retrieving the variable names
    and annotations of the input function and creating a dictionary of all the annotations. It then iterates through
    the default arguments of the input function and tries to convert them to the appropriate data type based on the
    annotations. If the conversion fails, it tries all possible data types until a successful conversion is made. The
    modified default arguments are then set and the input function is called with the modified arguments.
    """
    assert callable(f_py) or f_py is None
    f = sys._getframe(1)
    dct = f.f_globals

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            varnames = dct[func.__name__].__dict__["__wrapped__"].__code__.co_varnames
            allanot = [
                x
                for x in dct[func.__name__]
                .__dict__["__wrapped__"]
                .__annotations__.items()
            ]
            newargs = []
            allanotdict = dict(allanot)
            for a, b in zip(
                varnames, dct[func.__name__].__dict__["__wrapped__"].__defaults__
            ):
                try:
                    dtypegood = False
                    conva = b

                    try:
                        conva = literal_eval(config.parsedargs[a])
                        if type(conva) in allanotdict[a].__args__:
                            dtypegood = True
                    except Exception:
                        pass

                    if not dtypegood:
                        try:
                            for dty in allanotdict[a].__args__:
                                try:
                                    conva = dty(config.parsedargs[a])
                                    break
                                except Exception as fe:
                                    continue
                        except Exception as fa:
                            conva = allanotdict[a](config.parsedargs[a])
                    newargs.append(conva)
                except Exception as adf:
                    newargs.append(b)
                    continue

            setattr(
                dct[func.__name__].__dict__["__wrapped__"],
                "__defaults__",
                tuple(newargs),
            )
            return func(*args, **kwargs)

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
