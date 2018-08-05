# openapi_client.DefaultApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicelink_add_device_to_group**](DefaultApi.md#devicelink_add_device_to_group) | **PUT** /v1/groups/{group_id}/device/{id} | Adds device to group.
[**devicelink_create_group**](DefaultApi.md#devicelink_create_group) | **POST** /v1/groups | Creates a device group.
[**devicelink_delete_group**](DefaultApi.md#devicelink_delete_group) | **DELETE** /v1/groups/{id} | Deletes a group.
[**devicelink_do_action**](DefaultApi.md#devicelink_do_action) | **POST** /v1/device/{id}/actions | Prompts a device action.
[**devicelink_get_actions**](DefaultApi.md#devicelink_get_actions) | **GET** /v1/device/{id}/actions | Gets device actions.
[**devicelink_get_data**](DefaultApi.md#devicelink_get_data) | **GET** /v1/device/{id}/properties | Gets device properties.
[**devicelink_get_device_event**](DefaultApi.md#devicelink_get_device_event) | **GET** /v1/device/{id}/events | Gets device events.
[**devicelink_get_group_info**](DefaultApi.md#devicelink_get_group_info) | **GET** /v1/groups/{id} | Gets a device group.
[**devicelink_get_groups**](DefaultApi.md#devicelink_get_groups) | **GET** /v1/groups | Gets device groups.
[**devicelink_get_specific_action**](DefaultApi.md#devicelink_get_specific_action) | **GET** /v1/device/{id}/actions/{action-id} | Gets a device action.
[**devicelink_remove_device_from_group**](DefaultApi.md#devicelink_remove_device_from_group) | **DELETE** /v1/groups/{group_id}/device/{id} | Removes device from a group.
[**devicelink_update_group_metadata**](DefaultApi.md#devicelink_update_group_metadata) | **PATCH** /v1/groups/{id} | Updates group information.


# **devicelink_add_device_to_group**
> devicelink_add_device_to_group(group_id, id)

Adds device to group.

Adds a device to a group.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
group_id = 'group_id_example' # str | uuid of group
id = 'id_example' # str | uuid of device

try:
    # Adds device to group.
    api_instance.devicelink_add_device_to_group(group_id, id)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_add_device_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| uuid of group | 
 **id** | [**str**](.md)| uuid of device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_create_group**
> InlineResponse201 devicelink_create_group(body=body)

Creates a device group.

Creates virtual group for devices. Request can include list of devices as request-body or attributes.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
body = openapi_client.Body() # Body | List of devices (optional)

try:
    # Creates a device group.
    api_response = api_instance.devicelink_create_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| List of devices | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_delete_group**
> devicelink_delete_group(id)

Deletes a group.

Deletes group and its metadata.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of group

try:
    # Deletes a group.
    api_instance.devicelink_delete_group(id)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_do_action**
> InlineResponse2011 devicelink_do_action(id, body2)

Prompts a device action.

Prompts an action on a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of device
body2 = openapi_client.Body2() # Body2 | Action that shall be executed

try:
    # Prompts a device action.
    api_response = api_instance.devicelink_do_action(id, body2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_do_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of device | 
 **body2** | [**Body2**](Body2.md)| Action that shall be executed | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_actions**
> object devicelink_get_actions(id, _from=_from, to=to, start=start, sort=sort, count=count)

Gets device actions.

Returns device actions within a time range.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of device
_from = 56 # int | Range start in seconds since epoch (optional)
to = 56 # int | Range end in seconds since epoch (optional)
start = 56 # int | The start key of the first action object to return, (optional)
sort = 'desc' # str | If set to asc (default), action objects are returned in time ascending order (i.e. starting with from or start and ending with stop). If set to desc, action objects are returned in time descending order (i.e. starting with to or start and ending with from). (optional) (default to 'desc')
count = 100 # int | Limits the number of returned action objects (optional) (default to 100)

try:
    # Gets device actions.
    api_response = api_instance.devicelink_get_actions(id, _from=_from, to=to, start=start, sort=sort, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of device | 
 **_from** | **int**| Range start in seconds since epoch | [optional] 
 **to** | **int**| Range end in seconds since epoch | [optional] 
 **start** | **int**| The start key of the first action object to return, | [optional] 
 **sort** | **str**| If set to asc (default), action objects are returned in time ascending order (i.e. starting with from or start and ending with stop). If set to desc, action objects are returned in time descending order (i.e. starting with to or start and ending with from). | [optional] [default to &#39;desc&#39;]
 **count** | **int**| Limits the number of returned action objects | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_data**
> DeviceData devicelink_get_data(id, _from=_from, to=to, start=start, sort=sort, count=count, property_key=property_key, index=index)

Gets device properties.

Returns properties for a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of device
_from = 56 # int | Start time in seconds since epoch (optional)
to = 56 # int | End time in seconds since epoch (optional)
start = 56 # int | The start key of the first property object to return (optional)
sort = 'desc' # str | Order in which roperty objects are returned (optional) (default to 'desc')
count = 100 # int | Limits the number of returned property objects (optional) (default to 100)
property_key = 56 # int | Filters returned property objects by property-key (optional)
index = 56 # int | Filters returned property objects by property-index (can only be used in combination with property-key parameter) (optional)

try:
    # Gets device properties.
    api_response = api_instance.devicelink_get_data(id, _from=_from, to=to, start=start, sort=sort, count=count, property_key=property_key, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of device | 
 **_from** | **int**| Start time in seconds since epoch | [optional] 
 **to** | **int**| End time in seconds since epoch | [optional] 
 **start** | **int**| The start key of the first property object to return | [optional] 
 **sort** | **str**| Order in which roperty objects are returned | [optional] [default to &#39;desc&#39;]
 **count** | **int**| Limits the number of returned property objects | [optional] [default to 100]
 **property_key** | **int**| Filters returned property objects by property-key | [optional] 
 **index** | **int**| Filters returned property objects by property-index (can only be used in combination with property-key parameter) | [optional] 

### Return type

[**DeviceData**](DeviceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_device_event**
> object devicelink_get_device_event(id)

Gets device events.

Opens event-stream for a device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of device

try:
    # Gets device events.
    api_response = api_instance.devicelink_get_device_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_device_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of device | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_group_info**
> GroupInfo devicelink_get_group_info(id)

Gets a device group.

Returns a group, members, and metadata.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of group

try:
    # Gets a device group.
    api_response = api_instance.devicelink_get_group_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_group_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of group | 

### Return type

[**GroupInfo**](GroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_groups**
> GroupInfo devicelink_get_groups()

Gets device groups.

Returns all groups with devices and metadata.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    # Gets device groups.
    api_response = api_instance.devicelink_get_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupInfo**](GroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_get_specific_action**
> InlineResponse200 devicelink_get_specific_action(id, action_id)

Gets a device action.

Returns a action of device.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of device
action_id = 56 # int | Action key

try:
    # Gets a device action.
    api_response = api_instance.devicelink_get_specific_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_get_specific_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of device | 
 **action_id** | **int**| Action key | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_remove_device_from_group**
> devicelink_remove_device_from_group(id2, id)

Removes device from a group.

Removes a device from a group.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id2 = 'id_example' # str | uuid of group
id = 'id_example' # str | uuid of device

try:
    # Removes device from a group.
    api_instance.devicelink_remove_device_from_group(id2, id)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_remove_device_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id2** | [**str**](.md)| uuid of group | 
 **id** | [**str**](.md)| uuid of device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelink_update_group_metadata**
> devicelink_update_group_metadata(id, body1=body1)

Updates group information.

Updates group metadata.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | uuid of group
body1 = openapi_client.Body1() # Body1 | New metadata of group (optional)

try:
    # Updates group information.
    api_instance.devicelink_update_group_metadata(id, body1=body1)
except ApiException as e:
    print("Exception when calling DefaultApi->devicelink_update_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| uuid of group | 
 **body1** | [**Body1**](Body1.md)| New metadata of group | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

