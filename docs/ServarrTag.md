# ServarrTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from overseerr.models.servarr_tag import ServarrTag

# TODO update the JSON string below
json = "{}"
# create an instance of ServarrTag from a JSON string
servarr_tag_instance = ServarrTag.from_json(json)
# print the JSON string representation of the object
print(ServarrTag.to_json())

# convert the object into a dict
servarr_tag_dict = servarr_tag_instance.to_dict()
# create an instance of ServarrTag from a dict
servarr_tag_from_dict = ServarrTag.from_dict(servarr_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


