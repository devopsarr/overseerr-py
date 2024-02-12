# GetSearchCompany2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 
**results** | [**List[Company]**](Company.md) |  | [optional] 

## Example

```python
from overseerr.models.get_search_company2_xx_response import GetSearchCompany2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchCompany2XXResponse from a JSON string
get_search_company2_xx_response_instance = GetSearchCompany2XXResponse.from_json(json)
# print the JSON string representation of the object
print GetSearchCompany2XXResponse.to_json()

# convert the object into a dict
get_search_company2_xx_response_dict = get_search_company2_xx_response_instance.to_dict()
# create an instance of GetSearchCompany2XXResponse from a dict
get_search_company2_xx_response_form_dict = get_search_company2_xx_response.from_dict(get_search_company2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


