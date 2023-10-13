# GetPersonCombinedCredits200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[CreditCast]**](CreditCast.md) |  | [optional] 
**crew** | [**List[CreditCrew]**](CreditCrew.md) |  | [optional] 
**id** | **float** |  | [optional] 

## Example

```python
from overseerr.models.get_person_combined_credits200_response import GetPersonCombinedCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonCombinedCredits200Response from a JSON string
get_person_combined_credits200_response_instance = GetPersonCombinedCredits200Response.from_json(json)
# print the JSON string representation of the object
print GetPersonCombinedCredits200Response.to_json()

# convert the object into a dict
get_person_combined_credits200_response_dict = get_person_combined_credits200_response_instance.to_dict()
# create an instance of GetPersonCombinedCredits200Response from a dict
get_person_combined_credits200_response_form_dict = get_person_combined_credits200_response.from_dict(get_person_combined_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


