# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchRequest(object):
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
        '_from': 'int',
        'size': 'int',
        'query': 'QueryContainer',
        'sort': 'list[str]'
    }

    attribute_map = {
        '_from': 'from',
        'size': 'size',
        'query': 'query',
        'sort': 'sort'
    }

    def __init__(self, _from=None, size=None, query=None, sort=None):
        """
        SearchRequest - a model defined in Swagger
        """

        self.__from = None
        self._size = None
        self._query = None
        self._sort = None

        if _from is not None:
          self._from = _from
        if size is not None:
          self.size = size
        if query is not None:
          self.query = query
        if sort is not None:
          self.sort = sort

    @property
    def _from(self):
        """
        Gets the _from of this SearchRequest.

        :return: The _from of this SearchRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this SearchRequest.

        :param _from: The _from of this SearchRequest.
        :type: int
        """

        self.__from = _from

    @property
    def size(self):
        """
        Gets the size of this SearchRequest.
        The maximum number of search results to return.

        :return: The size of this SearchRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SearchRequest.
        The maximum number of search results to return.

        :param size: The size of this SearchRequest.
        :type: int
        """

        self._size = size

    @property
    def query(self):
        """
        Gets the query of this SearchRequest.

        :return: The query of this SearchRequest.
        :rtype: QueryContainer
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchRequest.

        :param query: The query of this SearchRequest.
        :type: QueryContainer
        """

        self._query = query

    @property
    def sort(self):
        """
        Gets the sort of this SearchRequest.
        An array of fields to sort the search results by.

        :return: The sort of this SearchRequest.
        :rtype: list[str]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this SearchRequest.
        An array of fields to sort the search results by.

        :param sort: The sort of this SearchRequest.
        :type: list[str]
        """

        self._sort = sort

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
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
