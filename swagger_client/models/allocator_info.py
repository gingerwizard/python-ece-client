# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AllocatorInfo(object):
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
        'status': 'AllocatorHealthStatus',
        'allocator_id': 'str',
        'zone_id': 'str',
        'host_ip': 'str',
        'public_hostname': 'str',
        'capacity': 'AllocatorCapacity',
        'settings': 'AllocatorSettings',
        'instances': 'list[AllocatedInstanceStatus]',
        'metadata': 'list[AllocatorMetadataItem]',
        'features': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'allocator_id': 'allocator_id',
        'zone_id': 'zone_id',
        'host_ip': 'host_ip',
        'public_hostname': 'public_hostname',
        'capacity': 'capacity',
        'settings': 'settings',
        'instances': 'instances',
        'metadata': 'metadata',
        'features': 'features'
    }

    def __init__(self, status=None, allocator_id=None, zone_id=None, host_ip=None, public_hostname=None, capacity=None, settings=None, instances=None, metadata=None, features=None):
        """
        AllocatorInfo - a model defined in Swagger
        """

        self._status = None
        self._allocator_id = None
        self._zone_id = None
        self._host_ip = None
        self._public_hostname = None
        self._capacity = None
        self._settings = None
        self._instances = None
        self._metadata = None
        self._features = None

        if status is not None:
          self.status = status
        if allocator_id is not None:
          self.allocator_id = allocator_id
        if zone_id is not None:
          self.zone_id = zone_id
        if host_ip is not None:
          self.host_ip = host_ip
        if public_hostname is not None:
          self.public_hostname = public_hostname
        if capacity is not None:
          self.capacity = capacity
        if settings is not None:
          self.settings = settings
        if instances is not None:
          self.instances = instances
        if metadata is not None:
          self.metadata = metadata
        if features is not None:
          self.features = features

    @property
    def status(self):
        """
        Gets the status of this AllocatorInfo.

        :return: The status of this AllocatorInfo.
        :rtype: AllocatorHealthStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AllocatorInfo.

        :param status: The status of this AllocatorInfo.
        :type: AllocatorHealthStatus
        """

        self._status = status

    @property
    def allocator_id(self):
        """
        Gets the allocator_id of this AllocatorInfo.
        Identifier for this allocator

        :return: The allocator_id of this AllocatorInfo.
        :rtype: str
        """
        return self._allocator_id

    @allocator_id.setter
    def allocator_id(self, allocator_id):
        """
        Sets the allocator_id of this AllocatorInfo.
        Identifier for this allocator

        :param allocator_id: The allocator_id of this AllocatorInfo.
        :type: str
        """

        self._allocator_id = allocator_id

    @property
    def zone_id(self):
        """
        Gets the zone_id of this AllocatorInfo.
        Identifier of the zone

        :return: The zone_id of this AllocatorInfo.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this AllocatorInfo.
        Identifier of the zone

        :param zone_id: The zone_id of this AllocatorInfo.
        :type: str
        """

        self._zone_id = zone_id

    @property
    def host_ip(self):
        """
        Gets the host_ip of this AllocatorInfo.
        Host IP of this allocator

        :return: The host_ip of this AllocatorInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """
        Sets the host_ip of this AllocatorInfo.
        Host IP of this allocator

        :param host_ip: The host_ip of this AllocatorInfo.
        :type: str
        """

        self._host_ip = host_ip

    @property
    def public_hostname(self):
        """
        Gets the public_hostname of this AllocatorInfo.
        Public hostname of this allocator

        :return: The public_hostname of this AllocatorInfo.
        :rtype: str
        """
        return self._public_hostname

    @public_hostname.setter
    def public_hostname(self, public_hostname):
        """
        Sets the public_hostname of this AllocatorInfo.
        Public hostname of this allocator

        :param public_hostname: The public_hostname of this AllocatorInfo.
        :type: str
        """

        self._public_hostname = public_hostname

    @property
    def capacity(self):
        """
        Gets the capacity of this AllocatorInfo.

        :return: The capacity of this AllocatorInfo.
        :rtype: AllocatorCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this AllocatorInfo.

        :param capacity: The capacity of this AllocatorInfo.
        :type: AllocatorCapacity
        """

        self._capacity = capacity

    @property
    def settings(self):
        """
        Gets the settings of this AllocatorInfo.

        :return: The settings of this AllocatorInfo.
        :rtype: AllocatorSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this AllocatorInfo.

        :param settings: The settings of this AllocatorInfo.
        :type: AllocatorSettings
        """

        self._settings = settings

    @property
    def instances(self):
        """
        Gets the instances of this AllocatorInfo.

        :return: The instances of this AllocatorInfo.
        :rtype: list[AllocatedInstanceStatus]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this AllocatorInfo.

        :param instances: The instances of this AllocatorInfo.
        :type: list[AllocatedInstanceStatus]
        """

        self._instances = instances

    @property
    def metadata(self):
        """
        Gets the metadata of this AllocatorInfo.
        Arbitrary metadata associated with this allocator

        :return: The metadata of this AllocatorInfo.
        :rtype: list[AllocatorMetadataItem]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this AllocatorInfo.
        Arbitrary metadata associated with this allocator

        :param metadata: The metadata of this AllocatorInfo.
        :type: list[AllocatorMetadataItem]
        """

        self._metadata = metadata

    @property
    def features(self):
        """
        Gets the features of this AllocatorInfo.
        List of features associated with this allocator. Note this is only present for backwards compatibility purposes and is scheduled for removal in the next major version release.

        :return: The features of this AllocatorInfo.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this AllocatorInfo.
        List of features associated with this allocator. Note this is only present for backwards compatibility purposes and is scheduled for removal in the next major version release.

        :param features: The features of this AllocatorInfo.
        :type: list[str]
        """

        self._features = features

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
        if not isinstance(other, AllocatorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
