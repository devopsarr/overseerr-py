# PersonDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**deathday** | **str** |  | [optional] 
**known_for_department** | **str** |  | [optional] 
**also_known_as** | **List[str]** |  | [optional] 
**gender** | **str** |  | [optional] 
**biography** | **str** |  | [optional] 
**popularity** | **str** |  | [optional] 
**place_of_birth** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 

## Example

```python
from overseerr.models.person_details import PersonDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PersonDetails from a JSON string
person_details_instance = PersonDetails.from_json(json)
# print the JSON string representation of the object
print(PersonDetails.to_json())

# convert the object into a dict
person_details_dict = person_details_instance.to_dict()
# create an instance of PersonDetails from a dict
person_details_form_dict = person_details.from_dict(person_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


