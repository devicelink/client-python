# DeviceConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_data** | **str** | The device configuration data. | [optional] 
**cloud_update_time** | **str** | [Output only] The time at which this configuration version was updated in Cloud IoT Core. This timestamp is set by the server. | [optional] 
**device_ack_time** | **str** | [Output only] The time at which Cloud IoT Core received the acknowledgment from the device, indicating that the device has received this configuration version. If this field is not present, the device has not yet acknowledged that it received this version. Note that when the config was sent to the device, many config versions may have been available in Cloud IoT Core while the device was disconnected, and on connection, only the latest version is sent to the device. Some versions may never be sent to the device, and therefore are never acknowledged. This timestamp is set by Cloud IoT Core. | [optional] 
**version** | **str** | [Output only] The version of this update. The version number is assigned by the server, and is always greater than 0 after device creation. The version must be 0 on the &#x60;CreateDevice&#x60; request if a &#x60;config&#x60; is specified; the response of &#x60;CreateDevice&#x60; will always have a value of 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


