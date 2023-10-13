# ListRegions200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.list_regions200_response_inner import ListRegions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegions200ResponseInner from a JSON string
list_regions200_response_inner_instance = ListRegions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListRegions200ResponseInner.to_json()

# convert the object into a dict
list_regions200_response_inner_dict = list_regions200_response_inner_instance.to_dict()
# create an instance of ListRegions200ResponseInner from a dict
list_regions200_response_inner_form_dict = list_regions200_response_inner.from_dict(list_regions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


