
import os
import time
from .helpers import encode, get_current_container_name
from .core import PexicdbCursor


def __create_fresh(name: str):
    """
    create fresh directory and file structure
    
    Arguments:
        `name`: name of the container
    """
    
    # create directory of the name
    os.mkdir(name)

    # create data file
    # data files contains the name of the container and the triggers' function
    with open(os.path.join(name, "datafile"), "wb") as f:
        f.write(encode({
            "name": name,
        }))
    
    # create container file
    with open(os.path.join(name, f"container-{time.time()}"), "wb") as f:
        pass


def connect(name: str, model: list, *args, **kwargs) -> PexicdbCursor:
    """
    connect to the container using the name and you have to provide a model
    that is passed to the cursor.

    `connect` function's main work is to create the container if it does not exists
    and create the cursor with all file pointers and return it.


    Arguments:
        `name`: container name

        `model`: model of the list containing fields
    
    Returns:
        returns the PexicdbCursor object to the container
    """
    # if container not found or not exists
    if os.path.exists(name) is not True or os.path.isdir(name) is not True:
        # create new one
        __create_fresh(name)

    return PexicdbCursor(
        name,
        model,
        open(os.path.join(name, "datafile"), "rb+"),
        open(get_current_container_name(name), "rb+"),
        *args,
        **kwargs
    )
