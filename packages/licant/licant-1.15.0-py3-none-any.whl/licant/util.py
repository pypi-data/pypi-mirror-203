import os
import inspect
import types
import re
import fnmatch
import functools
import warnings
import random
from collections import defaultdict

string_types = (type(b""), type(u""))


def invert_depends_dictionary(depends_dictionary):
    inverse_dictionary = {}
    for target in depends_dictionary:
        inverse_dictionary[target] = set()

    for target in depends_dictionary:
        deps_of_target = depends_dictionary[target]
        for dep in deps_of_target:
            inverse_dictionary[dep].add(target)
    return inverse_dictionary


def random_string(length):
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyz") for i in range(length))


def deprecated(reason):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """

    if isinstance(reason, string_types):

        # The @deprecated is used with a 'reason'.
        #
        # .. code-block:: python
        #
        #    @deprecated("please, use another function")
        #    def old_function(x, y):
        #      pass

        def decorator(func1):

            if inspect.isclass(func1):
                fmt1 = "Call to deprecated class {name} ({reason})."
            else:
                fmt1 = "Call to deprecated function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter("always", DeprecationWarning)
                warnings.warn(
                    fmt1.format(name=func1.__name__, reason=reason),
                    category=DeprecationWarning,
                    stacklevel=2,
                )
                warnings.simplefilter("default", DeprecationWarning)
                return func1(*args, **kwargs)

            return new_func1

        return decorator

    elif inspect.isclass(reason) or inspect.isfunction(reason):

        # The @deprecated is used without any 'reason'.
        #
        # .. code-block:: python
        #
        #    @deprecated
        #    def old_function(x, y):
        #      pass

        func2 = reason

        if inspect.isclass(func2):
            fmt2 = "Call to deprecated class {name}."
        else:
            fmt2 = "Call to deprecated function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter("always", DeprecationWarning)
            warnings.warn(
                fmt2.format(name=func2.__name__),
                category=DeprecationWarning,
                stacklevel=2,
            )
            warnings.simplefilter("default", DeprecationWarning)
            return func2(*args, **kwargs)

        return new_func2

    else:
        raise TypeError(repr(type(reason)))


def error(str):
    print(red("LicantError: ") + str)
    exit(-1)


def error_exception(str, ex):
    import traceback

    print(red("LicantException: ") + str)
    print(ex.__class__)
    traceback.print_exc()
    exit(-1)


def cutinvoke(func, *args, **kwargs):
    if isinstance(func, types.FunctionType):
        ins = inspect.getargspec(func)
        nargs = len(ins.args)
        return func(*args[:nargs])
    else:
        return func(*args)


class quite:
    pass


class queue:
    class DontHaveArg:
        pass

    def __init__(self):
        self.lst = []
        self.rdr = 0

    def put(self, obj):
        self.lst.append(obj)

    def get(self):
        if len(self.lst) == 0:
            raise Exception("DontHaveArg")

        ret = self.lst[self.rdr]

        self.rdr += 1
        if self.rdr >= len(self.lst):
            self.__init__()

        return ret

    def empty(self):
        return len(self.lst) == 0

    def __str__(self):
        return str(self.lst)


def textblock(str):
    return chr(27) + str + chr(27) + "[0m"


def black(str):
    return textblock("[30;1m" + str)


def red(str):
    return textblock("[31;1m" + str)


def green(str):
    return textblock("[32;1m" + str)


def yellow(str):
    return textblock("[33;1m" + str)


def purple(str):
    return textblock("[35;1m" + str)


def cyan(str):
    return textblock("[36;1m" + str)


def white(str):
    return textblock("[37;1m" + str)


def always_true(*args, **kwargs):
    return True


def always_false(*args, **kwargs):
    return False


def do_nothing(*args, **kwargs):
    pass


def changeext(path, newext):
    return os.path.splitext(path)[0] + "." + newext


def flag_prefix(pref, lst):
    if lst and lst != []:
        return " ".join(map(lambda x: pref + x, lst))
    else:
        return ""


def find_recursive(root, pattern, hide, debug):
    result = []

    if hide is None:
        for d, dirs, files in os.walk(root):
            for f in files:
                if pattern in f:
                    path = os.path.join(d, f)
                    if debug:
                        print(path)
                    result.append(path)

    else:
        for d, dirs, files in os.walk(root):
            if hide not in d:
                for f in files:
                    if pattern in f:
                        path = os.path.join(d, f)
                        if debug:
                            print(path)
                        result.append(path)

    return result


cxx_read_depends_pattern = re.compile(r"[\w./-]+")


def cxx_read_depends(path):
    if not os.path.exists(path):
        return None
    else:
        f = open(path)
        text = f.read()

        if len(text) == 0:
            return None

        lst = cxx_read_depends_pattern.findall(text)
        return lst[2:]


def get_actions(target):
    clsactions = list(target.__actions__)
    # objactions = [k for k in target.__dict__.keys() if callable(target.__dict__[k])]
    return sorted(clsactions)

    # return target.__dict__


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results


class DefaultDictLazy(defaultdict):
    def __init__(self, foo):
        super().__init__()
        self.foo = foo

    def __missing__(self, key):
        val = self.foo(key)
        self[key] = val
        return val


canonical_path_lazy_store = DefaultDictLazy(lambda path: os.path.realpath(path))


def canonical_path(path):
    return canonical_path_lazy_store[path]
