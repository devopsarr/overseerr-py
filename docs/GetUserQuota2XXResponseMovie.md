# GetUserQuota2XXResponseMovie


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**used** | **float** |  | [optional] 
**remaining** | **float** |  | [optional] 
**restricted** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.get_user_quota2_xx_response_movie import GetUserQuota2XXResponseMovie

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserQuota2XXResponseMovie from a JSON string
get_user_quota2_xx_response_movie_instance = GetUserQuota2XXResponseMovie.from_json(json)
# print the JSON string representation of the object
print GetUserQuota2XXResponseMovie.to_json()

# convert the object into a dict
get_user_quota2_xx_response_movie_dict = get_user_quota2_xx_response_movie_instance.to_dict()
# create an instance of GetUserQuota2XXResponseMovie from a dict
get_user_quota2_xx_response_movie_form_dict = get_user_quota2_xx_response_movie.from_dict(get_user_quota2_xx_response_movie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


