# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestoreSnapshotRepoConfiguration(object):
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
        'raw_settings': 'object'
    }

    attribute_map = {
        'raw_settings': 'raw_settings'
    }

    def __init__(self, raw_settings=None):
        """
        RestoreSnapshotRepoConfiguration - a model defined in Swagger
        """

        self._raw_settings = None

        if raw_settings is not None:
          self.raw_settings = raw_settings

    @property
    def raw_settings(self):
        """
        Gets the raw_settings of this RestoreSnapshotRepoConfiguration.
        The remote snapshot settings raw JSON - see the Elasticsearch '_snapshot' documentation for more details on supported formats

        :return: The raw_settings of this RestoreSnapshotRepoConfiguration.
        :rtype: object
        """
        return self._raw_settings

    @raw_settings.setter
    def raw_settings(self, raw_settings):
        """
        Sets the raw_settings of this RestoreSnapshotRepoConfiguration.
        The remote snapshot settings raw JSON - see the Elasticsearch '_snapshot' documentation for more details on supported formats

        :param raw_settings: The raw_settings of this RestoreSnapshotRepoConfiguration.
        :type: object
        """

        self._raw_settings = raw_settings

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
        if not isinstance(other, RestoreSnapshotRepoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other