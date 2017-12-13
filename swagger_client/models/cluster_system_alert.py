# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClusterSystemAlert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'timestamp': 'datetime',
        'instance_name': 'str',
        'alert_type': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'instance_name': 'instance_name',
        'alert_type': 'alert_type'
    }

    def __init__(self, timestamp=None, instance_name=None, alert_type=None):
        """
        ClusterSystemAlert - a model defined in Swagger
        """

        self._timestamp = None
        self._instance_name = None
        self._alert_type = None

        self.timestamp = timestamp
        self.instance_name = instance_name
        self.alert_type = alert_type

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ClusterSystemAlert.
        Timestamp marking the system alert

        :return: The timestamp of this ClusterSystemAlert.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ClusterSystemAlert.
        Timestamp marking the system alert

        :param timestamp: The timestamp of this ClusterSystemAlert.
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def instance_name(self):
        """
        Gets the instance_name of this ClusterSystemAlert.
        Instance that caused the system alert

        :return: The instance_name of this ClusterSystemAlert.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this ClusterSystemAlert.
        Instance that caused the system alert

        :param instance_name: The instance_name of this ClusterSystemAlert.
        :type: str
        """
        if instance_name is None:
            raise ValueError("Invalid value for `instance_name`, must not be `None`")

        self._instance_name = instance_name

    @property
    def alert_type(self):
        """
        Gets the alert_type of this ClusterSystemAlert.
        Type of system alert

        :return: The alert_type of this ClusterSystemAlert.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this ClusterSystemAlert.
        Type of system alert

        :param alert_type: The alert_type of this ClusterSystemAlert.
        :type: str
        """
        if alert_type is None:
            raise ValueError("Invalid value for `alert_type`, must not be `None`")
        allowed_values = ["automatic_restart", "unknown_event"]
        if alert_type not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_type` ({0}), must be one of {1}"
                .format(alert_type, allowed_values)
            )

        self._alert_type = alert_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClusterSystemAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other