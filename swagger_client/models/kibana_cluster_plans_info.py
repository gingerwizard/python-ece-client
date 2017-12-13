# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class KibanaClusterPlansInfo(object):
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
        'healthy': 'bool',
        'current': 'KibanaClusterPlanInfo',
        'pending': 'KibanaClusterPlanInfo',
        'history': 'list[KibanaClusterPlanInfo]'
    }

    attribute_map = {
        'healthy': 'healthy',
        'current': 'current',
        'pending': 'pending',
        'history': 'history'
    }

    def __init__(self, healthy=None, current=None, pending=None, history=None):
        """
        KibanaClusterPlansInfo - a model defined in Swagger
        """

        self._healthy = None
        self._current = None
        self._pending = None
        self._history = None

        self.healthy = healthy
        if current is not None:
          self.current = current
        if pending is not None:
          self.pending = pending
        self.history = history

    @property
    def healthy(self):
        """
        Gets the healthy of this KibanaClusterPlansInfo.
        Whether the plan situation is healthy (if unhealthy, means the last plan attempt failed)

        :return: The healthy of this KibanaClusterPlansInfo.
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """
        Sets the healthy of this KibanaClusterPlansInfo.
        Whether the plan situation is healthy (if unhealthy, means the last plan attempt failed)

        :param healthy: The healthy of this KibanaClusterPlansInfo.
        :type: bool
        """
        if healthy is None:
            raise ValueError("Invalid value for `healthy`, must not be `None`")

        self._healthy = healthy

    @property
    def current(self):
        """
        Gets the current of this KibanaClusterPlansInfo.

        :return: The current of this KibanaClusterPlansInfo.
        :rtype: KibanaClusterPlanInfo
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this KibanaClusterPlansInfo.

        :param current: The current of this KibanaClusterPlansInfo.
        :type: KibanaClusterPlanInfo
        """

        self._current = current

    @property
    def pending(self):
        """
        Gets the pending of this KibanaClusterPlansInfo.

        :return: The pending of this KibanaClusterPlansInfo.
        :rtype: KibanaClusterPlanInfo
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """
        Sets the pending of this KibanaClusterPlansInfo.

        :param pending: The pending of this KibanaClusterPlansInfo.
        :type: KibanaClusterPlanInfo
        """

        self._pending = pending

    @property
    def history(self):
        """
        Gets the history of this KibanaClusterPlansInfo.

        :return: The history of this KibanaClusterPlansInfo.
        :rtype: list[KibanaClusterPlanInfo]
        """
        return self._history

    @history.setter
    def history(self, history):
        """
        Sets the history of this KibanaClusterPlansInfo.

        :param history: The history of this KibanaClusterPlansInfo.
        :type: list[KibanaClusterPlanInfo]
        """
        if history is None:
            raise ValueError("Invalid value for `history`, must not be `None`")

        self._history = history

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
        if not isinstance(other, KibanaClusterPlansInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other