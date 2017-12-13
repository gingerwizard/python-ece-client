# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InstanceMoveRequest(object):
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
        '_from': 'str',
        'to': 'list[str]',
        'instance_down': 'bool'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'instance_down': 'instance_down'
    }

    def __init__(self, _from=None, to=None, instance_down=None):
        """
        InstanceMoveRequest - a model defined in Swagger
        """

        self.__from = None
        self._to = None
        self._instance_down = None

        self._from = _from
        if to is not None:
          self.to = to
        if instance_down is not None:
          self.instance_down = instance_down

    @property
    def _from(self):
        """
        Gets the _from of this InstanceMoveRequest.
        The instance id that is going to be moved

        :return: The _from of this InstanceMoveRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this InstanceMoveRequest.
        The instance id that is going to be moved

        :param _from: The _from of this InstanceMoveRequest.
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def to(self):
        """
        Gets the to of this InstanceMoveRequest.
        An optional list of allocator ids to which the instance should be moved. If not specified then any available allocator can be used (including the current one if it is healthy)

        :return: The to of this InstanceMoveRequest.
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this InstanceMoveRequest.
        An optional list of allocator ids to which the instance should be moved. If not specified then any available allocator can be used (including the current one if it is healthy)

        :param to: The to of this InstanceMoveRequest.
        :type: list[str]
        """

        self._to = to

    @property
    def instance_down(self):
        """
        Gets the instance_down of this InstanceMoveRequest.
        Tells the infrastructure that the instance should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will automatically decide (currently: will treat the instances as up)

        :return: The instance_down of this InstanceMoveRequest.
        :rtype: bool
        """
        return self._instance_down

    @instance_down.setter
    def instance_down(self, instance_down):
        """
        Sets the instance_down of this InstanceMoveRequest.
        Tells the infrastructure that the instance should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will automatically decide (currently: will treat the instances as up)

        :param instance_down: The instance_down of this InstanceMoveRequest.
        :type: bool
        """

        self._instance_down = instance_down

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
        if not isinstance(other, InstanceMoveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other