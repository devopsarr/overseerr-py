# SpokenLanguage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**english_name** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.spoken_language import SpokenLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of SpokenLanguage from a JSON string
spoken_language_instance = SpokenLanguage.from_json(json)
# print the JSON string representation of the object
print SpokenLanguage.to_json()

# convert the object into a dict
spoken_language_dict = spoken_language_instance.to_dict()
# create an instance of SpokenLanguage from a dict
spoken_language_form_dict = spoken_language.from_dict(spoken_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


