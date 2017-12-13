# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class KibanaConfiguration(object):
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
        'version': 'str',
        'docker_image': 'str',
        'system_settings': 'KibanaSystemSettings',
        'user_settings_json': 'object',
        'user_settings_yaml': 'str',
        'user_settings_override_json': 'object',
        'user_settings_override_yaml': 'str'
    }

    attribute_map = {
        'version': 'version',
        'docker_image': 'docker_image',
        'system_settings': 'system_settings',
        'user_settings_json': 'user_settings_json',
        'user_settings_yaml': 'user_settings_yaml',
        'user_settings_override_json': 'user_settings_override_json',
        'user_settings_override_yaml': 'user_settings_override_yaml'
    }

    def __init__(self, version=None, docker_image=None, system_settings=None, user_settings_json=None, user_settings_yaml=None, user_settings_override_json=None, user_settings_override_yaml=None):
        """
        KibanaConfiguration - a model defined in Swagger
        """

        self._version = None
        self._docker_image = None
        self._system_settings = None
        self._user_settings_json = None
        self._user_settings_yaml = None
        self._user_settings_override_json = None
        self._user_settings_override_yaml = None

        if version is not None:
          self.version = version
        if docker_image is not None:
          self.docker_image = docker_image
        if system_settings is not None:
          self.system_settings = system_settings
        if user_settings_json is not None:
          self.user_settings_json = user_settings_json
        if user_settings_yaml is not None:
          self.user_settings_yaml = user_settings_yaml
        if user_settings_override_json is not None:
          self.user_settings_override_json = user_settings_override_json
        if user_settings_override_yaml is not None:
          self.user_settings_override_yaml = user_settings_override_yaml

    @property
    def version(self):
        """
        Gets the version of this KibanaConfiguration.
        The version of the Kibana cluster (must be one of the ECE supported versions, and won't work unless it matches the Elasticsearch version. Leave blank to auto-detect version.)

        :return: The version of this KibanaConfiguration.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this KibanaConfiguration.
        The version of the Kibana cluster (must be one of the ECE supported versions, and won't work unless it matches the Elasticsearch version. Leave blank to auto-detect version.)

        :param version: The version of this KibanaConfiguration.
        :type: str
        """

        self._version = version

    @property
    def docker_image(self):
        """
        Gets the docker_image of this KibanaConfiguration.
        A docker URI that allows overriding of the default docker image specified for this version

        :return: The docker_image of this KibanaConfiguration.
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """
        Sets the docker_image of this KibanaConfiguration.
        A docker URI that allows overriding of the default docker image specified for this version

        :param docker_image: The docker_image of this KibanaConfiguration.
        :type: str
        """

        self._docker_image = docker_image

    @property
    def system_settings(self):
        """
        Gets the system_settings of this KibanaConfiguration.

        :return: The system_settings of this KibanaConfiguration.
        :rtype: KibanaSystemSettings
        """
        return self._system_settings

    @system_settings.setter
    def system_settings(self, system_settings):
        """
        Sets the system_settings of this KibanaConfiguration.

        :param system_settings: The system_settings of this KibanaConfiguration.
        :type: KibanaSystemSettings
        """

        self._system_settings = system_settings

    @property
    def user_settings_json(self):
        """
        Gets the user_settings_json of this KibanaConfiguration.
        An arbitrary JSON object allowing (non-admin) cluster owners to set their parameters (only one of this and 'user_settings_yaml' is allowed), provided they are on the whitelist ('user_settings_whitelist') and not on the blacklist ('user_settings_blacklist'). (This field together with 'user_settings_override*' and 'system_settings' defines the total set of Kibana settings)

        :return: The user_settings_json of this KibanaConfiguration.
        :rtype: object
        """
        return self._user_settings_json

    @user_settings_json.setter
    def user_settings_json(self, user_settings_json):
        """
        Sets the user_settings_json of this KibanaConfiguration.
        An arbitrary JSON object allowing (non-admin) cluster owners to set their parameters (only one of this and 'user_settings_yaml' is allowed), provided they are on the whitelist ('user_settings_whitelist') and not on the blacklist ('user_settings_blacklist'). (This field together with 'user_settings_override*' and 'system_settings' defines the total set of Kibana settings)

        :param user_settings_json: The user_settings_json of this KibanaConfiguration.
        :type: object
        """

        self._user_settings_json = user_settings_json

    @property
    def user_settings_yaml(self):
        """
        Gets the user_settings_yaml of this KibanaConfiguration.
        An arbitrary YAML object allowing (non-admin) cluster owners to set their parameters (only one of this and 'user_settings_json' is allowed), provided they are on the whitelist ('user_settings_whitelist') and not on the blacklist ('user_settings_blacklist'). (These field together with 'user_settings_override*' and 'system_settings' defines the total set of Kibana settings)

        :return: The user_settings_yaml of this KibanaConfiguration.
        :rtype: str
        """
        return self._user_settings_yaml

    @user_settings_yaml.setter
    def user_settings_yaml(self, user_settings_yaml):
        """
        Sets the user_settings_yaml of this KibanaConfiguration.
        An arbitrary YAML object allowing (non-admin) cluster owners to set their parameters (only one of this and 'user_settings_json' is allowed), provided they are on the whitelist ('user_settings_whitelist') and not on the blacklist ('user_settings_blacklist'). (These field together with 'user_settings_override*' and 'system_settings' defines the total set of Kibana settings)

        :param user_settings_yaml: The user_settings_yaml of this KibanaConfiguration.
        :type: str
        """

        self._user_settings_yaml = user_settings_yaml

    @property
    def user_settings_override_json(self):
        """
        Gets the user_settings_override_json of this KibanaConfiguration.
        An arbitrary JSON object allowing ECE admins owners to set clusters' parameters (only one of this and 'user_settings_override_yaml' is allowed), ie in addition to the documented 'system_settings'. (This field together with 'system_settings' and 'user_settings*' defines the total set of Kibana settings)

        :return: The user_settings_override_json of this KibanaConfiguration.
        :rtype: object
        """
        return self._user_settings_override_json

    @user_settings_override_json.setter
    def user_settings_override_json(self, user_settings_override_json):
        """
        Sets the user_settings_override_json of this KibanaConfiguration.
        An arbitrary JSON object allowing ECE admins owners to set clusters' parameters (only one of this and 'user_settings_override_yaml' is allowed), ie in addition to the documented 'system_settings'. (This field together with 'system_settings' and 'user_settings*' defines the total set of Kibana settings)

        :param user_settings_override_json: The user_settings_override_json of this KibanaConfiguration.
        :type: object
        """

        self._user_settings_override_json = user_settings_override_json

    @property
    def user_settings_override_yaml(self):
        """
        Gets the user_settings_override_yaml of this KibanaConfiguration.
        An arbitrary YAML object allowing ECE admins owners to set clusters' parameters (only one of this and 'user_settings_override_json' is allowed), ie in addition to the documented 'system_settings'. (This field together with 'system_settings' and 'user_settings*' defines the total set of Kibana settings)

        :return: The user_settings_override_yaml of this KibanaConfiguration.
        :rtype: str
        """
        return self._user_settings_override_yaml

    @user_settings_override_yaml.setter
    def user_settings_override_yaml(self, user_settings_override_yaml):
        """
        Sets the user_settings_override_yaml of this KibanaConfiguration.
        An arbitrary YAML object allowing ECE admins owners to set clusters' parameters (only one of this and 'user_settings_override_json' is allowed), ie in addition to the documented 'system_settings'. (This field together with 'system_settings' and 'user_settings*' defines the total set of Kibana settings)

        :param user_settings_override_yaml: The user_settings_override_yaml of this KibanaConfiguration.
        :type: str
        """

        self._user_settings_override_yaml = user_settings_override_yaml

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
        if not isinstance(other, KibanaConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other