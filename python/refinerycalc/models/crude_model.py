# coding: utf-8

"""
    Refinery Calc API Documentation

    Integrate the powerful Refinery Calc Engine into your process using this API.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@refinerycalc.com.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CrudeModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'crude_no': 'int',
        'crude_id': 'int',
        'name': 'str',
        'api': 'float',
        'sulphur': 'float',
        'value': 'float',
        'maximum': 'float',
        'minimum': 'float',
        'price': 'float',
        'freight': 'float',
        'is_available': 'bool',
        'price_date': 'datetime',
        'default_price_date': 'datetime',
        'crude_type': 'CrudeType',
        'allocation': 'CrudeAllocation',
        'display_order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'crude_no': 'crudeNo',
        'crude_id': 'crudeId',
        'name': 'name',
        'api': 'api',
        'sulphur': 'sulphur',
        'value': 'value',
        'maximum': 'maximum',
        'minimum': 'minimum',
        'price': 'price',
        'freight': 'freight',
        'is_available': 'isAvailable',
        'price_date': 'priceDate',
        'default_price_date': 'defaultPriceDate',
        'crude_type': 'crudeType',
        'allocation': 'allocation',
        'display_order': 'displayOrder'
    }

    def __init__(self, id=None, crude_no=None, crude_id=None, name=None, api=None, sulphur=None, value=None, maximum=None, minimum=None, price=None, freight=None, is_available=None, price_date=None, default_price_date=None, crude_type=None, allocation=None, display_order=None):  # noqa: E501
        """CrudeModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._crude_no = None
        self._crude_id = None
        self._name = None
        self._api = None
        self._sulphur = None
        self._value = None
        self._maximum = None
        self._minimum = None
        self._price = None
        self._freight = None
        self._is_available = None
        self._price_date = None
        self._default_price_date = None
        self._crude_type = None
        self._allocation = None
        self._display_order = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if crude_no is not None:
            self.crude_no = crude_no
        if crude_id is not None:
            self.crude_id = crude_id
        if name is not None:
            self.name = name
        if api is not None:
            self.api = api
        if sulphur is not None:
            self.sulphur = sulphur
        if value is not None:
            self.value = value
        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum
        if price is not None:
            self.price = price
        if freight is not None:
            self.freight = freight
        if is_available is not None:
            self.is_available = is_available
        if price_date is not None:
            self.price_date = price_date
        if default_price_date is not None:
            self.default_price_date = default_price_date
        if crude_type is not None:
            self.crude_type = crude_type
        if allocation is not None:
            self.allocation = allocation
        if display_order is not None:
            self.display_order = display_order

    @property
    def id(self):
        """Gets the id of this CrudeModel.  # noqa: E501


        :return: The id of this CrudeModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CrudeModel.


        :param id: The id of this CrudeModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def crude_no(self):
        """Gets the crude_no of this CrudeModel.  # noqa: E501


        :return: The crude_no of this CrudeModel.  # noqa: E501
        :rtype: int
        """
        return self._crude_no

    @crude_no.setter
    def crude_no(self, crude_no):
        """Sets the crude_no of this CrudeModel.


        :param crude_no: The crude_no of this CrudeModel.  # noqa: E501
        :type: int
        """

        self._crude_no = crude_no

    @property
    def crude_id(self):
        """Gets the crude_id of this CrudeModel.  # noqa: E501


        :return: The crude_id of this CrudeModel.  # noqa: E501
        :rtype: int
        """
        return self._crude_id

    @crude_id.setter
    def crude_id(self, crude_id):
        """Sets the crude_id of this CrudeModel.


        :param crude_id: The crude_id of this CrudeModel.  # noqa: E501
        :type: int
        """

        self._crude_id = crude_id

    @property
    def name(self):
        """Gets the name of this CrudeModel.  # noqa: E501


        :return: The name of this CrudeModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CrudeModel.


        :param name: The name of this CrudeModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def api(self):
        """Gets the api of this CrudeModel.  # noqa: E501


        :return: The api of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this CrudeModel.


        :param api: The api of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._api = api

    @property
    def sulphur(self):
        """Gets the sulphur of this CrudeModel.  # noqa: E501


        :return: The sulphur of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._sulphur

    @sulphur.setter
    def sulphur(self, sulphur):
        """Sets the sulphur of this CrudeModel.


        :param sulphur: The sulphur of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._sulphur = sulphur

    @property
    def value(self):
        """Gets the value of this CrudeModel.  # noqa: E501


        :return: The value of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CrudeModel.


        :param value: The value of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def maximum(self):
        """Gets the maximum of this CrudeModel.  # noqa: E501


        :return: The maximum of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this CrudeModel.


        :param maximum: The maximum of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this CrudeModel.  # noqa: E501


        :return: The minimum of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this CrudeModel.


        :param minimum: The minimum of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._minimum = minimum

    @property
    def price(self):
        """Gets the price of this CrudeModel.  # noqa: E501


        :return: The price of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CrudeModel.


        :param price: The price of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def freight(self):
        """Gets the freight of this CrudeModel.  # noqa: E501


        :return: The freight of this CrudeModel.  # noqa: E501
        :rtype: float
        """
        return self._freight

    @freight.setter
    def freight(self, freight):
        """Sets the freight of this CrudeModel.


        :param freight: The freight of this CrudeModel.  # noqa: E501
        :type: float
        """

        self._freight = freight

    @property
    def is_available(self):
        """Gets the is_available of this CrudeModel.  # noqa: E501


        :return: The is_available of this CrudeModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this CrudeModel.


        :param is_available: The is_available of this CrudeModel.  # noqa: E501
        :type: bool
        """

        self._is_available = is_available

    @property
    def price_date(self):
        """Gets the price_date of this CrudeModel.  # noqa: E501


        :return: The price_date of this CrudeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._price_date

    @price_date.setter
    def price_date(self, price_date):
        """Sets the price_date of this CrudeModel.


        :param price_date: The price_date of this CrudeModel.  # noqa: E501
        :type: datetime
        """

        self._price_date = price_date

    @property
    def default_price_date(self):
        """Gets the default_price_date of this CrudeModel.  # noqa: E501


        :return: The default_price_date of this CrudeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._default_price_date

    @default_price_date.setter
    def default_price_date(self, default_price_date):
        """Sets the default_price_date of this CrudeModel.


        :param default_price_date: The default_price_date of this CrudeModel.  # noqa: E501
        :type: datetime
        """

        self._default_price_date = default_price_date

    @property
    def crude_type(self):
        """Gets the crude_type of this CrudeModel.  # noqa: E501


        :return: The crude_type of this CrudeModel.  # noqa: E501
        :rtype: CrudeType
        """
        return self._crude_type

    @crude_type.setter
    def crude_type(self, crude_type):
        """Sets the crude_type of this CrudeModel.


        :param crude_type: The crude_type of this CrudeModel.  # noqa: E501
        :type: CrudeType
        """

        self._crude_type = crude_type

    @property
    def allocation(self):
        """Gets the allocation of this CrudeModel.  # noqa: E501


        :return: The allocation of this CrudeModel.  # noqa: E501
        :rtype: CrudeAllocation
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this CrudeModel.


        :param allocation: The allocation of this CrudeModel.  # noqa: E501
        :type: CrudeAllocation
        """

        self._allocation = allocation

    @property
    def display_order(self):
        """Gets the display_order of this CrudeModel.  # noqa: E501


        :return: The display_order of this CrudeModel.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this CrudeModel.


        :param display_order: The display_order of this CrudeModel.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CrudeModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CrudeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
