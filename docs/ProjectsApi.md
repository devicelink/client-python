# openapi_client.ProjectsApi

All URIs are relative to *https://cloudiot.googleapis.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudiot_projects_locations_registries_create**](ProjectsApi.md#cloudiot_projects_locations_registries_create) | **POST** /v1/{parent}/registries | 
[**cloudiot_projects_locations_registries_devices_config_versions_list**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_config_versions_list) | **GET** /v1/{name}/configVersions | 
[**cloudiot_projects_locations_registries_devices_create**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_create) | **POST** /v1/{parent}/devices | 
[**cloudiot_projects_locations_registries_devices_delete**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_delete) | **DELETE** /v1/{name} | 
[**cloudiot_projects_locations_registries_devices_get**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_get) | **GET** /v1/{name} | 
[**cloudiot_projects_locations_registries_devices_list**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_list) | **GET** /v1/{parent}/devices | 
[**cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config) | **POST** /v1/{name}:modifyCloudToDeviceConfig | 
[**cloudiot_projects_locations_registries_devices_patch**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_patch) | **PATCH** /v1/{name} | 
[**cloudiot_projects_locations_registries_devices_states_list**](ProjectsApi.md#cloudiot_projects_locations_registries_devices_states_list) | **GET** /v1/{name}/states | 
[**cloudiot_projects_locations_registries_groups_get_iam_policy**](ProjectsApi.md#cloudiot_projects_locations_registries_groups_get_iam_policy) | **POST** /v1/{resource}:getIamPolicy | 
[**cloudiot_projects_locations_registries_groups_set_iam_policy**](ProjectsApi.md#cloudiot_projects_locations_registries_groups_set_iam_policy) | **POST** /v1/{resource}:setIamPolicy | 
[**cloudiot_projects_locations_registries_groups_test_iam_permissions**](ProjectsApi.md#cloudiot_projects_locations_registries_groups_test_iam_permissions) | **POST** /v1/{resource}:testIamPermissions | 
[**cloudiot_projects_locations_registries_list**](ProjectsApi.md#cloudiot_projects_locations_registries_list) | **GET** /v1/{parent}/registries | 


# **cloudiot_projects_locations_registries_create**
> DeviceRegistry cloudiot_projects_locations_registries_create(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device_registry=device_registry)



Creates a device registry that contains devices.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
parent = 'parent_example' # str | The project and cloud region where this device registry must be created. For example, `projects/example-project/locations/us-central1`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
device_registry = openapi_client.DeviceRegistry() # DeviceRegistry |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_create(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device_registry=device_registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The project and cloud region where this device registry must be created. For example, &#x60;projects/example-project/locations/us-central1&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **device_registry** | [**DeviceRegistry**](DeviceRegistry.md)|  | [optional] 

### Return type

[**DeviceRegistry**](DeviceRegistry.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_config_versions_list**
> ListDeviceConfigVersionsResponse cloudiot_projects_locations_registries_devices_config_versions_list(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, num_versions=num_versions)



Lists the last few versions of the device configuration in descending order (i.e.: newest first).

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
num_versions = 56 # int | The number of versions to list. Versions are listed in decreasing order of the version number. The maximum number of versions retained is 10. If this value is zero, it will return all the versions available. (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_config_versions_list(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, num_versions=num_versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_config_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the device. For example, &#x60;projects/p0/locations/us-central1/registries/registry0/devices/device0&#x60; or &#x60;projects/p0/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **num_versions** | **int**| The number of versions to list. Versions are listed in decreasing order of the version number. The maximum number of versions retained is 10. If this value is zero, it will return all the versions available. | [optional] 

### Return type

[**ListDeviceConfigVersionsResponse**](ListDeviceConfigVersionsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_create**
> Device cloudiot_projects_locations_registries_devices_create(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device=device)



Creates a device in a device registry.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
parent = 'parent_example' # str | The name of the device registry where this device should be created. For example, `projects/example-project/locations/us-central1/registries/my-registry`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
device = openapi_client.Device() # Device |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_create(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the device registry where this device should be created. For example, &#x60;projects/example-project/locations/us-central1/registries/my-registry&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **device** | [**Device**](Device.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_delete**
> Empty cloudiot_projects_locations_registries_devices_delete(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol)



Deletes a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_delete(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the device. For example, &#x60;projects/p0/locations/us-central1/registries/registry0/devices/device0&#x60; or &#x60;projects/p0/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_get**
> Device cloudiot_projects_locations_registries_devices_get(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, field_mask=field_mask)



Gets details about a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
field_mask = 'field_mask_example' # str | The fields of the `Device` resource to be returned in the response. If the field mask is unset or empty, all fields are returned. (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_get(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, field_mask=field_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the device. For example, &#x60;projects/p0/locations/us-central1/registries/registry0/devices/device0&#x60; or &#x60;projects/p0/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **field_mask** | **str**| The fields of the &#x60;Device&#x60; resource to be returned in the response. If the field mask is unset or empty, all fields are returned. | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_list**
> ListDevicesResponse cloudiot_projects_locations_registries_devices_list(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device_ids=device_ids, device_num_ids=device_num_ids, field_mask=field_mask, page_size=page_size, page_token=page_token)



List devices in a device registry.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
parent = 'parent_example' # str | The device registry path. Required. For example, `projects/my-project/locations/us-central1/registries/my-registry`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
device_ids = ['device_ids_example'] # list[str] | A list of device string identifiers. If empty, it will ignore this field. For example, `['device0', 'device12']`. This field cannot hold more than 10,000 entries. (optional)
device_num_ids = ['device_num_ids_example'] # list[str] | A list of device numerical ids. If empty, it will ignore this field. This field cannot hold more than 10,000 entries. (optional)
field_mask = 'field_mask_example' # str | The fields of the `Device` resource to be returned in the response. The fields `id`, and `num_id` are always returned by default, along with any other fields specified. (optional)
page_size = 56 # int | The maximum number of devices to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested, but if there is a non-empty `page_token`, it indicates that more entries are available. (optional)
page_token = 'page_token_example' # str | The value returned by the last `ListDevicesResponse`; indicates that this is a continuation of a prior `ListDevices` call, and that the system should return the next page of data. (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_list(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, device_ids=device_ids, device_num_ids=device_num_ids, field_mask=field_mask, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The device registry path. Required. For example, &#x60;projects/my-project/locations/us-central1/registries/my-registry&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **device_ids** | [**list[str]**](str.md)| A list of device string identifiers. If empty, it will ignore this field. For example, &#x60;[&#39;device0&#39;, &#39;device12&#39;]&#x60;. This field cannot hold more than 10,000 entries. | [optional] 
 **device_num_ids** | [**list[str]**](str.md)| A list of device numerical ids. If empty, it will ignore this field. This field cannot hold more than 10,000 entries. | [optional] 
 **field_mask** | **str**| The fields of the &#x60;Device&#x60; resource to be returned in the response. The fields &#x60;id&#x60;, and &#x60;num_id&#x60; are always returned by default, along with any other fields specified. | [optional] 
 **page_size** | **int**| The maximum number of devices to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested, but if there is a non-empty &#x60;page_token&#x60;, it indicates that more entries are available. | [optional] 
 **page_token** | **str**| The value returned by the last &#x60;ListDevicesResponse&#x60;; indicates that this is a continuation of a prior &#x60;ListDevices&#x60; call, and that the system should return the next page of data. | [optional] 

### Return type

[**ListDevicesResponse**](ListDevicesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config**
> DeviceConfig cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, modify_cloud_to_device_config_request=modify_cloud_to_device_config_request)



Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
modify_cloud_to_device_config_request = openapi_client.ModifyCloudToDeviceConfigRequest() # ModifyCloudToDeviceConfigRequest |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, modify_cloud_to_device_config_request=modify_cloud_to_device_config_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_modify_cloud_to_device_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the device. For example, &#x60;projects/p0/locations/us-central1/registries/registry0/devices/device0&#x60; or &#x60;projects/p0/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **modify_cloud_to_device_config_request** | [**ModifyCloudToDeviceConfigRequest**](ModifyCloudToDeviceConfigRequest.md)|  | [optional] 

### Return type

[**DeviceConfig**](DeviceConfig.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_patch**
> Device cloudiot_projects_locations_registries_devices_patch(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, update_mask=update_mask, device=device)



Updates a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The resource path name. For example, `projects/p1/locations/us-central1/registries/registry0/devices/dev0` or `projects/p1/locations/us-central1/registries/registry0/devices/{num_id}`. When `name` is populated as a response from the service, it always ends in the device numeric ID.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
update_mask = 'update_mask_example' # str | Only updates the `device` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server. Mutable top-level fields: `credentials`, `blocked`, and `metadata` (optional)
device = openapi_client.Device() # Device |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_patch(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, update_mask=update_mask, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The resource path name. For example, &#x60;projects/p1/locations/us-central1/registries/registry0/devices/dev0&#x60; or &#x60;projects/p1/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. When &#x60;name&#x60; is populated as a response from the service, it always ends in the device numeric ID. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **update_mask** | **str**| Only updates the &#x60;device&#x60; fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server. Mutable top-level fields: &#x60;credentials&#x60;, &#x60;blocked&#x60;, and &#x60;metadata&#x60; | [optional] 
 **device** | [**Device**](Device.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_devices_states_list**
> ListDeviceStatesResponse cloudiot_projects_locations_registries_devices_states_list(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, num_states=num_states)



Lists the last few versions of the device state in descending order (i.e.: newest first).

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
num_states = 56 # int | The number of states to list. States are listed in descending order of update time. The maximum number of states retained is 10. If this value is zero, it will return all the states available. (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_devices_states_list(name, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, num_states=num_states)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_devices_states_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the device. For example, &#x60;projects/p0/locations/us-central1/registries/registry0/devices/device0&#x60; or &#x60;projects/p0/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **num_states** | **int**| The number of states to list. States are listed in descending order of update time. The maximum number of states retained is 10. If this value is zero, it will return all the states available. | [optional] 

### Return type

[**ListDeviceStatesResponse**](ListDeviceStatesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_groups_get_iam_policy**
> Policy cloudiot_projects_locations_registries_groups_get_iam_policy(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, get_iam_policy_request=get_iam_policy_request)



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
resource = 'resource_example' # str | REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
get_iam_policy_request = openapi_client.GetIamPolicyRequest() # GetIamPolicyRequest |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_groups_get_iam_policy(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, get_iam_policy_request=get_iam_policy_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_groups_get_iam_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **get_iam_policy_request** | [**GetIamPolicyRequest**](GetIamPolicyRequest.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_groups_set_iam_policy**
> Policy cloudiot_projects_locations_registries_groups_set_iam_policy(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, set_iam_policy_request=set_iam_policy_request)



Sets the access control policy on the specified resource. Replaces any existing policy.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
resource = 'resource_example' # str | REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
set_iam_policy_request = openapi_client.SetIamPolicyRequest() # SetIamPolicyRequest |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_groups_set_iam_policy(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, set_iam_policy_request=set_iam_policy_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_groups_set_iam_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **set_iam_policy_request** | [**SetIamPolicyRequest**](SetIamPolicyRequest.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_groups_test_iam_permissions**
> TestIamPermissionsResponse cloudiot_projects_locations_registries_groups_test_iam_permissions(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, test_iam_permissions_request=test_iam_permissions_request)



Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
resource = 'resource_example' # str | REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
test_iam_permissions_request = openapi_client.TestIamPermissionsRequest() # TestIamPermissionsRequest |  (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_groups_test_iam_permissions(resource, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, test_iam_permissions_request=test_iam_permissions_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_groups_test_iam_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **test_iam_permissions_request** | [**TestIamPermissionsRequest**](TestIamPermissionsRequest.md)|  | [optional] 

### Return type

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudiot_projects_locations_registries_list**
> ListDeviceRegistriesResponse cloudiot_projects_locations_registries_list(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, page_size=page_size, page_token=page_token)



Lists device registries.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.ProjectsApi(openapi_client.ApiClient(configuration))
parent = 'parent_example' # str | The project and cloud region path. For example, `projects/example-project/locations/us-central1`.
xgafv = 'xgafv_example' # str | V1 error format. (optional)
access_token = 'access_token_example' # str | OAuth access token. (optional)
alt = 'json' # str | Data format for response. (optional) (default to 'json')
bearer_token = 'bearer_token_example' # str | OAuth bearer token. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pp = True # bool | Pretty-print response. (optional) (default to True)
pretty_print = True # bool | Returns response with indentations and line breaks. (optional) (default to True)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
page_size = 56 # int | The maximum number of registries to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested, but if there is a non-empty `page_token`, it indicates that more entries are available. (optional)
page_token = 'page_token_example' # str | The value returned by the last `ListDeviceRegistriesResponse`; indicates that this is a continuation of a prior `ListDeviceRegistries` call, and that the system should return the next page of data. (optional)

try:
    api_response = api_instance.cloudiot_projects_locations_registries_list(parent, xgafv=xgafv, access_token=access_token, alt=alt, bearer_token=bearer_token, param_callback=param_callback, fields=fields, key=key, oauth_token=oauth_token, pp=pp, pretty_print=pretty_print, quota_user=quota_user, upload_type=upload_type, upload_protocol=upload_protocol, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cloudiot_projects_locations_registries_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The project and cloud region path. For example, &#x60;projects/example-project/locations/us-central1&#x60;. | 
 **xgafv** | **str**| V1 error format. | [optional] 
 **access_token** | **str**| OAuth access token. | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to &#39;json&#39;]
 **bearer_token** | **str**| OAuth bearer token. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pp** | **bool**| Pretty-print response. | [optional] [default to True]
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to True]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **page_size** | **int**| The maximum number of registries to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested, but if there is a non-empty &#x60;page_token&#x60;, it indicates that more entries are available. | [optional] 
 **page_token** | **str**| The value returned by the last &#x60;ListDeviceRegistriesResponse&#x60;; indicates that this is a continuation of a prior &#x60;ListDeviceRegistries&#x60; call, and that the system should return the next page of data. | [optional] 

### Return type

[**ListDeviceRegistriesResponse**](ListDeviceRegistriesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

