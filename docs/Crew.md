# Crew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**gender** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.crew import Crew

# TODO update the JSON string below
json = "{}"
# create an instance of Crew from a JSON string
crew_instance = Crew.from_json(json)
# print the JSON string representation of the object
print Crew.to_json()

# convert the object into a dict
crew_dict = crew_instance.to_dict()
# create an instance of Crew from a dict
crew_form_dict = crew.from_dict(crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


