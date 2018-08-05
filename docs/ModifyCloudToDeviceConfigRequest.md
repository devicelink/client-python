# ModifyCloudToDeviceConfigRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_data** | **str** | The configuration data for the device. | [optional] 
**version_to_update** | **str** | The version number to update. If this value is zero, it will not check the version number of the server and will always update the current version; otherwise, this update will fail if the version number found on the server does not match this version number. This is used to support multiple simultaneous updates without losing data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


