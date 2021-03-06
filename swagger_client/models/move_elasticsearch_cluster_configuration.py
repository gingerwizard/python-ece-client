# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MoveElasticsearchClusterConfiguration(object):
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
        'cluster_ids': 'list[str]',
        'plan_override': 'TransientElasticsearchPlanConfiguration'
    }

    attribute_map = {
        'cluster_ids': 'cluster_ids',
        'plan_override': 'plan_override'
    }

    def __init__(self, cluster_ids=None, plan_override=None):
        """
        MoveElasticsearchClusterConfiguration - a model defined in Swagger
        """

        self._cluster_ids = None
        self._plan_override = None

        self.cluster_ids = cluster_ids
        if plan_override is not None:
          self.plan_override = plan_override

    @property
    def cluster_ids(self):
        """
        Gets the cluster_ids of this MoveElasticsearchClusterConfiguration.
        Identifiers for the Elasticsearch clusters.

        :return: The cluster_ids of this MoveElasticsearchClusterConfiguration.
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        """
        Sets the cluster_ids of this MoveElasticsearchClusterConfiguration.
        Identifiers for the Elasticsearch clusters.

        :param cluster_ids: The cluster_ids of this MoveElasticsearchClusterConfiguration.
        :type: list[str]
        """
        if cluster_ids is None:
            raise ValueError("Invalid value for `cluster_ids`, must not be `None`")

        self._cluster_ids = cluster_ids

    @property
    def plan_override(self):
        """
        Gets the plan_override of this MoveElasticsearchClusterConfiguration.
        Plan override to apply to the Elasticsearch clusters being moved.

        :return: The plan_override of this MoveElasticsearchClusterConfiguration.
        :rtype: TransientElasticsearchPlanConfiguration
        """
        return self._plan_override

    @plan_override.setter
    def plan_override(self, plan_override):
        """
        Sets the plan_override of this MoveElasticsearchClusterConfiguration.
        Plan override to apply to the Elasticsearch clusters being moved.

        :param plan_override: The plan_override of this MoveElasticsearchClusterConfiguration.
        :type: TransientElasticsearchPlanConfiguration
        """

        self._plan_override = plan_override

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
        if not isinstance(other, MoveElasticsearchClusterConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
