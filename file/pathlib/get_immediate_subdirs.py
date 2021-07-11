import os
import pathlib
import timeit
import glob

path = "D:\\dev\\4_python3_learn"


def a():
    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
    # print(len(list_subfolders_with_paths))


def b():
    list_subfolders_with_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # print(len(list_subfolders_with_paths))


def c():
    list_subfolders_with_paths = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            list_subfolders_with_paths.append( os.path.join(root, dir) )
        break
    # print(len(list_subfolders_with_paths))


def d():
    list_subfolders_with_paths = glob.glob(path + '/*/')
    # print(len(list_subfolders_with_paths))


def e():
    list_subfolders_with_paths = list(filter(os.path.isdir, [os.path.join(path, f) for f in os.listdir(path)]))
    # print(len(list(list_subfolders_with_paths)))


def f():
    p = pathlib.Path(path)
    list_subfolders_with_paths = [x for x in p.iterdir() if x.is_dir()]
    # print(len(list_subfolders_with_paths))



print(f"Scandir:          {timeit.timeit(a, number=1000):.3f}")
print(f"Listdir:          {timeit.timeit(b, number=1000):.3f}")
print(f"Walk:             {timeit.timeit(c, number=1000):.3f}")
print(f"Glob:             {timeit.timeit(d, number=1000):.3f}")
print(f"Listdir (filter): {timeit.timeit(e, number=1000):.3f}")
print(f"Pathlib:          {timeit.timeit(f, number=1000):.3f}")