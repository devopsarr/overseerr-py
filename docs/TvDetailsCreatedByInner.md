# TvDetailsCreatedByInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**gender** | **float** |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.tv_details_created_by_inner import TvDetailsCreatedByInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvDetailsCreatedByInner from a JSON string
tv_details_created_by_inner_instance = TvDetailsCreatedByInner.from_json(json)
# print the JSON string representation of the object
print TvDetailsCreatedByInner.to_json()

# convert the object into a dict
tv_details_created_by_inner_dict = tv_details_created_by_inner_instance.to_dict()
# create an instance of TvDetailsCreatedByInner from a dict
tv_details_created_by_inner_form_dict = tv_details_created_by_inner.from_dict(tv_details_created_by_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


