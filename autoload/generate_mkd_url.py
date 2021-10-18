"""
Author: Wangxianzhuo 
"""
import os
import re
from typing import List


def generate_mkd_url(path: str, suffix: str, ignore: List[str]) -> List[str]:
    """generate_mkd_url.

    Args:
        path (str): generate file link from all files in path, relativa path and global path
            are both supported.
        suffix (str): the suffix of files you want to generate, only single suffix supported.
        ignore (List[str]): some files you want to ignore.

    Returns:
        List[str]:
    """

    # get files I want
    files = os.listdir(path)
    files_wanted = []
    for single_file in files:
        if not single_file.endswith(suffix) or ignore == single_file:
            continue
        absolute_path = os.path.join(path, single_file)
        if os.path.isdir(absolute_path):
            continue
        files_wanted.append(absolute_path)
    del files

    # generate mkd url using filename string
    for i, single_file in enumerate(files_wanted):
        split_file = re.split("/|\.", single_file)
        file_short_name = split_file[-2]
        files_wanted[i] = f"[{file_short_name}]({single_file})\n\n"

    return files_wanted


if __name__ == "__main__":
    path = "../../dailyExe"
    suffix = "py"
    ignore = "__init__.py"

    mkd_urls = generate_mkd_url(path, suffix, ignore)
    for mkd_url in mkd_urls:
        print(mkd_url, end="")
