# MovieDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] [readonly] 
**imdb_id** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**budget** | **float** |  | [optional] 
**genres** | [**List[Genre]**](Genre.md) |  | [optional] 
**homepage** | **str** |  | [optional] 
**related_videos** | [**List[RelatedVideo]**](RelatedVideo.md) |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**production_companies** | [**List[ProductionCompany]**](ProductionCompany.md) |  | [optional] 
**production_countries** | [**List[MovieDetailsProductionCountriesInner]**](MovieDetailsProductionCountriesInner.md) |  | [optional] 
**release_date** | **str** |  | [optional] 
**releases** | [**MovieDetailsReleases**](MovieDetailsReleases.md) |  | [optional] 
**revenue** | **float** |  | [optional] 
**runtime** | **float** |  | [optional] 
**spoken_languages** | [**List[SpokenLanguage]**](SpokenLanguage.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**credits** | [**MovieDetailsCredits**](MovieDetailsCredits.md) |  | [optional] 
**collection** | [**MovieDetailsCollection**](MovieDetailsCollection.md) |  | [optional] 
**external_ids** | [**ExternalIds**](ExternalIds.md) |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**watch_providers** | **List[List[WatchProvidersInner]]** |  | [optional] 

## Example

```python
from overseerr.models.movie_details import MovieDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetails from a JSON string
movie_details_instance = MovieDetails.from_json(json)
# print the JSON string representation of the object
print MovieDetails.to_json()

# convert the object into a dict
movie_details_dict = movie_details_instance.to_dict()
# create an instance of MovieDetails from a dict
movie_details_form_dict = movie_details.from_dict(movie_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


