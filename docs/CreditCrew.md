# CreditCrew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**original_language** | **str** |  | [optional] 
**episode_count** | **float** |  | [optional] 
**overview** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_name** | **str** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] 
**release_date** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 

## Example

```python
from overseerr.models.credit_crew import CreditCrew

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCrew from a JSON string
credit_crew_instance = CreditCrew.from_json(json)
# print the JSON string representation of the object
print(CreditCrew.to_json())

# convert the object into a dict
credit_crew_dict = credit_crew_instance.to_dict()
# create an instance of CreditCrew from a dict
credit_crew_from_dict = CreditCrew.from_dict(credit_crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


