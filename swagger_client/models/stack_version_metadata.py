# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StackVersionMetadata(object):
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
        'notes': 'str',
        'pre_release': 'bool',
        'min_platform_version': 'str',
        'schema_version': 'int'
    }

    attribute_map = {
        'notes': 'notes',
        'pre_release': 'pre_release',
        'min_platform_version': 'min_platform_version',
        'schema_version': 'schema_version'
    }

    def __init__(self, notes=None, pre_release=None, min_platform_version=None, schema_version=None):
        """
        StackVersionMetadata - a model defined in Swagger
        """

        self._notes = None
        self._pre_release = None
        self._min_platform_version = None
        self._schema_version = None

        if notes is not None:
          self.notes = notes
        if pre_release is not None:
          self.pre_release = pre_release
        if min_platform_version is not None:
          self.min_platform_version = min_platform_version
        if schema_version is not None:
          self.schema_version = schema_version

    @property
    def notes(self):
        """
        Gets the notes of this StackVersionMetadata.
        Notes for administrator

        :return: The notes of this StackVersionMetadata.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this StackVersionMetadata.
        Notes for administrator

        :param notes: The notes of this StackVersionMetadata.
        :type: str
        """

        self._notes = notes

    @property
    def pre_release(self):
        """
        Gets the pre_release of this StackVersionMetadata.
        Indicates that the stack pack version is not GA and is not supposed to be used in production

        :return: The pre_release of this StackVersionMetadata.
        :rtype: bool
        """
        return self._pre_release

    @pre_release.setter
    def pre_release(self, pre_release):
        """
        Sets the pre_release of this StackVersionMetadata.
        Indicates that the stack pack version is not GA and is not supposed to be used in production

        :param pre_release: The pre_release of this StackVersionMetadata.
        :type: bool
        """

        self._pre_release = pre_release

    @property
    def min_platform_version(self):
        """
        Gets the min_platform_version of this StackVersionMetadata.
        The minimum version of the platform that the stack pack version is compatible with

        :return: The min_platform_version of this StackVersionMetadata.
        :rtype: str
        """
        return self._min_platform_version

    @min_platform_version.setter
    def min_platform_version(self, min_platform_version):
        """
        Sets the min_platform_version of this StackVersionMetadata.
        The minimum version of the platform that the stack pack version is compatible with

        :param min_platform_version: The min_platform_version of this StackVersionMetadata.
        :type: str
        """

        self._min_platform_version = min_platform_version

    @property
    def schema_version(self):
        """
        Gets the schema_version of this StackVersionMetadata.
        The schema version of the stack pack version

        :return: The schema_version of this StackVersionMetadata.
        :rtype: int
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """
        Sets the schema_version of this StackVersionMetadata.
        The schema version of the stack pack version

        :param schema_version: The schema_version of this StackVersionMetadata.
        :type: int
        """

        self._schema_version = schema_version

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
        if not isinstance(other, StackVersionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
