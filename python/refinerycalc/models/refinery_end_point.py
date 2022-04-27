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

class RefineryEndPoint(object):
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
        'refinery_id': 'int',
        'apply_all': 'bool',
        'end_points': 'list[RefineryEndPointItem]'
    }

    attribute_map = {
        'refinery_id': 'refineryId',
        'apply_all': 'applyAll',
        'end_points': 'endPoints'
    }

    def __init__(self, refinery_id=None, apply_all=None, end_points=None):  # noqa: E501
        """RefineryEndPoint - a model defined in Swagger"""  # noqa: E501
        self._refinery_id = None
        self._apply_all = None
        self._end_points = None
        self.discriminator = None
        if refinery_id is not None:
            self.refinery_id = refinery_id
        if apply_all is not None:
            self.apply_all = apply_all
        if end_points is not None:
            self.end_points = end_points

    @property
    def refinery_id(self):
        """Gets the refinery_id of this RefineryEndPoint.  # noqa: E501


        :return: The refinery_id of this RefineryEndPoint.  # noqa: E501
        :rtype: int
        """
        return self._refinery_id

    @refinery_id.setter
    def refinery_id(self, refinery_id):
        """Sets the refinery_id of this RefineryEndPoint.


        :param refinery_id: The refinery_id of this RefineryEndPoint.  # noqa: E501
        :type: int
        """

        self._refinery_id = refinery_id

    @property
    def apply_all(self):
        """Gets the apply_all of this RefineryEndPoint.  # noqa: E501


        :return: The apply_all of this RefineryEndPoint.  # noqa: E501
        :rtype: bool
        """
        return self._apply_all

    @apply_all.setter
    def apply_all(self, apply_all):
        """Sets the apply_all of this RefineryEndPoint.


        :param apply_all: The apply_all of this RefineryEndPoint.  # noqa: E501
        :type: bool
        """

        self._apply_all = apply_all

    @property
    def end_points(self):
        """Gets the end_points of this RefineryEndPoint.  # noqa: E501


        :return: The end_points of this RefineryEndPoint.  # noqa: E501
        :rtype: list[RefineryEndPointItem]
        """
        return self._end_points

    @end_points.setter
    def end_points(self, end_points):
        """Sets the end_points of this RefineryEndPoint.


        :param end_points: The end_points of this RefineryEndPoint.  # noqa: E501
        :type: list[RefineryEndPointItem]
        """

        self._end_points = end_points

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
        if issubclass(RefineryEndPoint, dict):
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
        if not isinstance(other, RefineryEndPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other