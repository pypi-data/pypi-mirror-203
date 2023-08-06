import os
import typing

from .fields import BaseField, UUIDField, IntegerField
from .helpers import decode, encode, create_container, get_all_containers
from .lock import Lock


class PexicdbCursor:
    """
    PexicdbCursor is the main class that handles and provide methods to perform operations.

    Arguments:
        `name`: name of the container

        `model`: list of fields

        `datafile_fp`: file pointer to data file
        
        `container_fp`: file pointer to last created container file
        
        `max_size`: maximum size of the container file in MegaBytes
    """
    def __init__(self, name:str, model:list[BaseField], datafile_fp, container_fp, max_size:int = 256) -> None:
        """
        
        """
        if isinstance(name, str) is not True:
            raise TypeError(
                "name of the container must be type %s"%(str.__name__,)
            )

        if isinstance(model, list) is not True or len(model) < 1:
            raise TypeError(
                "model must be instance of %s and must contains atleast one member"%(list.__name__,)
            )
        
        for field in model:
            if isinstance(field, BaseField) is not True:
                raise TypeError(
                    "model field must be instance of %s"%(BaseField.__name__,)
                )
        
        if isinstance(model[0], (UUIDField, IntegerField)) is not True:
            raise ValueError(
                "first field of any model must be instance of %s or %s, got %s"%(UUIDField.__name__, IntegerField.__name__, type(model[0]).__name__)
            )

        if isinstance(max_size, int) is not True:
            raise TypeError(
                "container's maximum size value must be type of %s"%(int.__name__,)
            )

        if max_size <= 0:
            raise ValueError(
                "container's maximum size value must be greater than zero"
            )

        self._name = name
        """name of the container"""

        self._model = model.copy()
        """copy of the model created by the user"""

        self._datafile_fp = datafile_fp
        """datafile opened file pointer"""

        self._container_fp = container_fp
        """container file pointer(this must of the last container or freshly created)"""

        self._lock = Lock()
        """Lock to maintain queue of the operation"""

        self.max_size = max_size
        """
        Maximum size of the container file in megabytes, this must be less than the runtime memory.

        New container file will be created when a file exceed the maximum filesize.
        """

        self.triggers = {
            "ON_INSERT": lambda model,cursor:None,
            "ON_UPDATE": lambda updated_models,cursor:None,
            "ON_REMOVE": lambda removed_models,cursor:None
        }
        """
        Triggers are used to run a specific function on specific operation, trigger name must be in uppercase

        - `ON_INSERT` : associated function will run after insert operation
        - `ON_UPDATE` : associated function will run after update operation
        - `ON_REMOVE` : associated function will run after remove operation

        ### **TRIGGER** `ON_INSERT`
        Associated function must accept two arguments:

         - `model` : model that is added
         - `cursor` : instance of class
        
        ### **TRIGGER** `ON_UPDATE`
        Associated function must accept two arguments:
         
         - `updated_models` : updated models in `list`
         - `cursor` : instance of class
         
        ### **TRIGGER** `ON_REMOVE`
        Associated function must accept two arguments:
         
         - `removed_models` : removed models in `list`
         - `cursor` : instance of class

         
        ```
        # ON_INSERT Trigger
        import time
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))

        def on_insert_log(model, cursor):
            print("Model is inserted", time.time())

        users.triggers["ON_INSERT"] = on_insert_log

        users.insert({
            "name": "Harkishan Khuva",
            "age": 19
        })

        # Output:
        # Model is inserted 1681646736.9039178
        ```
        """
    

    def exec_trigger(self, name: str, kws:typing.Union[dict, None]=None) -> None:
        """
        Execute the trigger using its name, if the trigger not found or it is not callable at
        that time value will not used as callable and no calls will be made.

        You can also pass the keyword arguments to functions using `kws`.

        `exec_trigger` is mainly for the internal use, but allows you to create your own and
        allows you to execute it.

        ```
        import time
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))
        
        def on_insert(model, cursor):
            users.exec_trigger("MY_TRIGGER", kws={
                "t": time.time()
            })
        
        users.triggers["ON_INSERT"] = on_insert
        users.triggers["MY_TRIGGER"] = lambda t: print("my trigger is called @",t)

        users.insert({
            "name": "Harkishan Khuva",
            "age": 19
        })

        # Output:
        # my trigger is called @ 1681647079.6642978
        ```

        Arguments:
            `name`: name of the trigger

            `kws`: arguments to pass to the trigger function
        """
        trigger_fun = self.triggers.get(name.upper())   # getting trigger function from the class object using name
        # if trigger value found and it is not None and it is callable
        # then call the function with argument kws
        if trigger_fun is not None and callable(trigger_fun) is True:
            if kws is None:
                kws = {}
            return trigger_fun(**kws)


    def insert(self, data: typing.Union[list[BaseField], dict[str, typing.Any]]) -> typing.Union[UUIDField, IntegerField]:
        """
        Insert the model, at the time of insert you can also pass the `dict` object that
        contains the field name as the key in it and the corresponding value to it.

        To insert more than one model use iteration.

        ```
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))

        users.insert({
            "name": "Harkishan Khuva",
            "age": 19
        })
        # or it can be done as follows
        model = user.copy()
        model["name"].data = "Harkishan Khuva"
        model["age"].data = 19
        users.insert(list(model.values()))
        ```

        Arguments:
            `data`: data to be inserted
        
        Returns:
            First field of the model
        """
        # checking for data is instance of list or dict
        if isinstance(data, list) is True:
            # is list it's ok, check the field type and copy it
            for field in data:
                if isinstance(field, BaseField) is not True:
                    raise TypeError(
                        "model field to be inserted must be instance of %s"%(BaseField.__name__,)
                    )
            model = data.copy()

        elif isinstance(data, dict) is True:
            # is dict
            # now add values to model fields using the keys.
            # keys and name of the fields are matched and value is set.
            model = self._model.copy()
            for k,v in data.items(): # type:ignore
                for field in model:
                    if field.name == k:
                        field.data = v
        else:
            # its error time.
            raise TypeError(
                "Insert value argument must be instance of %s or %s, got %s"%(list.__name__, dict.__name__, type(data).__name__)
            )
    
        # checking model
        if len(model) != len(self._model):
            raise ValueError(
                "model length is not equal to the class model length"
            )
        
        # comparing the model and fields' types
        for index, field in enumerate(model):
            if isinstance(field, type(self._model[index])) is not True:
                raise TypeError(
                    "model to insert in the container contains invalid field '%s', it must be '%s'"%(type(field).__name__, type(self._model[index]).__name__)
                )

        with self._lock:
            # iterating fields of the model
            for field in model:
                # assigning default value if exists
                field.auto_assign() # type: ignore
                # validating the field(e.g. checking data type and etc)
                field.validate() # type: ignore
            
            # going at the end of the file
            self._container_fp.seek(0,2)
            # writing the model in base64 format using encode function.
            self._container_fp.write(encode(model))
            
            # truncate the file
            self._container_fp.truncate()

            # checking the size of the current container
            if (os.stat(self._container_fp.name).st_size/1024/1024) >= self.max_size:
                # if container is greater than or equal to the maximum size set
                # then close the container file pointer
                self._container_fp.close()
                # create new container and set to the class member
                self._container_fp = open(create_container(self._name), self._container_fp.mode)
            
            # calling trigger function if exists
            self.exec_trigger("ON_INSERT", {
                "model": model,
                "cursor": self
            })            

            # return the first field of the model
            return model[0] # type: ignore


    def get(self, filter_fields:typing.Union[list, None] = None, limit:int = -1, return_as_dict:bool = False):
        """
        Select or get the models stored in the container.

        Filter fields are nothing but the list of lambda functions or it can be `None` to
        get all models from the container.

        You can also get the values as `dict` object, by setting `return_as_dict` value to `True`

        ```
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))

        # get all stored models
        for c_user in users.get():
            print(c_user)

        # get models has age more than 20
        for c_user in users.get([user["age"].greater_than(20)]):
            print(c_user)

        # get only 2 models and in dictionary object
        for c_user in users.get(limit=2, return_as_dict=True):
            print(c_user)
        ```

        Arguments:
            `filter_fields`: list of lambda functions to filter or None to get all

            `limit`: number of models to be returned, `-1` for no limit

            `return_as_dict`: returns in dict object when set to `True`
        """
        returned_models = 0     # number of returned models
        containers = get_all_containers(self._name)     # all containers name

        # iterating containers
        for container in containers:
            # open the container is bytes read mode
            container_fp = open(container, "rb")    # container file pointer

            # run the loop
            # when the line data is nothing then break
            while True:
                line = container_fp.readline()  # read line from the container
                if not line:
                    # if line is empty or not then break the loop
                    break
                
                # converting the base64 to model
                model = decode(line)
                
                # total booleans returned by the lambda functions
                booleans = []
                
                if filter_fields is None:
                    # if filter_fields value is None
                    # then to evaluate then to return the model
                    # append the True to booleans list
                    booleans.append(True)
                else:
                    # iterating lambda functions
                    for lambda_fun in filter_fields:
                        # iterating model field
                        for field in model:
                            booleans.append(lambda_fun(field))  # comparing and adding return value to the booleans

                # checking for booleans
                # if first booleans list value is True
                # then all function will be used to get if all values in the list are True or not
                if booleans[0] is True and all(booleans) is True:
                    returned_models += 1    # incrementing the returned model

                    if return_as_dict is True:
                        # if the return as dict object is True
                        kv = {} # empty dictionary object
                        # itertating fields
                        for field in model:
                            # settings key value as the field name and the value is
                            # the field
                            kv[field.name] = field
                        yield kv
                    else:
                        yield model

                # checking the limit if set
                if limit > 0 and returned_models >= limit:
                    # if returned models are equal or more than it
                    # then break
                    break
            
            # checking the limit if set
            if limit > 0 and returned_models >= limit:
                # if returned models are equal or more than it
                # then break
                break


    def update(self, filter_fields:typing.Union[list, None], data_to_update:dict) -> list:
        """
        Update the field data of stored model in the container using the `filter_fields`

        You need pass the dictionary(`dict`) object to that contains data to replace with
        using field name as the key.

        ```
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))

        # update the models where name is `Harkishan Khuva` and update it to the `Haki`
        users.update(
            [
                user["name"] == "Harkishan Khuva"
            ],
            {
                "name": "Haki"
            }
        )
        ```

        Arguments:
            `filter_fields`: lambda functions or None to filter out models
            `data_to_update`: data to replace in the model
        
        Returns:
            returns the list of first field of model
        """
        updated_keys = []   # updated models' key will be stored in this object
        containers = get_all_containers(self._name)     # getting all containers

        # iterating containers
        for container in containers:
            models_to_update = {}   # models to be updated from container will be stored in this object
            container_fp = open(container, "rb+")   # container file's file pointer

            index = 0   # using index and at last models are replaced with new models using index in the container
            while True:
                line = container_fp.readline()
                if not line:
                    break
                # getting model from the line
                model = decode(line)

                booleans = []   # booleans will be stored from lambda functions
                if filter_fields is None:
                    # None mean do all
                    # append the True value will make it to do
                    booleans.append(True)
                else:
                    # iterating lambda function and appending it to booleans
                    for lambda_fun in filter_fields:
                        for field in model:
                            booleans.append(lambda_fun(field))

                # if booleans' elements are True or only True value present in the booleans
                if booleans[0] is True and all(booleans) is True:
                    # updating model
                    # using key value of data_to_update argument
                    for k,v in data_to_update.items():
                        for field in model:
                            if field.name == k: # checking field name and update the value
                                field.data = v
                    models_to_update[index] = model # adding model to models_to_update with index number(line_number-1)
                index += 1  # incrment index

            # if models are available in models_to_update object
            if len(models_to_update.keys()) > 0:
                container_fp.seek(0) # file pointer to starting position
                lines = container_fp.readlines()    # reading all lines of container
                
                # iterating updated models
                for index, model in models_to_update.items():
                    lines[index] = encode(model)    # updating model using index of it's in container
                    updated_keys.append(model[0].data)  # append the first field value to the updated_keys
                
                container_fp.seek(0)    # again file pointer at start position
                container_fp.writelines(lines)  # write modified lines
                container_fp.truncate() # truncate the file

            # close the container file pointer
            container_fp.close()

            # execute the trigger
            self.exec_trigger("ON_UPDATE", {
                "updated_models": list(models_to_update.values()),
                "cursor": self
            })

        return updated_keys


    def remove(self, filter_fields:typing.Union[list, None], limit:int = -1) -> list:
        """
        Remove the model from the container using lambda functions or None to remove all.

        You can also pass the number of models to be removed, using `limit` argument.

        ```
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values()))

        users.remove(None) # remove all models

        # remove specific model where the name value is `Harkishan Khuva`
        # and limit is set to 1
        users.remove([
            user["name"] == "Harkishan Khuva"
        ], limit=1)
        ```

        Arguments:
            `filter_fields`: lambda functions or None for all

            `limit`: limit of number of records to remove
        
        Returns:
            List containing removed models
        """
        removed_models = [] # models that are removed

        with self._lock:
            containers = get_all_containers(self._name) # all containers

            # iterating containers
            for container in containers:
                container_fp = open(container, "rb+")   # container file's file pointer
                container_fp.seek(0)

                to_remove_models_index = [] # index of model to be removed from the container
                index = 0   # index for getting index of the line in the container
                while True:
                    line = container_fp.readline()
                    if not line:
                        break
                    model = decode(line)    # original model

                    booleans = []
                    if filter_fields is None:
                        # None mean do all
                        # append the True value will make it to do
                        booleans.append(True)
                    else:
                        # iterating lambda functions
                        for lambda_fun in filter_fields:
                            for field in model:
                                booleans.append(lambda_fun(field))

                    # if booleans have only True values
                    if booleans[0] is True and all(booleans) is True:
                        to_remove_models_index.append(index)    # adding index to remove
                        removed_models.append(model)    # adding model that will be removed

                        # if the limit is set and removed models length is greater than or equal to
                        # then break the loop
                        if limit > 0 and len(removed_models) >= limit:
                            break
                    index += 1  # increment the index value
                
                if len(to_remove_models_index) > 0: # if the length of to_remove_models_index object is more than 0
                    container_fp.seek(0)    # change the position to the starting
                    lines = container_fp.readlines()    # reading all lines

                    # iterating index in the to_remove_models_index in reverse to
                    # avoid the index error
                    for index in reversed(to_remove_models_index):
                        lines.pop(index)    # removing the line(encoded model) using index
                    
                    container_fp.seek(0)    # set the position to the start
                    container_fp.writelines(lines)  # writing modified lines
                    container_fp.truncate() # truncate the file

                # closing the container
                container_fp.close()
                
                # execute trigger
                self.exec_trigger("ON_REMOVE", {
                    "removed_models": removed_models,
                    "cursor": self
                })
                
                # if the limit is set and removed models length is greater than or equal to
                # then break the loop
                if limit > 0 and len(removed_models) >= limit:
                    break

        return removed_models
    

    def count(self, generator:typing.Generator) -> int:
        """
        This will iterate the generator and stops when `StopIteration` exception is raised.
        It will count the number of iterations and returns it.

        ```
        from pexicdb import connect
        from pexicdb.fields import UUIDField, StringField, IntegerField

        # create user model
        user = {
            "id": UUIDField("id"),
            "name": StringField("name"),
            "age": IntegerField("age")
        }

        users = connect("users", list(user.values())) # connect to the container
        print(users.count(users.get())) # prints the number of models
        ```

        Arguments:
            `generator`: any iterable object
        
        Returns:
            Count of iterations
        """
        if isinstance(generator, typing.Generator) is not True:
            raise TypeError(
                "generator argument must be instance of %s, got %s"%(typing.Generator.__name__, type(generator).__name__)
            )

        k = 0   # assigning count to value zero
        
        while True:
            try:
                next(generator) # next to item
            except StopIteration:
                break # break when StopIteration raises
            else:
                k += 1  # increment k by 1

        return k


    def __repr__(self) -> str:
        return f"<PexicdbCursor name='{self._name}' max_size='{self.max_size}MBs'>"