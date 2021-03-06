# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AllocatedInstanceStatus(object):
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
        'cluster_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'instance_name': 'str',
        'node_memory': 'int',
        'healthy': 'bool',
        'cluster_healthy': 'bool'
    }

    attribute_map = {
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'instance_name': 'instance_name',
        'node_memory': 'node_memory',
        'healthy': 'healthy',
        'cluster_healthy': 'cluster_healthy'
    }

    def __init__(self, cluster_type=None, cluster_id=None, cluster_name=None, instance_name=None, node_memory=None, healthy=None, cluster_healthy=None):
        """
        AllocatedInstanceStatus - a model defined in Swagger
        """

        self._cluster_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._instance_name = None
        self._node_memory = None
        self._healthy = None
        self._cluster_healthy = None

        if cluster_type is not None:
          self.cluster_type = cluster_type
        if cluster_id is not None:
          self.cluster_id = cluster_id
        if cluster_name is not None:
          self.cluster_name = cluster_name
        if instance_name is not None:
          self.instance_name = instance_name
        if node_memory is not None:
          self.node_memory = node_memory
        if healthy is not None:
          self.healthy = healthy
        if cluster_healthy is not None:
          self.cluster_healthy = cluster_healthy

    @property
    def cluster_type(self):
        """
        Gets the cluster_type of this AllocatedInstanceStatus.
        Type of instance that is running. E.g. elasticsearch, kibana

        :return: The cluster_type of this AllocatedInstanceStatus.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """
        Sets the cluster_type of this AllocatedInstanceStatus.
        Type of instance that is running. E.g. elasticsearch, kibana

        :param cluster_type: The cluster_type of this AllocatedInstanceStatus.
        :type: str
        """

        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this AllocatedInstanceStatus.
        Identifier for the cluster this instance belongs

        :return: The cluster_id of this AllocatedInstanceStatus.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this AllocatedInstanceStatus.
        Identifier for the cluster this instance belongs

        :param cluster_id: The cluster_id of this AllocatedInstanceStatus.
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this AllocatedInstanceStatus.
        Name of cluster this instance belongs, if available

        :return: The cluster_name of this AllocatedInstanceStatus.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this AllocatedInstanceStatus.
        Name of cluster this instance belongs, if available

        :param cluster_name: The cluster_name of this AllocatedInstanceStatus.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def instance_name(self):
        """
        Gets the instance_name of this AllocatedInstanceStatus.
        Instance ID of the instance

        :return: The instance_name of this AllocatedInstanceStatus.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this AllocatedInstanceStatus.
        Instance ID of the instance

        :param instance_name: The instance_name of this AllocatedInstanceStatus.
        :type: str
        """

        self._instance_name = instance_name

    @property
    def node_memory(self):
        """
        Gets the node_memory of this AllocatedInstanceStatus.
        Memory assigned to this instance

        :return: The node_memory of this AllocatedInstanceStatus.
        :rtype: int
        """
        return self._node_memory

    @node_memory.setter
    def node_memory(self, node_memory):
        """
        Sets the node_memory of this AllocatedInstanceStatus.
        Memory assigned to this instance

        :param node_memory: The node_memory of this AllocatedInstanceStatus.
        :type: int
        """

        self._node_memory = node_memory

    @property
    def healthy(self):
        """
        Gets the healthy of this AllocatedInstanceStatus.
        Indicates whether the instance is healthy

        :return: The healthy of this AllocatedInstanceStatus.
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """
        Sets the healthy of this AllocatedInstanceStatus.
        Indicates whether the instance is healthy

        :param healthy: The healthy of this AllocatedInstanceStatus.
        :type: bool
        """

        self._healthy = healthy

    @property
    def cluster_healthy(self):
        """
        Gets the cluster_healthy of this AllocatedInstanceStatus.
        Indicates whether the cluster the instance belongs to is healthy

        :return: The cluster_healthy of this AllocatedInstanceStatus.
        :rtype: bool
        """
        return self._cluster_healthy

    @cluster_healthy.setter
    def cluster_healthy(self, cluster_healthy):
        """
        Sets the cluster_healthy of this AllocatedInstanceStatus.
        Indicates whether the cluster the instance belongs to is healthy

        :param cluster_healthy: The cluster_healthy of this AllocatedInstanceStatus.
        :type: bool
        """

        self._cluster_healthy = cluster_healthy

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
        if not isinstance(other, AllocatedInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
