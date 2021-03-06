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


class Status(object):
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
        'code': 'int',
        'details': 'list[dict(str, object)]',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'details': 'details',
        'message': 'message'
    }

    def __init__(self, code=None, details=None, message=None):  # noqa: E501
        """Status - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._details = None
        self._message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this Status.  # noqa: E501

        The status code, which should be an enum value of google.rpc.Code.  # noqa: E501

        :return: The code of this Status.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Status.

        The status code, which should be an enum value of google.rpc.Code.  # noqa: E501

        :param code: The code of this Status.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this Status.  # noqa: E501

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :return: The details of this Status.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Status.

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :param details: The details of this Status.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this Status.  # noqa: E501

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.  # noqa: E501

        :return: The message of this Status.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Status.

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.  # noqa: E501

        :param message: The message of this Status.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
