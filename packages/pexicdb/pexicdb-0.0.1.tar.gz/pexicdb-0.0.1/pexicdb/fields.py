import uuid


class BaseField:
    """
    This is base class for the all fields to use as model's field.

    This class contains all methods and member variable to provide basic functionality,
    and can be implemented as user wants and can customize easily.
    """
    FIELD_TYPE = "BaseField"
    """Basically it should be same as class name but can be any and this is used to identify the field type."""

    def __init__(self, name: str, default=None, nullable=True) -> None:
        """
        Arguments:
            `name`: name of the field

            `default`: any default value to assign if the current data is None

            `nullable`: this field can be nullable or not
        """
        self.__name = name
        self.__data = None
        self.__default = default
        self.__nullable = nullable


    @property
    def name(self):
        """
        name of the current field
        """
        return self.__name

    @property
    def default(self):
        """
        default value of the current field
        """
        return self.__default

    @property
    def nullable(self):
        """
        This field can be nullable or not
        """
        return self.__nullable

    @property
    def data(self):
        """
        Returns set data to the field
        """
        return self.__data

    @data.setter
    def data(self, __o):
        self.__data = __o


    def validate(self):
        """
        Validates the current field using it's data and properties.

        Here field can be nullable, default, etc operations are performed and
        can be customized by performing inheritance.

        Here no return is performed but errors can be raised if anything
        happens wrong.
        """
        if not self.name:
            raise RuntimeError(
                "name is removed or is unset."
            )
    
        if self.nullable is False and self.data is None and self.default is None:
            # this field cannot be NULLABLE and data, default value is also None
            raise ValueError(
                "value cannot be null as it is set to False for `%s`"%(self.name)
            )
    
    def auto_assign(self):
        """
        Assigns the `default` property value to the `data` property.
        """
        if self.data is None and self.default is not None:
            self.data = self.default
    
    
    def __repr__(self) -> str:
        return f"<{self.FIELD_TYPE}:{self.name}='{self.data}'>"
    
    def equals(self, __o):
        """
        returns lambda function containing equals to the object operation

        ```
        users = connect("users", list(user.values()))

        user["name"].equals("Harkishan Khuva")
        # you can also use `==` operator
        user["name"] == "Harkishan Khuva"
        ```
        """
        return lambda field: field.data == __o if field.name == self.name else True
    def __eq__(self, __o):
        return lambda field: field.data == __o if field.name == self.name else True

    def not_equals(self, __o):
        """
        returns lambda function containing not equals to the object operation

        ```
        users = connect("users", list(user.values()))

        user["name"].not_equals("Harkishan Khuva")
        # you can also use `!=` operator
        user["name"] != "Harkishan Khuva"
        ```
        """
        return lambda field: field.data != __o if field.name == self.name else True
    def __ne__(self, __o):
        return lambda field: field.data != __o if field.name == self.name else True

    def less_than(self, __o):
        """
        returns lambda function containing less than to the object operation

        ```
        users = connect("users", list(user.values()))

        user["age"].less_than(18)
        # you can also use `<` operator
        user["age"] < 18
        ```
        """
        return lambda field: field.data < __o if field.name == self.name else True
    def __lt__(self, __o):
        return lambda field: field.data < __o if field.name == self.name else True


    def less_than_equal(self, __o):
        """
        returns lambda function containing less than or equal to the object operation

        ```
        users = connect("users", list(user.values()))

        user["age"].less_than_equal(18)
        # you can also use `<=` operator
        user["age"] <= 18
        ```
        """
        return lambda field: field.data <= __o if field.name == self.name else True
    def __le__(self, __o):
        return lambda field: field.data <= __o if field.name == self.name else True


    def greater_than(self, __o):
        """
        returns lambda function containing greater than to the object operation

        ```
        users = connect("users", list(user.values()))

        user["age"].greater_than(18)
        # you can also use `>` operator
        user["age"] > 18
        ```
        """
        return lambda field: field.data > __o if field.name == self.name else True
    def __gt__(self, __o):
        return lambda field: field.data > __o if field.name == self.name else True


    def greater_than_equal(self, __o):
        """
        returns lambda function containing greater than or equal to the object operation

        ```
        users = connect("users", list(user.values()))

        user["age"].greater_than_equal(18)
        # you can also use `>=` operator
        user["age"] >= 18
        ```
        """
        return lambda field: field.data >= __o if field.name == self.name else True
    def __ge__(self, __o):
        return lambda field: field.data >= __o if field.name == self.name else True

    def custom_filter(self, callable_object):
        """
        Use this when you have to perform unique operations, this must be
        a function or callable and returns boolean.

        Example
        ```
        def unique_operation(field):
            # this function will return the boolean value that
            # field data is None or field data(currently it's a StringField)
            # has length more than zero.
            return field.data is None or len(field.data) > 0
        ```

        Arguments:
            `callable_object`: any callable object
        """
        return lambda field: callable_object(field.data) if field.name == self.name else True


class StringField(BaseField):
    """
    Use this field class for String, this allow only string as values.
    """
    FIELD_TYPE = "StringField"

    @BaseField.data.setter
    def data(self, __o: str):
        if __o is not None and isinstance(__o, str) is not True:
            raise ValueError(
                "data to set must be instance of %s"%(str)
            )
        BaseField.data.fset(self, __o)

class IntegerField(BaseField):
    """
    Use this field class for Integers, this allow only integers as values.
    """
    FIELD_TYPE = "IntegerField"

    @BaseField.data.setter
    def data(self, __o: int):
        if __o is not None and isinstance(__o, int) is not True:
            raise ValueError(
                "data to set must be instance of %s"%(int)
            )
        BaseField.data.fset(self, __o)


class FloatField(BaseField):
    """
    Use this field class for Float values, this allow only float type values.
    """
    FIELD_TYPE = "FloatField"

    @BaseField.data.setter
    def data(self, __o: float):
        if __o is not None and isinstance(__o, float) is not True:
            raise ValueError(
                "data to set must be instance of %s"%(float)
            )
        BaseField.data.fset(self, __o)


class BytesField(BaseField):
    """
    Use this field class for Bytes, this allow only bytes as values.
    """
    FIELD_TYPE = "BytesField"

    @BaseField.data.setter
    def data(self, __o: bytes):
        if __o is not None and isinstance(__o, bytes) is not True:
            raise ValueError(
                "data to set must be instance of %s"%(bytes)
            )
        BaseField.data.fset(self, __o)


class UUIDField(BaseField):
    """
    Use this field class for UUID data, this allow only UUID type data as values.
    """
    FIELD_TYPE = "UUIDField"
    
    def __init__(self, name: str, *args, auto_assign_function=uuid.uuid4, **kws) -> None:
        """
        Arguments:
            `name`: name of the field

            `default`: any default value to assign if the current data is None

            `nullable`: this field can be nullable or not

            `auto_assign_function`: any auto assign callable that returns UUID type value
        """
        super().__init__(name, *args, **kws)
        self.auto_assign_function = auto_assign_function


    def auto_assign(self):
        super().auto_assign()
        if self.data is None:
            self.data = self.auto_assign_function()


    @BaseField.data.setter
    def data(self, __o: uuid.UUID):
        if __o is not None and isinstance(__o, uuid.UUID) is not True:
            raise ValueError(
                "data to set must be instance of %s"%(uuid.UUID)
            )
        BaseField.data.fset(self, __o)