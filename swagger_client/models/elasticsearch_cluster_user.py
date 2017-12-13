# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ElasticsearchClusterUser(object):
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
        'username': 'str',
        'password_hash': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password_hash': 'password_hash'
    }

    def __init__(self, username=None, password_hash=None):
        """
        ElasticsearchClusterUser - a model defined in Swagger
        """

        self._username = None
        self._password_hash = None

        self.username = username
        self.password_hash = password_hash

    @property
    def username(self):
        """
        Gets the username of this ElasticsearchClusterUser.
        The username

        :return: The username of this ElasticsearchClusterUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ElasticsearchClusterUser.
        The username

        :param username: The username of this ElasticsearchClusterUser.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def password_hash(self):
        """
        Gets the password_hash of this ElasticsearchClusterUser.
        The hashed password

        :return: The password_hash of this ElasticsearchClusterUser.
        :rtype: str
        """
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password_hash):
        """
        Sets the password_hash of this ElasticsearchClusterUser.
        The hashed password

        :param password_hash: The password_hash of this ElasticsearchClusterUser.
        :type: str
        """
        if password_hash is None:
            raise ValueError("Invalid value for `password_hash`, must not be `None`")

        self._password_hash = password_hash

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
        if not isinstance(other, ElasticsearchClusterUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
