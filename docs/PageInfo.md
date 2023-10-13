# PageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**pages** | **float** |  | [optional] 
**results** | **float** |  | [optional] 

## Example

```python
from overseerr.models.page_info import PageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageInfo from a JSON string
page_info_instance = PageInfo.from_json(json)
# print the JSON string representation of the object
print PageInfo.to_json()

# convert the object into a dict
page_info_dict = page_info_instance.to_dict()
# create an instance of PageInfo from a dict
page_info_form_dict = page_info.from_dict(page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


