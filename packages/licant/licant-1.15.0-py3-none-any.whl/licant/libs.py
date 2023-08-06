from licant.scripter import scriptq
from licant.util import yellow
import licant.core

import os
import json

gpath = "/var/lib/licant"
lpath = os.path.expanduser("~/.licant")

libs = None

included = dict()


def merge_two_dicts(x, y):
    z = x.copy()  # start with x's keys and values
    z.update(y)  # modifies z with y's keys and values & returns None
    return z


glibs = {}
llibs = {}


def init():
    global libs, glibs, llibs

    if os.path.exists(gpath):
        glibs = json.load(open(gpath))

    if os.path.exists(lpath):
        llibs = json.load(open(lpath))

    libs = merge_two_dicts(glibs, llibs)


def include(lib, path=None, local_tunel=None):
    if libs is None:
        init()

    if lib in included:
        if path and path != included[lib]:
            print(
                "Warning: prevent library by path({}) include becouse library been include early with another path({})".format(path, included[lib]))
        return

    if path is not None:
        included[lib] = path

        print_about_lib(lib, path)
        scriptq.execute(path)
        return

    if local_tunel is not None:
        # Local tunel is special technique for use licant
        # with python packages. Local tunel create link
        # for setup.py can find sources by relative path.

        if not os.path.exists(local_tunel[0]):
            # Убеждаемся, что директории до тунеля существуют
            if not os.path.exists(os.path.dirname(local_tunel[0])):
                os.makedirs(os.path.dirname(local_tunel[0]))

            rawdir = os.path.dirname(libs[lib])

            if not os.path.exists(local_tunel[0]):
                os.symlink(rawdir, local_tunel[0])

            included[lib] = os.path.join(local_tunel[0], local_tunel[1])
            scriptq.execute(os.path.join(local_tunel[0], local_tunel[1]))
            return

        else:
            included[lib] = os.path.join(local_tunel[0], local_tunel[1])
            scriptq.execute(os.path.join(local_tunel[0], local_tunel[1]))
            return

    if lib not in libs:
        print(
            "Unregistred library {}. Use licant-config utility or manually edit {} or {} file. NOTE: If you use local libraries, maybe you need to reorder your includes".format(
                yellow(lib), yellow(lpath), yellow(gpath)
            )
        )
        exit(-1)

    included[lib] = libs[lib]
    print_about_lib(lib, libs[lib])
    scriptq.execute(libs[lib])


def print_about_lib(lib, path):
    if licant.core.default_core().runtime["debug"]:
        print(f"LICANTLIB {lib} {path}")


def print_system_libs(taget, *args):
    if libs is None:
        init()

    keys = sorted(libs.keys())
    for k in keys:
        print("{}: {}".format(k, libs[k]))


def print_included_libs(taget, *args):
    keys = sorted(included.keys())
    for k in keys:
        print("{}: {}".format(k, included[k]))


libs_target = licant.core.Target(
    tgt="l",
    deps=[],
    list=print_system_libs,
    included=print_included_libs,
    actions={
        "list",
        "included"
    }, __help__="Licant libs info"
)

licant.core.default_core().add(libs_target)
