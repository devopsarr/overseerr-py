# ExternalIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facebook_id** | **str** |  | [optional] 
**freebase_id** | **str** |  | [optional] 
**freebase_mid** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**instagram_id** | **str** |  | [optional] 
**tvdb_id** | **float** |  | [optional] 
**tvrage_id** | **float** |  | [optional] 
**twitter_id** | **str** |  | [optional] 

## Example

```python
from overseerr.models.external_ids import ExternalIds

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIds from a JSON string
external_ids_instance = ExternalIds.from_json(json)
# print the JSON string representation of the object
print(ExternalIds.to_json())

# convert the object into a dict
external_ids_dict = external_ids_instance.to_dict()
# create an instance of ExternalIds from a dict
external_ids_from_dict = ExternalIds.from_dict(external_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


