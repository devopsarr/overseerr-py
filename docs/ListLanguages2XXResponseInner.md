# ListLanguages2XXResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_639_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.list_languages2_xx_response_inner import ListLanguages2XXResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListLanguages2XXResponseInner from a JSON string
list_languages2_xx_response_inner_instance = ListLanguages2XXResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListLanguages2XXResponseInner.to_json())

# convert the object into a dict
list_languages2_xx_response_inner_dict = list_languages2_xx_response_inner_instance.to_dict()
# create an instance of ListLanguages2XXResponseInner from a dict
list_languages2_xx_response_inner_form_dict = list_languages2_xx_response_inner.from_dict(list_languages2_xx_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


