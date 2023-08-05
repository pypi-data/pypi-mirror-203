"""Utilities for working with the file system."""
import os
import time
import pathlib
import inductiva

from inductiva import types


def get_timestamped_path(path: types.Path, sep: str = "-") -> pathlib.Path:
    """Return a path that does not exist by appending a timestamp.

    Args:
        path: Path to a file or directory.

    Returns:
        A path that does not exist by appending the timestamp.
    """
    path = pathlib.Path(path)
    timestamp = time.strftime("%Y-%m-%dT%Hh%Mm%Ss")

    name = f"{path.stem}{sep}{timestamp}"

    return path.with_name(name + path.suffix)


def resolve_path(path: types.Path) -> pathlib.Path:
    """Resolve a path relative to the Inductiva package working directory.

    Args:
        path: Path to a file or directory.
    """
    root = pathlib.Path.cwd()

    if inductiva.working_dir:
        root = pathlib.Path(inductiva.working_dir)

    return pathlib.Path(root, path)


def get_sorted_files(data_dir: str,
                     file_format: str = "name",
                     split_token: str = "_"):
    """Returns list of files sorted according to [file_key].

    Order a set of .format files of the form
    ['name_1.format', 'name_2.format',...,'name_10.format',
    ...,'name_n.format'].

    The default sorting methods for list, list.sort()
    or sorted(list), order 'name_10.format' before 'name_2.format',
    which is not representative of the time series.

    In this function we sort according to the number..
    """

    if not os.path.exists(data_dir):
        raise IOError(f"Directory '{data_dir}' does not exist.")

    # Get a list of the files in the data directory.
    files = os.scandir(data_dir)

    # The files have file_format extension.
    files = [
        file for file in files if pathlib.Path(file.path).suffix == file_format
    ]

    # Sort the files to be read according to [file_key].
    def get_alphanum_key(file):
        file_name = pathlib.Path(file.path).stem
        file_name_splits = file_name.split(split_token)
        file_key = file_name_splits[-1]
        return int(file_key)

    files = sorted(files, key=get_alphanum_key)

    return files
