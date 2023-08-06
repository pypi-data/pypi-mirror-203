# Pexicdb [![Downloads](https://pepy.tech/badge/pexicdb)](https://pepy.tech/project/pexicdb)

pexicdb is a simple model based file database, pexicdb is a lightweight and stores
data in the folders and files, basically a folder is called container.

There are 2 types of files inside container

1. container file(models stored in this)
2. data file(contains all data about the container)

pexicdb interact with the containers using model which is usually a list of fields.

## Install

```
$ pip install pexicdb
```

## Simple program

```python
from pexicdb.fields import StringField, UUIDField
from pexicdb import connect

user_model = {
    "id": UUIDField("id"),
    "name": StringField("name")
}

users = connect("users", list(user_model.values()))

users.insert({
    "name" : "Harkishan Khuva"
})
```

**NOTE :** The first field of any Model must be either `UUIDField` or an `IntegerField`.