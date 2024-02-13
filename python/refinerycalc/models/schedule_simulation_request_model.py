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

class ScheduleSimulationRequestModel(object):
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
        'time_zone': 'str',
        'cron_expression': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'time_zone': 'timeZone',
        'cron_expression': 'cronExpression',
        'start_date': 'startDate'
    }

    def __init__(self, time_zone=None, cron_expression=None, start_date='yyyy-MM-dd'):  # noqa: E501
        """ScheduleSimulationRequestModel - a model defined in Swagger"""  # noqa: E501
        self._time_zone = None
        self._cron_expression = None
        self._start_date = None
        self.discriminator = None
        if time_zone is not None:
            self.time_zone = time_zone
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if start_date is not None:
            self.start_date = start_date

    @property
    def time_zone(self):
        """Gets the time_zone of this ScheduleSimulationRequestModel.  # noqa: E501


        :return: The time_zone of this ScheduleSimulationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScheduleSimulationRequestModel.


        :param time_zone: The time_zone of this ScheduleSimulationRequestModel.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def cron_expression(self):
        """Gets the cron_expression of this ScheduleSimulationRequestModel.  # noqa: E501


        :return: The cron_expression of this ScheduleSimulationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this ScheduleSimulationRequestModel.


        :param cron_expression: The cron_expression of this ScheduleSimulationRequestModel.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def start_date(self):
        """Gets the start_date of this ScheduleSimulationRequestModel.  # noqa: E501


        :return: The start_date of this ScheduleSimulationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ScheduleSimulationRequestModel.


        :param start_date: The start_date of this ScheduleSimulationRequestModel.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ScheduleSimulationRequestModel, dict):
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
        if not isinstance(other, ScheduleSimulationRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
