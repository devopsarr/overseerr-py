# ProductionCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**logo_path** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.production_company import ProductionCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionCompany from a JSON string
production_company_instance = ProductionCompany.from_json(json)
# print the JSON string representation of the object
print(ProductionCompany.to_json())

# convert the object into a dict
production_company_dict = production_company_instance.to_dict()
# create an instance of ProductionCompany from a dict
production_company_from_dict = ProductionCompany.from_dict(production_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


