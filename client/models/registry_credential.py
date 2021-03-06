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


class RegistryCredential(object):
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
        'public_key_certificate': 'PublicKeyCertificate'
    }

    attribute_map = {
        'public_key_certificate': 'publicKeyCertificate'
    }

    def __init__(self, public_key_certificate=None):  # noqa: E501
        """RegistryCredential - a model defined in OpenAPI"""  # noqa: E501

        self._public_key_certificate = None
        self.discriminator = None

        if public_key_certificate is not None:
            self.public_key_certificate = public_key_certificate

    @property
    def public_key_certificate(self):
        """Gets the public_key_certificate of this RegistryCredential.  # noqa: E501


        :return: The public_key_certificate of this RegistryCredential.  # noqa: E501
        :rtype: PublicKeyCertificate
        """
        return self._public_key_certificate

    @public_key_certificate.setter
    def public_key_certificate(self, public_key_certificate):
        """Sets the public_key_certificate of this RegistryCredential.


        :param public_key_certificate: The public_key_certificate of this RegistryCredential.  # noqa: E501
        :type: PublicKeyCertificate
        """

        self._public_key_certificate = public_key_certificate

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
        if not isinstance(other, RegistryCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
