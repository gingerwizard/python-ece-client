# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateKibanaInCreateElasticsearchRequest(object):
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
        'cluster_name': 'str',
        'plan': 'KibanaClusterPlan'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'plan': 'plan'
    }

    def __init__(self, cluster_name=None, plan=None):
        """
        CreateKibanaInCreateElasticsearchRequest - a model defined in Swagger
        """

        self._cluster_name = None
        self._plan = None

        if cluster_name is not None:
          self.cluster_name = cluster_name
        self.plan = plan

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this CreateKibanaInCreateElasticsearchRequest.
        The human readable name for the Kibana cluster (default: takes the name of its Elasticsearch cluster)

        :return: The cluster_name of this CreateKibanaInCreateElasticsearchRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this CreateKibanaInCreateElasticsearchRequest.
        The human readable name for the Kibana cluster (default: takes the name of its Elasticsearch cluster)

        :param cluster_name: The cluster_name of this CreateKibanaInCreateElasticsearchRequest.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def plan(self):
        """
        Gets the plan of this CreateKibanaInCreateElasticsearchRequest.

        :return: The plan of this CreateKibanaInCreateElasticsearchRequest.
        :rtype: KibanaClusterPlan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """
        Sets the plan of this CreateKibanaInCreateElasticsearchRequest.

        :param plan: The plan of this CreateKibanaInCreateElasticsearchRequest.
        :type: KibanaClusterPlan
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")

        self._plan = plan

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
        if not isinstance(other, CreateKibanaInCreateElasticsearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other