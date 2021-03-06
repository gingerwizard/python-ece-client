# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestoreSnapshotConfiguration(object):
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
        'repository_name': 'str',
        'snapshot_name': 'str',
        'repository_config': 'RestoreSnapshotRepoConfiguration',
        'restore_payload': 'RestoreSnapshotApiConfiguration'
    }

    attribute_map = {
        'repository_name': 'repository_name',
        'snapshot_name': 'snapshot_name',
        'repository_config': 'repository_config',
        'restore_payload': 'restore_payload'
    }

    def __init__(self, repository_name=None, snapshot_name=None, repository_config=None, restore_payload=None):
        """
        RestoreSnapshotConfiguration - a model defined in Swagger
        """

        self._repository_name = None
        self._snapshot_name = None
        self._repository_config = None
        self._restore_payload = None

        if repository_name is not None:
          self.repository_name = repository_name
        self.snapshot_name = snapshot_name
        if repository_config is not None:
          self.repository_config = repository_config
        if restore_payload is not None:
          self.restore_payload = restore_payload

    @property
    def repository_name(self):
        """
        Gets the repository_name of this RestoreSnapshotConfiguration.
        If specified, contains the name of the snapshot repository - else will default to the Elastic Cloud system repo ('found-snapshots')

        :return: The repository_name of this RestoreSnapshotConfiguration.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """
        Sets the repository_name of this RestoreSnapshotConfiguration.
        If specified, contains the name of the snapshot repository - else will default to the Elastic Cloud system repo ('found-snapshots')

        :param repository_name: The repository_name of this RestoreSnapshotConfiguration.
        :type: str
        """

        self._repository_name = repository_name

    @property
    def snapshot_name(self):
        """
        Gets the snapshot_name of this RestoreSnapshotConfiguration.
        The name of the snapshot to restore. Use '\\_\\_latest_success\\_\\_' to get the most recent snapshot from the specified repository

        :return: The snapshot_name of this RestoreSnapshotConfiguration.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """
        Sets the snapshot_name of this RestoreSnapshotConfiguration.
        The name of the snapshot to restore. Use '\\_\\_latest_success\\_\\_' to get the most recent snapshot from the specified repository

        :param snapshot_name: The snapshot_name of this RestoreSnapshotConfiguration.
        :type: str
        """
        if snapshot_name is None:
            raise ValueError("Invalid value for `snapshot_name`, must not be `None`")

        self._snapshot_name = snapshot_name

    @property
    def repository_config(self):
        """
        Gets the repository_config of this RestoreSnapshotConfiguration.

        :return: The repository_config of this RestoreSnapshotConfiguration.
        :rtype: RestoreSnapshotRepoConfiguration
        """
        return self._repository_config

    @repository_config.setter
    def repository_config(self, repository_config):
        """
        Sets the repository_config of this RestoreSnapshotConfiguration.

        :param repository_config: The repository_config of this RestoreSnapshotConfiguration.
        :type: RestoreSnapshotRepoConfiguration
        """

        self._repository_config = repository_config

    @property
    def restore_payload(self):
        """
        Gets the restore_payload of this RestoreSnapshotConfiguration.

        :return: The restore_payload of this RestoreSnapshotConfiguration.
        :rtype: RestoreSnapshotApiConfiguration
        """
        return self._restore_payload

    @restore_payload.setter
    def restore_payload(self, restore_payload):
        """
        Sets the restore_payload of this RestoreSnapshotConfiguration.

        :param restore_payload: The restore_payload of this RestoreSnapshotConfiguration.
        :type: RestoreSnapshotApiConfiguration
        """

        self._restore_payload = restore_payload

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
        if not isinstance(other, RestoreSnapshotConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
