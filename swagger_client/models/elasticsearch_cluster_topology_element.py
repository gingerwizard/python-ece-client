# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ElasticsearchClusterTopologyElement(object):
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
        'node_type': 'ElasticsearchNodeType',
        'memory_per_node': 'int',
        'node_count_per_zone': 'int',
        'zone_count': 'int',
        'elasticsearch': 'ElasticsearchConfiguration',
        'allocator_filter': 'object',
        'node_configuration': 'str'
    }

    attribute_map = {
        'node_type': 'node_type',
        'memory_per_node': 'memory_per_node',
        'node_count_per_zone': 'node_count_per_zone',
        'zone_count': 'zone_count',
        'elasticsearch': 'elasticsearch',
        'allocator_filter': 'allocator_filter',
        'node_configuration': 'node_configuration'
    }

    def __init__(self, node_type=None, memory_per_node=None, node_count_per_zone=None, zone_count=None, elasticsearch=None, allocator_filter=None, node_configuration=None):
        """
        ElasticsearchClusterTopologyElement - a model defined in Swagger
        """

        self._node_type = None
        self._memory_per_node = None
        self._node_count_per_zone = None
        self._zone_count = None
        self._elasticsearch = None
        self._allocator_filter = None
        self._node_configuration = None

        if node_type is not None:
          self.node_type = node_type
        self.memory_per_node = memory_per_node
        self.node_count_per_zone = node_count_per_zone
        if zone_count is not None:
          self.zone_count = zone_count
        if elasticsearch is not None:
          self.elasticsearch = elasticsearch
        if allocator_filter is not None:
          self.allocator_filter = allocator_filter
        if node_configuration is not None:
          self.node_configuration = node_configuration

    @property
    def node_type(self):
        """
        Gets the node_type of this ElasticsearchClusterTopologyElement.

        :return: The node_type of this ElasticsearchClusterTopologyElement.
        :rtype: ElasticsearchNodeType
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this ElasticsearchClusterTopologyElement.

        :param node_type: The node_type of this ElasticsearchClusterTopologyElement.
        :type: ElasticsearchNodeType
        """

        self._node_type = node_type

    @property
    def memory_per_node(self):
        """
        Gets the memory_per_node of this ElasticsearchClusterTopologyElement.
        The memory capacity in MB for each node of this type built in each zone. NOTES: (Only powers of 2 starting with 1024 are supported. Will fail to allocate if too much memory is requested - use 'node_count_per_zone' in that case to split the cluster up within a zone)

        :return: The memory_per_node of this ElasticsearchClusterTopologyElement.
        :rtype: int
        """
        return self._memory_per_node

    @memory_per_node.setter
    def memory_per_node(self, memory_per_node):
        """
        Sets the memory_per_node of this ElasticsearchClusterTopologyElement.
        The memory capacity in MB for each node of this type built in each zone. NOTES: (Only powers of 2 starting with 1024 are supported. Will fail to allocate if too much memory is requested - use 'node_count_per_zone' in that case to split the cluster up within a zone)

        :param memory_per_node: The memory_per_node of this ElasticsearchClusterTopologyElement.
        :type: int
        """
        if memory_per_node is None:
            raise ValueError("Invalid value for `memory_per_node`, must not be `None`")

        self._memory_per_node = memory_per_node

    @property
    def node_count_per_zone(self):
        """
        Gets the node_count_per_zone of this ElasticsearchClusterTopologyElement.
        The number of nodes of this type that are allocated within each zone. NOTES: (ie total capacity per zone = 'node_count_per_zone' * 'memory_per_node' in MB). Cannot be set for tiebreaker topologies. For dedicated master nodes, must be 1 if an entry exists

        :return: The node_count_per_zone of this ElasticsearchClusterTopologyElement.
        :rtype: int
        """
        return self._node_count_per_zone

    @node_count_per_zone.setter
    def node_count_per_zone(self, node_count_per_zone):
        """
        Sets the node_count_per_zone of this ElasticsearchClusterTopologyElement.
        The number of nodes of this type that are allocated within each zone. NOTES: (ie total capacity per zone = 'node_count_per_zone' * 'memory_per_node' in MB). Cannot be set for tiebreaker topologies. For dedicated master nodes, must be 1 if an entry exists

        :param node_count_per_zone: The node_count_per_zone of this ElasticsearchClusterTopologyElement.
        :type: int
        """
        if node_count_per_zone is None:
            raise ValueError("Invalid value for `node_count_per_zone`, must not be `None`")

        self._node_count_per_zone = node_count_per_zone

    @property
    def zone_count(self):
        """
        Gets the zone_count of this ElasticsearchClusterTopologyElement.
        The default number of zones in which data nodes will be placed

        :return: The zone_count of this ElasticsearchClusterTopologyElement.
        :rtype: int
        """
        return self._zone_count

    @zone_count.setter
    def zone_count(self, zone_count):
        """
        Sets the zone_count of this ElasticsearchClusterTopologyElement.
        The default number of zones in which data nodes will be placed

        :param zone_count: The zone_count of this ElasticsearchClusterTopologyElement.
        :type: int
        """

        self._zone_count = zone_count

    @property
    def elasticsearch(self):
        """
        Gets the elasticsearch of this ElasticsearchClusterTopologyElement.

        :return: The elasticsearch of this ElasticsearchClusterTopologyElement.
        :rtype: ElasticsearchConfiguration
        """
        return self._elasticsearch

    @elasticsearch.setter
    def elasticsearch(self, elasticsearch):
        """
        Sets the elasticsearch of this ElasticsearchClusterTopologyElement.

        :param elasticsearch: The elasticsearch of this ElasticsearchClusterTopologyElement.
        :type: ElasticsearchConfiguration
        """

        self._elasticsearch = elasticsearch

    @property
    def allocator_filter(self):
        """
        Gets the allocator_filter of this ElasticsearchClusterTopologyElement.
        DEPRECATED: Controls the allocation strategy of this node type using a simplified version of the Elasticsearch filter DSL (together with 'node_configuration')

        :return: The allocator_filter of this ElasticsearchClusterTopologyElement.
        :rtype: object
        """
        return self._allocator_filter

    @allocator_filter.setter
    def allocator_filter(self, allocator_filter):
        """
        Sets the allocator_filter of this ElasticsearchClusterTopologyElement.
        DEPRECATED: Controls the allocation strategy of this node type using a simplified version of the Elasticsearch filter DSL (together with 'node_configuration')

        :param allocator_filter: The allocator_filter of this ElasticsearchClusterTopologyElement.
        :type: object
        """

        self._allocator_filter = allocator_filter

    @property
    def node_configuration(self):
        """
        Gets the node_configuration of this ElasticsearchClusterTopologyElement.
        Controls the allocation strategy of this node type by pointing to the names of pre-registered allocator settings. Unless otherwise specified for this deployment, only 'default' is supported (equivalent to omitting).

        :return: The node_configuration of this ElasticsearchClusterTopologyElement.
        :rtype: str
        """
        return self._node_configuration

    @node_configuration.setter
    def node_configuration(self, node_configuration):
        """
        Sets the node_configuration of this ElasticsearchClusterTopologyElement.
        Controls the allocation strategy of this node type by pointing to the names of pre-registered allocator settings. Unless otherwise specified for this deployment, only 'default' is supported (equivalent to omitting).

        :param node_configuration: The node_configuration of this ElasticsearchClusterTopologyElement.
        :type: str
        """

        self._node_configuration = node_configuration

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
        if not isinstance(other, ElasticsearchClusterTopologyElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
