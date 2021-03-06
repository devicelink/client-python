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


class Binding(object):
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
        'members': 'list[str]',
        'role': 'str'
    }

    attribute_map = {
        'members': 'members',
        'role': 'role'
    }

    def __init__(self, members=None, role=None):  # noqa: E501
        """Binding - a model defined in OpenAPI"""  # noqa: E501

        self._members = None
        self._role = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if role is not None:
            self.role = role

    @property
    def members(self):
        """Gets the members of this Binding.  # noqa: E501

        Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:  * `allUsers`: A special identifier that represents anyone who is    on the internet; with or without a Google account.  * `allAuthenticatedUsers`: A special identifier that represents anyone    who is authenticated with a Google account or a service account.  * `user:{emailid}`: An email address that represents a specific Google    account. For example, `alice@gmail.com` .   * `serviceAccount:{emailid}`: An email address that represents a service    account. For example, `my-other-app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address that represents a Google group.    For example, `admins@example.com`.   * `domain:{domain}`: A Google Apps domain name that represents all the    users of that domain. For example, `google.com` or `example.com`.    # noqa: E501

        :return: The members of this Binding.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Binding.

        Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:  * `allUsers`: A special identifier that represents anyone who is    on the internet; with or without a Google account.  * `allAuthenticatedUsers`: A special identifier that represents anyone    who is authenticated with a Google account or a service account.  * `user:{emailid}`: An email address that represents a specific Google    account. For example, `alice@gmail.com` .   * `serviceAccount:{emailid}`: An email address that represents a service    account. For example, `my-other-app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address that represents a Google group.    For example, `admins@example.com`.   * `domain:{domain}`: A Google Apps domain name that represents all the    users of that domain. For example, `google.com` or `example.com`.    # noqa: E501

        :param members: The members of this Binding.  # noqa: E501
        :type: list[str]
        """

        self._members = members

    @property
    def role(self):
        """Gets the role of this Binding.  # noqa: E501

        Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. Required  # noqa: E501

        :return: The role of this Binding.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Binding.

        Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. Required  # noqa: E501

        :param role: The role of this Binding.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if not isinstance(other, Binding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
