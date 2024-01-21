import shutil


def copy(generator, target_path):
    shutil.copyfile(generator(), target_path)
