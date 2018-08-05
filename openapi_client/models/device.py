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


class Device(object):
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
        'blocked': 'bool',
        'config': 'DeviceConfig',
        'credentials': 'list[DeviceCredential]',
        'id': 'str',
        'last_config_ack_time': 'str',
        'last_config_send_time': 'str',
        'last_error_status': 'Status',
        'last_error_time': 'str',
        'last_event_time': 'str',
        'last_heartbeat_time': 'str',
        'last_state_time': 'str',
        'metadata': 'dict(str, str)',
        'name': 'str',
        'num_id': 'str',
        'state': 'DeviceState'
    }

    attribute_map = {
        'blocked': 'blocked',
        'config': 'config',
        'credentials': 'credentials',
        'id': 'id',
        'last_config_ack_time': 'lastConfigAckTime',
        'last_config_send_time': 'lastConfigSendTime',
        'last_error_status': 'lastErrorStatus',
        'last_error_time': 'lastErrorTime',
        'last_event_time': 'lastEventTime',
        'last_heartbeat_time': 'lastHeartbeatTime',
        'last_state_time': 'lastStateTime',
        'metadata': 'metadata',
        'name': 'name',
        'num_id': 'numId',
        'state': 'state'
    }

    def __init__(self, blocked=None, config=None, credentials=None, id=None, last_config_ack_time=None, last_config_send_time=None, last_error_status=None, last_error_time=None, last_event_time=None, last_heartbeat_time=None, last_state_time=None, metadata=None, name=None, num_id=None, state=None):  # noqa: E501
        """Device - a model defined in OpenAPI"""  # noqa: E501

        self._blocked = None
        self._config = None
        self._credentials = None
        self._id = None
        self._last_config_ack_time = None
        self._last_config_send_time = None
        self._last_error_status = None
        self._last_error_time = None
        self._last_event_time = None
        self._last_heartbeat_time = None
        self._last_state_time = None
        self._metadata = None
        self._name = None
        self._num_id = None
        self._state = None
        self.discriminator = None

        if blocked is not None:
            self.blocked = blocked
        if config is not None:
            self.config = config
        if credentials is not None:
            self.credentials = credentials
        if id is not None:
            self.id = id
        if last_config_ack_time is not None:
            self.last_config_ack_time = last_config_ack_time
        if last_config_send_time is not None:
            self.last_config_send_time = last_config_send_time
        if last_error_status is not None:
            self.last_error_status = last_error_status
        if last_error_time is not None:
            self.last_error_time = last_error_time
        if last_event_time is not None:
            self.last_event_time = last_event_time
        if last_heartbeat_time is not None:
            self.last_heartbeat_time = last_heartbeat_time
        if last_state_time is not None:
            self.last_state_time = last_state_time
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if num_id is not None:
            self.num_id = num_id
        if state is not None:
            self.state = state

    @property
    def blocked(self):
        """Gets the blocked of this Device.  # noqa: E501

        If a device is blocked, connections or requests from this device will fail. Can be used to temporarily prevent the device from connecting if, for example, the sensor is generating bad data and needs maintenance.  # noqa: E501

        :return: The blocked of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this Device.

        If a device is blocked, connections or requests from this device will fail. Can be used to temporarily prevent the device from connecting if, for example, the sensor is generating bad data and needs maintenance.  # noqa: E501

        :param blocked: The blocked of this Device.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def config(self):
        """Gets the config of this Device.  # noqa: E501


        :return: The config of this Device.  # noqa: E501
        :rtype: DeviceConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Device.


        :param config: The config of this Device.  # noqa: E501
        :type: DeviceConfig
        """

        self._config = config

    @property
    def credentials(self):
        """Gets the credentials of this Device.  # noqa: E501

        The credentials used to authenticate this device. To allow credential rotation without interruption, multiple device credentials can be bound to this device. No more than 3 credentials can be bound to a single device at a time. When new credentials are added to a device, they are verified against the registry credentials. For details, see the description of the `DeviceRegistry.credentials` field.  # noqa: E501

        :return: The credentials of this Device.  # noqa: E501
        :rtype: list[DeviceCredential]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Device.

        The credentials used to authenticate this device. To allow credential rotation without interruption, multiple device credentials can be bound to this device. No more than 3 credentials can be bound to a single device at a time. When new credentials are added to a device, they are verified against the registry credentials. For details, see the description of the `DeviceRegistry.credentials` field.  # noqa: E501

        :param credentials: The credentials of this Device.  # noqa: E501
        :type: list[DeviceCredential]
        """

        self._credentials = credentials

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501

        The user-defined device identifier. The device ID must be unique within a device registry.  # noqa: E501

        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.

        The user-defined device identifier. The device ID must be unique within a device registry.  # noqa: E501

        :param id: The id of this Device.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_config_ack_time(self):
        """Gets the last_config_ack_time of this Device.  # noqa: E501

        [Output only] The last time a cloud-to-device config version acknowledgment was received from the device. This field is only for configurations sent through MQTT.  # noqa: E501

        :return: The last_config_ack_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_config_ack_time

    @last_config_ack_time.setter
    def last_config_ack_time(self, last_config_ack_time):
        """Sets the last_config_ack_time of this Device.

        [Output only] The last time a cloud-to-device config version acknowledgment was received from the device. This field is only for configurations sent through MQTT.  # noqa: E501

        :param last_config_ack_time: The last_config_ack_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_config_ack_time = last_config_ack_time

    @property
    def last_config_send_time(self):
        """Gets the last_config_send_time of this Device.  # noqa: E501

        [Output only] The last time a cloud-to-device config version was sent to the device.  # noqa: E501

        :return: The last_config_send_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_config_send_time

    @last_config_send_time.setter
    def last_config_send_time(self, last_config_send_time):
        """Sets the last_config_send_time of this Device.

        [Output only] The last time a cloud-to-device config version was sent to the device.  # noqa: E501

        :param last_config_send_time: The last_config_send_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_config_send_time = last_config_send_time

    @property
    def last_error_status(self):
        """Gets the last_error_status of this Device.  # noqa: E501


        :return: The last_error_status of this Device.  # noqa: E501
        :rtype: Status
        """
        return self._last_error_status

    @last_error_status.setter
    def last_error_status(self, last_error_status):
        """Sets the last_error_status of this Device.


        :param last_error_status: The last_error_status of this Device.  # noqa: E501
        :type: Status
        """

        self._last_error_status = last_error_status

    @property
    def last_error_time(self):
        """Gets the last_error_time of this Device.  # noqa: E501

        [Output only] The time the most recent error occurred, such as a failure to publish to Cloud Pub/Sub. This field is the timestamp of 'last_error_status'.  # noqa: E501

        :return: The last_error_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_error_time

    @last_error_time.setter
    def last_error_time(self, last_error_time):
        """Sets the last_error_time of this Device.

        [Output only] The time the most recent error occurred, such as a failure to publish to Cloud Pub/Sub. This field is the timestamp of 'last_error_status'.  # noqa: E501

        :param last_error_time: The last_error_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_error_time = last_error_time

    @property
    def last_event_time(self):
        """Gets the last_event_time of this Device.  # noqa: E501

        [Output only] The last time a telemetry event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :return: The last_event_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this Device.

        [Output only] The last time a telemetry event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :param last_event_time: The last_event_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_event_time = last_event_time

    @property
    def last_heartbeat_time(self):
        """Gets the last_heartbeat_time of this Device.  # noqa: E501

        [Output only] The last time an MQTT `PINGREQ` was received. This field applies only to devices connecting through MQTT. MQTT clients usually only send `PINGREQ` messages if the connection is idle, and no other messages have been sent. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :return: The last_heartbeat_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_heartbeat_time

    @last_heartbeat_time.setter
    def last_heartbeat_time(self, last_heartbeat_time):
        """Sets the last_heartbeat_time of this Device.

        [Output only] The last time an MQTT `PINGREQ` was received. This field applies only to devices connecting through MQTT. MQTT clients usually only send `PINGREQ` messages if the connection is idle, and no other messages have been sent. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :param last_heartbeat_time: The last_heartbeat_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_heartbeat_time = last_heartbeat_time

    @property
    def last_state_time(self):
        """Gets the last_state_time of this Device.  # noqa: E501

        [Output only] The last time a state event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :return: The last_state_time of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_state_time

    @last_state_time.setter
    def last_state_time(self, last_state_time):
        """Sets the last_state_time of this Device.

        [Output only] The last time a state event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.  # noqa: E501

        :param last_state_time: The last_state_time of this Device.  # noqa: E501
        :type: str
        """

        self._last_state_time = last_state_time

    @property
    def metadata(self):
        """Gets the metadata of this Device.  # noqa: E501

        The metadata key-value pairs assigned to the device. This metadata is not interpreted or indexed by Cloud IoT Core. It can be used to add contextual information for the device.  Keys must conform to the regular expression a-zA-Z+ and be less than 128 bytes in length.  Values are free-form strings. Each value must be less than or equal to 32 KB in size.  The total size of all keys and values must be less than 256 KB, and the maximum number of key-value pairs is 500.  # noqa: E501

        :return: The metadata of this Device.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Device.

        The metadata key-value pairs assigned to the device. This metadata is not interpreted or indexed by Cloud IoT Core. It can be used to add contextual information for the device.  Keys must conform to the regular expression a-zA-Z+ and be less than 128 bytes in length.  Values are free-form strings. Each value must be less than or equal to 32 KB in size.  The total size of all keys and values must be less than 256 KB, and the maximum number of key-value pairs is 500.  # noqa: E501

        :param metadata: The metadata of this Device.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501

        The resource path name. For example, `projects/p1/locations/us-central1/registries/registry0/devices/dev0` or `projects/p1/locations/us-central1/registries/registry0/devices/{num_id}`. When `name` is populated as a response from the service, it always ends in the device numeric ID.  # noqa: E501

        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.

        The resource path name. For example, `projects/p1/locations/us-central1/registries/registry0/devices/dev0` or `projects/p1/locations/us-central1/registries/registry0/devices/{num_id}`. When `name` is populated as a response from the service, it always ends in the device numeric ID.  # noqa: E501

        :param name: The name of this Device.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_id(self):
        """Gets the num_id of this Device.  # noqa: E501

        [Output only] A server-defined unique numeric ID for the device. This is a more compact way to identify devices, and it is globally unique.  # noqa: E501

        :return: The num_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._num_id

    @num_id.setter
    def num_id(self, num_id):
        """Sets the num_id of this Device.

        [Output only] A server-defined unique numeric ID for the device. This is a more compact way to identify devices, and it is globally unique.  # noqa: E501

        :param num_id: The num_id of this Device.  # noqa: E501
        :type: str
        """

        self._num_id = num_id

    @property
    def state(self):
        """Gets the state of this Device.  # noqa: E501


        :return: The state of this Device.  # noqa: E501
        :rtype: DeviceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Device.


        :param state: The state of this Device.  # noqa: E501
        :type: DeviceState
        """

        self._state = state

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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
