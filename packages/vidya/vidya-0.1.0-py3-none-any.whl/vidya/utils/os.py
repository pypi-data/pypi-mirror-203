import os


def create_dir_if_not_exists(path: str):
    if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
