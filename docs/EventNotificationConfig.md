# EventNotificationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubsub_topic_name** | **str** | A Cloud Pub/Sub topic name. For example, &#x60;projects/myProject/topics/deviceEvents&#x60;. | [optional] 
**subfolder_matches** | **str** | If the subfolder name matches this string exactly, this configuration will be used. The string must not include the leading &#39;/&#39; character. If empty, all strings are matched. This field is used only for telemetry events; subfolders are not supported for state changes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


