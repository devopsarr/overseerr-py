# TvDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**content_ratings** | [**TvDetailsContentRatings**](TvDetailsContentRatings.md) |  | [optional] 
**created_by** | [**List[TvDetailsCreatedByInner]**](TvDetailsCreatedByInner.md) |  | [optional] 
**episode_run_time** | **List[float]** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**genres** | [**List[Genre]**](Genre.md) |  | [optional] 
**homepage** | **str** |  | [optional] 
**in_production** | **bool** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**last_air_date** | **str** |  | [optional] 
**last_episode_to_air** | [**Episode**](Episode.md) |  | [optional] 
**name** | **str** |  | [optional] 
**next_episode_to_air** | [**Episode**](Episode.md) |  | [optional] 
**networks** | [**List[ProductionCompany]**](ProductionCompany.md) |  | [optional] 
**number_of_episodes** | **float** |  | [optional] 
**number_of_season** | **float** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**production_companies** | [**List[ProductionCompany]**](ProductionCompany.md) |  | [optional] 
**production_countries** | [**List[MovieDetailsProductionCountriesInner]**](MovieDetailsProductionCountriesInner.md) |  | [optional] 
**spoken_languages** | [**List[SpokenLanguage]**](SpokenLanguage.md) |  | [optional] 
**seasons** | [**List[Season]**](Season.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**credits** | [**MovieDetailsCredits**](MovieDetailsCredits.md) |  | [optional] 
**external_ids** | [**ExternalIds**](ExternalIds.md) |  | [optional] 
**keywords** | [**List[Keyword]**](Keyword.md) |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**watch_providers** | **List[List[WatchProvidersInner]]** |  | [optional] 

## Example

```python
from overseerr.models.tv_details import TvDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TvDetails from a JSON string
tv_details_instance = TvDetails.from_json(json)
# print the JSON string representation of the object
print TvDetails.to_json()

# convert the object into a dict
tv_details_dict = tv_details_instance.to_dict()
# create an instance of TvDetails from a dict
tv_details_form_dict = tv_details.from_dict(tv_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


