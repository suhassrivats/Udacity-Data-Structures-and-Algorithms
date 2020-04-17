import os


def find_files_using_walk(suffix, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                print(os.path.join(root, file))
    return None


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix == '':
        return []

    # Base condition
    if len(os.listdir(path)) == 0:
        return []

    path_elements = os.listdir(path)
    path_files = [file for file in path_elements if ('.' + suffix) in file]
    path_folders = [folder for folder in path_elements if '.' not in folder]

    for folder in path_folders:
        path_files.extend(find_files(suffix=suffix, path=path + '/' + folder))

    return path_files


def main():
    # find_files_using_walk('.c', 'testdir')

    # Tests
    path_base = os.getcwd() + '/testdir'

    # Testcase 1
    print(find_files(suffix='c', path=path_base))

    # Testscase 2
    print(find_files(suffix='h', path=path_base))

    # Testcase 3
    print(find_files(suffix='x', path=path_base))


if __name__ == '__main__':
    main()
