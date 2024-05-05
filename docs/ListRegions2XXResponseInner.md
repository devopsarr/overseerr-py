# ListRegions2XXResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.list_regions2_xx_response_inner import ListRegions2XXResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegions2XXResponseInner from a JSON string
list_regions2_xx_response_inner_instance = ListRegions2XXResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListRegions2XXResponseInner.to_json())

# convert the object into a dict
list_regions2_xx_response_inner_dict = list_regions2_xx_response_inner_instance.to_dict()
# create an instance of ListRegions2XXResponseInner from a dict
list_regions2_xx_response_inner_from_dict = ListRegions2XXResponseInner.from_dict(list_regions2_xx_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


