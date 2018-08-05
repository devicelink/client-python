# coding: utf-8

"""
    Cloud IoT

    Registers and manages IoT (Internet of Things) devices that connect to the Google Cloud Platform.   # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ListDeviceConfigVersionsResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'device_configs': 'list[DeviceConfig]'
    }

    attribute_map = {
        'device_configs': 'deviceConfigs'
    }

    def __init__(self, device_configs=None):  # noqa: E501
        """ListDeviceConfigVersionsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._device_configs = None
        self.discriminator = None

        if device_configs is not None:
            self.device_configs = device_configs

    @property
    def device_configs(self):
        """Gets the device_configs of this ListDeviceConfigVersionsResponse.  # noqa: E501

        The device configuration for the last few versions. Versions are listed in decreasing order, starting from the most recent one.  # noqa: E501

        :return: The device_configs of this ListDeviceConfigVersionsResponse.  # noqa: E501
        :rtype: list[DeviceConfig]
        """
        return self._device_configs

    @device_configs.setter
    def device_configs(self, device_configs):
        """Sets the device_configs of this ListDeviceConfigVersionsResponse.

        The device configuration for the last few versions. Versions are listed in decreasing order, starting from the most recent one.  # noqa: E501

        :param device_configs: The device_configs of this ListDeviceConfigVersionsResponse.  # noqa: E501
        :type: list[DeviceConfig]
        """

        self._device_configs = device_configs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDeviceConfigVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
