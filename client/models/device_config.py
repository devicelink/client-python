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


class DeviceConfig(object):
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
        'binary_data': 'str',
        'cloud_update_time': 'str',
        'device_ack_time': 'str',
        'version': 'str'
    }

    attribute_map = {
        'binary_data': 'binaryData',
        'cloud_update_time': 'cloudUpdateTime',
        'device_ack_time': 'deviceAckTime',
        'version': 'version'
    }

    def __init__(self, binary_data=None, cloud_update_time=None, device_ack_time=None, version=None):  # noqa: E501
        """DeviceConfig - a model defined in OpenAPI"""  # noqa: E501

        self._binary_data = None
        self._cloud_update_time = None
        self._device_ack_time = None
        self._version = None
        self.discriminator = None

        if binary_data is not None:
            self.binary_data = binary_data
        if cloud_update_time is not None:
            self.cloud_update_time = cloud_update_time
        if device_ack_time is not None:
            self.device_ack_time = device_ack_time
        if version is not None:
            self.version = version

    @property
    def binary_data(self):
        """Gets the binary_data of this DeviceConfig.  # noqa: E501

        The device configuration data.  # noqa: E501

        :return: The binary_data of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._binary_data

    @binary_data.setter
    def binary_data(self, binary_data):
        """Sets the binary_data of this DeviceConfig.

        The device configuration data.  # noqa: E501

        :param binary_data: The binary_data of this DeviceConfig.  # noqa: E501
        :type: str
        """
        if binary_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', binary_data):  # noqa: E501
            raise ValueError("Invalid value for `binary_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._binary_data = binary_data

    @property
    def cloud_update_time(self):
        """Gets the cloud_update_time of this DeviceConfig.  # noqa: E501

        [Output only] The time at which this configuration version was updated in Cloud IoT Core. This timestamp is set by the server.  # noqa: E501

        :return: The cloud_update_time of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._cloud_update_time

    @cloud_update_time.setter
    def cloud_update_time(self, cloud_update_time):
        """Sets the cloud_update_time of this DeviceConfig.

        [Output only] The time at which this configuration version was updated in Cloud IoT Core. This timestamp is set by the server.  # noqa: E501

        :param cloud_update_time: The cloud_update_time of this DeviceConfig.  # noqa: E501
        :type: str
        """

        self._cloud_update_time = cloud_update_time

    @property
    def device_ack_time(self):
        """Gets the device_ack_time of this DeviceConfig.  # noqa: E501

        [Output only] The time at which Cloud IoT Core received the acknowledgment from the device, indicating that the device has received this configuration version. If this field is not present, the device has not yet acknowledged that it received this version. Note that when the config was sent to the device, many config versions may have been available in Cloud IoT Core while the device was disconnected, and on connection, only the latest version is sent to the device. Some versions may never be sent to the device, and therefore are never acknowledged. This timestamp is set by Cloud IoT Core.  # noqa: E501

        :return: The device_ack_time of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._device_ack_time

    @device_ack_time.setter
    def device_ack_time(self, device_ack_time):
        """Sets the device_ack_time of this DeviceConfig.

        [Output only] The time at which Cloud IoT Core received the acknowledgment from the device, indicating that the device has received this configuration version. If this field is not present, the device has not yet acknowledged that it received this version. Note that when the config was sent to the device, many config versions may have been available in Cloud IoT Core while the device was disconnected, and on connection, only the latest version is sent to the device. Some versions may never be sent to the device, and therefore are never acknowledged. This timestamp is set by Cloud IoT Core.  # noqa: E501

        :param device_ack_time: The device_ack_time of this DeviceConfig.  # noqa: E501
        :type: str
        """

        self._device_ack_time = device_ack_time

    @property
    def version(self):
        """Gets the version of this DeviceConfig.  # noqa: E501

        [Output only] The version of this update. The version number is assigned by the server, and is always greater than 0 after device creation. The version must be 0 on the `CreateDevice` request if a `config` is specified; the response of `CreateDevice` will always have a value of 1.  # noqa: E501

        :return: The version of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceConfig.

        [Output only] The version of this update. The version number is assigned by the server, and is always greater than 0 after device creation. The version must be 0 on the `CreateDevice` request if a `config` is specified; the response of `CreateDevice` will always have a value of 1.  # noqa: E501

        :param version: The version of this DeviceConfig.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, DeviceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
