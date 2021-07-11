"""
Credit:  
    BY Terry Davis 
    https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python

Usage:
>>> size = get_folder_size("c:/users/tdavis/downloads")
>>> print(size)
5.81 GB
>>> size.GB
5.810891855508089
>>> size.gigabytes
5.810891855508089
>>> size.PB
0.005674699077644618
>>> size.MB
5950.353260040283
>>> size
ByteSize(6239397620)
"""
################################################
from fs.osfs import OSFS
from pathlib import Path


def get_folder_size(folder : Path):
    return ByteSize(sum(file.stat().st_size for file in folder.rglob('*')))


class ByteSize(int):

    _kB = 1024
    _suffixes = 'B', 'kB', 'MB', 'GB', 'PB'

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.bytes = self.B = int(self)
        self.kilobytes = self.kB = self / self._kB**1
        self.megabytes = self.MB = self / self._kB**2
        self.gigabytes = self.GB = self / self._kB**3
        self.petabytes = self.PB = self / self._kB**4
        *suffixes, last = self._suffixes
        suffix = next((
            suffix
            for suffix in suffixes
            if 1 <= getattr(self, suffix) < self._kB
        ), last)
        self.readable = suffix, getattr(self, suffix)

        super().__init__()

    def __str__(self):
        return self.__format__('.2f')

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, super().__repr__())

    def __format__(self, format_spec):
        suffix, val = self.readable
        return '{val:{fmt}} {suf}'.format(val=val, fmt=format_spec, suf=suffix)

    def __sub__(self, other):
        return self.__class__(super().__sub__(other))

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __mul__(self, other):
        return self.__class__(super().__mul__(other))

    def __rsub__(self, other):
        return self.__class__(super().__sub__(other))

    def __radd__(self, other):
        return self.__class__(super().__add__(other))

    def __rmul__(self, other):
        return self.__class__(super().__rmul__(other))   


if __name__ == "__main__":

    # path_to_walk = Path("D:\\dev\\4_python3_learn\\file")
    path_to_walk = Path("D:\\dev\\4_python3_learn")
    print(path_to_walk)

    size = get_folder_size(path_to_walk)
    print(size)

    # size2 = ByteSize(1023)
    # print(size2)

    # create a basic file walker
    with OSFS(path_to_walk) as myfs:
        print("-- Directories --")
        # TODO: use the dirs walker for directories
        for path in myfs.walk.dirs(max_depth=1, exclude_dirs=['.git', '.vscode', '.pytest_cache']):
            cur_dir = path_to_walk.joinpath(path[1:])
            print(get_folder_size(cur_dir), path)
