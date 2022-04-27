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

class AddRefineriesToSimulationRequest(object):
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
        'refinery_ids': 'list[int]',
        'is_time_series': 'bool',
        'data_source': 'DataSource'
    }

    attribute_map = {
        'refinery_ids': 'refineryIds',
        'is_time_series': 'isTimeSeries',
        'data_source': 'dataSource'
    }

    def __init__(self, refinery_ids=None, is_time_series=None, data_source=None):  # noqa: E501
        """AddRefineriesToSimulationRequest - a model defined in Swagger"""  # noqa: E501
        self._refinery_ids = None
        self._is_time_series = None
        self._data_source = None
        self.discriminator = None
        self.refinery_ids = refinery_ids
        if is_time_series is not None:
            self.is_time_series = is_time_series
        if data_source is not None:
            self.data_source = data_source

    @property
    def refinery_ids(self):
        """Gets the refinery_ids of this AddRefineriesToSimulationRequest.  # noqa: E501


        :return: The refinery_ids of this AddRefineriesToSimulationRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._refinery_ids

    @refinery_ids.setter
    def refinery_ids(self, refinery_ids):
        """Sets the refinery_ids of this AddRefineriesToSimulationRequest.


        :param refinery_ids: The refinery_ids of this AddRefineriesToSimulationRequest.  # noqa: E501
        :type: list[int]
        """
        if refinery_ids is None:
            raise ValueError("Invalid value for `refinery_ids`, must not be `None`")  # noqa: E501

        self._refinery_ids = refinery_ids

    @property
    def is_time_series(self):
        """Gets the is_time_series of this AddRefineriesToSimulationRequest.  # noqa: E501


        :return: The is_time_series of this AddRefineriesToSimulationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_time_series

    @is_time_series.setter
    def is_time_series(self, is_time_series):
        """Sets the is_time_series of this AddRefineriesToSimulationRequest.


        :param is_time_series: The is_time_series of this AddRefineriesToSimulationRequest.  # noqa: E501
        :type: bool
        """

        self._is_time_series = is_time_series

    @property
    def data_source(self):
        """Gets the data_source of this AddRefineriesToSimulationRequest.  # noqa: E501


        :return: The data_source of this AddRefineriesToSimulationRequest.  # noqa: E501
        :rtype: DataSource
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this AddRefineriesToSimulationRequest.


        :param data_source: The data_source of this AddRefineriesToSimulationRequest.  # noqa: E501
        :type: DataSource
        """

        self._data_source = data_source

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
        if issubclass(AddRefineriesToSimulationRequest, dict):
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
        if not isinstance(other, AddRefineriesToSimulationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
