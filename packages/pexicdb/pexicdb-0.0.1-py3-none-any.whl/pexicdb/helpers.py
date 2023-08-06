import os
import time
import pickle
import base64
import typing


def encode(data):
    """
    Transform the original data argument object using `pickle.dumps()` method
    to bytes and then also encode that bytes using the `base64.urlsafe_b64encode()`
    method.

    Arguments:
        `data`: data to use
    
    Returns:
        encoded object in bytes
    """
    return base64.urlsafe_b64encode(pickle.dumps(data))+b"\n"


def decode(data) -> typing.Any:
    """
    Decode the encoded data into original object, this is reverse process of
    encode function.

    Arguments:
        `data`: data to use
    
    Returns:
        any object that was encoded
    """
    return pickle.loads(base64.urlsafe_b64decode(data.rstrip(b"\n")))


def create_container(path) -> str:
    """
    Create the new container at the given path.

    Basically it's a container file not whole container and the container file
    name is is generated using `time.time()` method.

    ex. `container-{time.time()}` -> `container-1681490140.5154865`

    Arguments:
        `path`: container file to be created on path
    
    Returns:
        [path + container file name] in string
    """
    container_name = f"container-{time.time()}"
    with open(os.path.join(path, container_name), "wb"):
        pass
    return os.path.join(path, container_name)


def get_current_container_name(path: str) -> str:
    """
    Sort all the container files and sort it using its name.

    Sorting is done using the time that is stored in file's name and
    in ascending form.

    This will return the container filename created at last.

    Arguments:
        `path`: path to container files
    
    Returns:
        [path + current container filename]
    """
    objects = os.listdir(path)
    containers = []
    for obj in objects:
        if obj.startswith("container-"):
            _, time = obj.split("-")
            time = float(time)
            containers.append(time)
    containers.sort()
    return os.path.join(path, f"container-{containers[-1]}")


def get_all_containers(path: str) -> list[str]:
    """
    This will return all container files' name in `list` object and it
    only get the filename which starts from `container-`.

    Arguments:
        `path`: path to the container files
    
    Returns:
        list of container filenames
    """
    return list(os.path.join(path, x) for x in os.listdir(path) if x.startswith("container-"))
