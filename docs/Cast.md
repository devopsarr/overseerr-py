# Cast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**cast_id** | **float** |  | [optional] 
**character** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**gender** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**order** | **float** |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.cast import Cast

# TODO update the JSON string below
json = "{}"
# create an instance of Cast from a JSON string
cast_instance = Cast.from_json(json)
# print the JSON string representation of the object
print(Cast.to_json())

# convert the object into a dict
cast_dict = cast_instance.to_dict()
# create an instance of Cast from a dict
cast_from_dict = Cast.from_dict(cast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


