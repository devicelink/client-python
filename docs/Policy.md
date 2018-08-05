# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | [**list[Binding]**](Binding.md) | Associates a list of &#x60;members&#x60; to a &#x60;role&#x60;. &#x60;bindings&#x60; with no members will result in an error. | [optional] 
**etag** | **str** | &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;getIamPolicy&#x60;, and systems are expected to put that etag in the request to &#x60;setIamPolicy&#x60; to ensure that their change will be applied to the same version of the policy.  If no &#x60;etag&#x60; is provided in the call to &#x60;setIamPolicy&#x60;, then the existing policy is overwritten blindly. | [optional] 
**version** | **int** | Deprecated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


