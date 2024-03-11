# GetTvRatings2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**year** | **float** |  | [optional] 
**url** | **str** |  | [optional] 
**critics_score** | **float** |  | [optional] 
**critics_rating** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_tv_ratings2_xx_response import GetTvRatings2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTvRatings2XXResponse from a JSON string
get_tv_ratings2_xx_response_instance = GetTvRatings2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetTvRatings2XXResponse.to_json())

# convert the object into a dict
get_tv_ratings2_xx_response_dict = get_tv_ratings2_xx_response_instance.to_dict()
# create an instance of GetTvRatings2XXResponse from a dict
get_tv_ratings2_xx_response_form_dict = get_tv_ratings2_xx_response.from_dict(get_tv_ratings2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


