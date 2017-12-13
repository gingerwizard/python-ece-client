# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RequestEnrollmentTokenReply(object):
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
        'token': 'str',
        'token_id': 'str'
    }

    attribute_map = {
        'token': 'token',
        'token_id': 'token_id'
    }

    def __init__(self, token=None, token_id=None):
        """
        RequestEnrollmentTokenReply - a model defined in Swagger
        """

        self._token = None
        self._token_id = None

        if token is not None:
          self.token = token
        if token_id is not None:
          self.token_id = token_id

    @property
    def token(self):
        """
        Gets the token of this RequestEnrollmentTokenReply.
        The requested token

        :return: The token of this RequestEnrollmentTokenReply.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this RequestEnrollmentTokenReply.
        The requested token

        :param token: The token of this RequestEnrollmentTokenReply.
        :type: str
        """

        self._token = token

    @property
    def token_id(self):
        """
        Gets the token_id of this RequestEnrollmentTokenReply.
        An identifier for the requested token (if persistent) that can be used in listing and deletion

        :return: The token_id of this RequestEnrollmentTokenReply.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """
        Sets the token_id of this RequestEnrollmentTokenReply.
        An identifier for the requested token (if persistent) that can be used in listing and deletion

        :param token_id: The token_id of this RequestEnrollmentTokenReply.
        :type: str
        """

        self._token_id = token_id

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
        if not isinstance(other, RequestEnrollmentTokenReply):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other