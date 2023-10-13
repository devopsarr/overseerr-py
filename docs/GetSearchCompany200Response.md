# GetSearchCompany200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 
**results** | [**List[Company]**](Company.md) |  | [optional] 

## Example

```python
from overseerr.models.get_search_company200_response import GetSearchCompany200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchCompany200Response from a JSON string
get_search_company200_response_instance = GetSearchCompany200Response.from_json(json)
# print the JSON string representation of the object
print GetSearchCompany200Response.to_json()

# convert the object into a dict
get_search_company200_response_dict = get_search_company200_response_instance.to_dict()
# create an instance of GetSearchCompany200Response from a dict
get_search_company200_response_form_dict = get_search_company200_response.from_dict(get_search_company200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


