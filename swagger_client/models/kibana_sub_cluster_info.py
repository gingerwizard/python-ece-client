# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class KibanaSubClusterInfo(object):
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
        'kibana_id': 'str',
        'enabled': 'bool',
        'links': 'dict(str, Hyperlink)'
    }

    attribute_map = {
        'kibana_id': 'kibana_id',
        'enabled': 'enabled',
        'links': 'links'
    }

    def __init__(self, kibana_id=None, enabled=None, links=None):
        """
        KibanaSubClusterInfo - a model defined in Swagger
        """

        self._kibana_id = None
        self._enabled = None
        self._links = None

        self.kibana_id = kibana_id
        self.enabled = enabled
        if links is not None:
          self.links = links

    @property
    def kibana_id(self):
        """
        Gets the kibana_id of this KibanaSubClusterInfo.
        The Kibana cluster Id

        :return: The kibana_id of this KibanaSubClusterInfo.
        :rtype: str
        """
        return self._kibana_id

    @kibana_id.setter
    def kibana_id(self, kibana_id):
        """
        Sets the kibana_id of this KibanaSubClusterInfo.
        The Kibana cluster Id

        :param kibana_id: The kibana_id of this KibanaSubClusterInfo.
        :type: str
        """
        if kibana_id is None:
            raise ValueError("Invalid value for `kibana_id`, must not be `None`")

        self._kibana_id = kibana_id

    @property
    def enabled(self):
        """
        Gets the enabled of this KibanaSubClusterInfo.
        Whether the associated Kibana cluster is currently available

        :return: The enabled of this KibanaSubClusterInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this KibanaSubClusterInfo.
        Whether the associated Kibana cluster is currently available

        :param enabled: The enabled of this KibanaSubClusterInfo.
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def links(self):
        """
        Gets the links of this KibanaSubClusterInfo.
        A map of application-specific operations (which map to 'operationId's in the Swagger API) to metadata about that operation

        :return: The links of this KibanaSubClusterInfo.
        :rtype: dict(str, Hyperlink)
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this KibanaSubClusterInfo.
        A map of application-specific operations (which map to 'operationId's in the Swagger API) to metadata about that operation

        :param links: The links of this KibanaSubClusterInfo.
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
        if not isinstance(other, KibanaSubClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
