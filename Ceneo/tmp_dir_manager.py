import os
import shutil


def create(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def delete(path):
    try:
        shutil.rmtree(path)
    except OSError:
        print("Deletion of the directory %s failed" % path)
        delete(path)
    else:
        print("Successfully deleted the directory %s" % path)