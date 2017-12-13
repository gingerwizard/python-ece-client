# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TargetElasticsearchCluster(object):
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
        'elasticsearch_id': 'str',
        'links': 'dict(str, Hyperlink)'
    }

    attribute_map = {
        'elasticsearch_id': 'elasticsearch_id',
        'links': 'links'
    }

    def __init__(self, elasticsearch_id=None, links=None):
        """
        TargetElasticsearchCluster - a model defined in Swagger
        """

        self._elasticsearch_id = None
        self._links = None

        self.elasticsearch_id = elasticsearch_id
        if links is not None:
          self.links = links

    @property
    def elasticsearch_id(self):
        """
        Gets the elasticsearch_id of this TargetElasticsearchCluster.
        The Elasticsearch cluster Id

        :return: The elasticsearch_id of this TargetElasticsearchCluster.
        :rtype: str
        """
        return self._elasticsearch_id

    @elasticsearch_id.setter
    def elasticsearch_id(self, elasticsearch_id):
        """
        Sets the elasticsearch_id of this TargetElasticsearchCluster.
        The Elasticsearch cluster Id

        :param elasticsearch_id: The elasticsearch_id of this TargetElasticsearchCluster.
        :type: str
        """
        if elasticsearch_id is None:
            raise ValueError("Invalid value for `elasticsearch_id`, must not be `None`")

        self._elasticsearch_id = elasticsearch_id

    @property
    def links(self):
        """
        Gets the links of this TargetElasticsearchCluster.
        A map of application-specific operations (which map to 'operationId's in the Swagger API) to metadata about that operation

        :return: The links of this TargetElasticsearchCluster.
        :rtype: dict(str, Hyperlink)
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TargetElasticsearchCluster.
        A map of application-specific operations (which map to 'operationId's in the Swagger API) to metadata about that operation

        :param links: The links of this TargetElasticsearchCluster.
        :type: dict(str, Hyperlink)
        """

        self._links = links

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
        if not isinstance(other, TargetElasticsearchCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other