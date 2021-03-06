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


class ListDevicesResponse(object):
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
        'devices': 'list[Device]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'devices': 'devices',
        'next_page_token': 'nextPageToken'
    }

    def __init__(self, devices=None, next_page_token=None):  # noqa: E501
        """ListDevicesResponse - a model defined in OpenAPI"""  # noqa: E501

        self._devices = None
        self._next_page_token = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def devices(self):
        """Gets the devices of this ListDevicesResponse.  # noqa: E501

        The devices that match the request.  # noqa: E501

        :return: The devices of this ListDevicesResponse.  # noqa: E501
        :rtype: list[Device]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ListDevicesResponse.

        The devices that match the request.  # noqa: E501

        :param devices: The devices of this ListDevicesResponse.  # noqa: E501
        :type: list[Device]
        """

        self._devices = devices

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ListDevicesResponse.  # noqa: E501

        If not empty, indicates that there may be more devices that match the request; this value should be passed in a new `ListDevicesRequest`.  # noqa: E501

        :return: The next_page_token of this ListDevicesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ListDevicesResponse.

        If not empty, indicates that there may be more devices that match the request; this value should be passed in a new `ListDevicesRequest`.  # noqa: E501

        :param next_page_token: The next_page_token of this ListDevicesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if not isinstance(other, ListDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
