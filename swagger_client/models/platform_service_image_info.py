# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PlatformServiceImageInfo(object):
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
        'id': 'str',
        'tag': 'str',
        'version': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tag': 'tag',
        'version': 'version',
        'hash': 'hash'
    }

    def __init__(self, id=None, tag=None, version=None, hash=None):
        """
        PlatformServiceImageInfo - a model defined in Swagger
        """

        self._id = None
        self._tag = None
        self._version = None
        self._hash = None

        if id is not None:
          self.id = id
        if tag is not None:
          self.tag = tag
        if version is not None:
          self.version = version
        if hash is not None:
          self.hash = hash

    @property
    def id(self):
        """
        Gets the id of this PlatformServiceImageInfo.
        Id of runner that hosts the container

        :return: The id of this PlatformServiceImageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PlatformServiceImageInfo.
        Id of runner that hosts the container

        :param id: The id of this PlatformServiceImageInfo.
        :type: str
        """

        self._id = id

    @property
    def tag(self):
        """
        Gets the tag of this PlatformServiceImageInfo.
        Image tag

        :return: The tag of this PlatformServiceImageInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this PlatformServiceImageInfo.
        Image tag

        :param tag: The tag of this PlatformServiceImageInfo.
        :type: str
        """

        self._tag = tag

    @property
    def version(self):
        """
        Gets the version of this PlatformServiceImageInfo.
        Version of service

        :return: The version of this PlatformServiceImageInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PlatformServiceImageInfo.
        Version of service

        :param version: The version of this PlatformServiceImageInfo.
        :type: str
        """

        self._version = version

    @property
    def hash(self):
        """
        Gets the hash of this PlatformServiceImageInfo.
        Image hash code

        :return: The hash of this PlatformServiceImageInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this PlatformServiceImageInfo.
        Image hash code

        :param hash: The hash of this PlatformServiceImageInfo.
        :type: str
        """

        self._hash = hash

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
        if not isinstance(other, PlatformServiceImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other