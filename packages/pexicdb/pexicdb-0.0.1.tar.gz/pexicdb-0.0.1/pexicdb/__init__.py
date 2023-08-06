"""
    # Pexicdb

    Pexicdb is a simple model based file database, pexicdb is a lightweight and stores
    data in the folders and files, basically a folder is called container.

    There are 2 types of files inside container
    
    1. container file(models stored in this)
    2. data file(contains all data about the container)

    Pexicdb interact with the containers using model which is usually a list of fields.
    ```
    from pexicdb.fields import StringField, UUIDField
    from pexicdb import connect

    user_model = {
        "id": UUIDField("id"),
        "name": StringField("name")
    }

    users = connect("users", list(user_model).values())
    ```

    **NOTE :** The first field of any Model must be either `UUIDField` or an `IntegerField`.
"""

from .__about__ import __name__, __version__, __author__, __author_email__, __license__
from .functions import connect

__all__ = ["connect", ]