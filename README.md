# overseerr-py
This is the documentation for the Overseerr API backend.

Two primary authentication methods are supported:

- **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie.
- **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

[comment]: # (x-release-please-start-version)
- Package version: 0.0.0

[comment]: # (x-release-please-end)
- API version: 1.0.0

- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/devopsarr/overseerr-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/devopsarr/overseerr-py.git`)

Then import the package:
```python
import overseerr
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import overseerr
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import overseerr
from overseerr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)



# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.AuthApi(api_client)
    create_auth_local_request = overseerr.CreateAuthLocalRequest() # CreateAuthLocalRequest | 

    try:
        # Sign in using a local account
        api_response = api_instance.create_auth_local(create_auth_local_request)
        print("The response of AuthApi->create_auth_local:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->create_auth_local: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5055/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**create_auth_local**](docs/AuthApi.md#create_auth_local) | **POST** /auth/local | Sign in using a local account
*AuthApi* | [**create_auth_logout**](docs/AuthApi.md#create_auth_logout) | **POST** /auth/logout | Sign out and clear session cookie
*AuthApi* | [**create_auth_plex**](docs/AuthApi.md#create_auth_plex) | **POST** /auth/plex | Sign in using a Plex token
*AuthApi* | [**get_auth_me**](docs/AuthApi.md#get_auth_me) | **GET** /auth/me | Get logged-in user
*CollectionApi* | [**get_collection_by_collection_id**](docs/CollectionApi.md#get_collection_by_collection_id) | **GET** /collection/{collectionId} | Get collection details
*IssueApi* | [**create_issue**](docs/IssueApi.md#create_issue) | **POST** /issue | Create new issue
*IssueApi* | [**create_issue_by_status**](docs/IssueApi.md#create_issue_by_status) | **POST** /issue/{issueId}/{status} | Update an issue&#39;s status
*IssueApi* | [**create_issue_comment**](docs/IssueApi.md#create_issue_comment) | **POST** /issue/{issueId}/comment | Create a comment
*IssueApi* | [**delete_issue**](docs/IssueApi.md#delete_issue) | **DELETE** /issue/{issueId} | Delete issue
*IssueApi* | [**delete_issue_comment**](docs/IssueApi.md#delete_issue_comment) | **DELETE** /issueComment/{commentId} | Delete issue comment
*IssueApi* | [**get_issue**](docs/IssueApi.md#get_issue) | **GET** /issue | Get all issues
*IssueApi* | [**get_issue_by_issue_id**](docs/IssueApi.md#get_issue_by_issue_id) | **GET** /issue/{issueId} | Get issue
*IssueApi* | [**get_issue_comment_by_comment_id**](docs/IssueApi.md#get_issue_comment_by_comment_id) | **GET** /issueComment/{commentId} | Get issue comment
*IssueApi* | [**get_issue_count**](docs/IssueApi.md#get_issue_count) | **GET** /issue/count | Gets issue counts
*IssueApi* | [**update_issue_comment**](docs/IssueApi.md#update_issue_comment) | **PUT** /issueComment/{commentId} | Update issue comment
*MediaApi* | [**create_media_by_status**](docs/MediaApi.md#create_media_by_status) | **POST** /media/{mediaId}/{status} | Update media status
*MediaApi* | [**delete_media**](docs/MediaApi.md#delete_media) | **DELETE** /media/{mediaId} | Delete media item
*MediaApi* | [**get_media**](docs/MediaApi.md#get_media) | **GET** /media | Get media
*MediaApi* | [**get_media_watch_data**](docs/MediaApi.md#get_media_watch_data) | **GET** /media/{mediaId}/watch_data | Get watch data
*MoviesApi* | [**get_movie_by_movie_id**](docs/MoviesApi.md#get_movie_by_movie_id) | **GET** /movie/{movieId} | Get movie details
*MoviesApi* | [**get_movie_ratings**](docs/MoviesApi.md#get_movie_ratings) | **GET** /movie/{movieId}/ratings | Get movie ratings
*MoviesApi* | [**get_movie_ratingscombined**](docs/MoviesApi.md#get_movie_ratingscombined) | **GET** /movie/{movieId}/ratingscombined | Get RT and IMDB movie ratings combined
*MoviesApi* | [**get_movie_recommendations**](docs/MoviesApi.md#get_movie_recommendations) | **GET** /movie/{movieId}/recommendations | Get recommended movies
*MoviesApi* | [**get_movie_similar**](docs/MoviesApi.md#get_movie_similar) | **GET** /movie/{movieId}/similar | Get similar movies
*OtherApi* | [**get_keyword_by_keyword_id**](docs/OtherApi.md#get_keyword_by_keyword_id) | **GET** /keyword/{keywordId} | Get keyword
*OtherApi* | [**list_watchproviders_movies**](docs/OtherApi.md#list_watchproviders_movies) | **GET** /watchproviders/movies | Get watch provider movies
*OtherApi* | [**list_watchproviders_regions**](docs/OtherApi.md#list_watchproviders_regions) | **GET** /watchproviders/regions | Get watch provider regions
*OtherApi* | [**list_watchproviders_tv**](docs/OtherApi.md#list_watchproviders_tv) | **GET** /watchproviders/tv | Get watch provider series
*PersonApi* | [**get_person_by_person_id**](docs/PersonApi.md#get_person_by_person_id) | **GET** /person/{personId} | Get person details
*PersonApi* | [**get_person_combined_credits**](docs/PersonApi.md#get_person_combined_credits) | **GET** /person/{personId}/combined_credits | Get combined credits
*PublicApi* | [**get_status**](docs/PublicApi.md#get_status) | **GET** /status | Get Overseerr status
*PublicApi* | [**get_status_appdata**](docs/PublicApi.md#get_status_appdata) | **GET** /status/appdata | Get application data volume status
*RequestApi* | [**create_request**](docs/RequestApi.md#create_request) | **POST** /request | Create new request
*RequestApi* | [**create_request_by_status**](docs/RequestApi.md#create_request_by_status) | **POST** /request/{requestId}/{status} | Update a request&#39;s status
*RequestApi* | [**create_request_retry**](docs/RequestApi.md#create_request_retry) | **POST** /request/{requestId}/retry | Retry failed request
*RequestApi* | [**delete_request**](docs/RequestApi.md#delete_request) | **DELETE** /request/{requestId} | Delete request
*RequestApi* | [**get_request**](docs/RequestApi.md#get_request) | **GET** /request | Get all requests
*RequestApi* | [**get_request_by_request_id**](docs/RequestApi.md#get_request_by_request_id) | **GET** /request/{requestId} | Get MediaRequest
*RequestApi* | [**get_request_count**](docs/RequestApi.md#get_request_count) | **GET** /request/count | Gets request counts
*RequestApi* | [**update_request**](docs/RequestApi.md#update_request) | **PUT** /request/{requestId} | Update MediaRequest
*SearchApi* | [**get_discover_keyword_movies**](docs/SearchApi.md#get_discover_keyword_movies) | **GET** /discover/keyword/{keywordId}/movies | Get movies from keyword
*SearchApi* | [**get_discover_movies**](docs/SearchApi.md#get_discover_movies) | **GET** /discover/movies | Discover movies
*SearchApi* | [**get_discover_movies_genre_by_genre_id**](docs/SearchApi.md#get_discover_movies_genre_by_genre_id) | **GET** /discover/movies/genre/{genreId} | Discover movies by genre
*SearchApi* | [**get_discover_movies_language_by_language**](docs/SearchApi.md#get_discover_movies_language_by_language) | **GET** /discover/movies/language/{language} | Discover movies by original language
*SearchApi* | [**get_discover_movies_studio_by_studio_id**](docs/SearchApi.md#get_discover_movies_studio_by_studio_id) | **GET** /discover/movies/studio/{studioId} | Discover movies by studio
*SearchApi* | [**get_discover_movies_upcoming**](docs/SearchApi.md#get_discover_movies_upcoming) | **GET** /discover/movies/upcoming | Upcoming movies
*SearchApi* | [**get_discover_trending**](docs/SearchApi.md#get_discover_trending) | **GET** /discover/trending | Trending movies and TV
*SearchApi* | [**get_discover_tv**](docs/SearchApi.md#get_discover_tv) | **GET** /discover/tv | Discover TV shows
*SearchApi* | [**get_discover_tv_genre_by_genre_id**](docs/SearchApi.md#get_discover_tv_genre_by_genre_id) | **GET** /discover/tv/genre/{genreId} | Discover TV shows by genre
*SearchApi* | [**get_discover_tv_language_by_language**](docs/SearchApi.md#get_discover_tv_language_by_language) | **GET** /discover/tv/language/{language} | Discover TV shows by original language
*SearchApi* | [**get_discover_tv_network_by_network_id**](docs/SearchApi.md#get_discover_tv_network_by_network_id) | **GET** /discover/tv/network/{networkId} | Discover TV shows by network
*SearchApi* | [**get_discover_tv_upcoming**](docs/SearchApi.md#get_discover_tv_upcoming) | **GET** /discover/tv/upcoming | Discover Upcoming TV shows
*SearchApi* | [**get_discover_watchlist**](docs/SearchApi.md#get_discover_watchlist) | **GET** /discover/watchlist | Get the Plex watchlist.
*SearchApi* | [**get_search**](docs/SearchApi.md#get_search) | **GET** /search | Search for movies, TV shows, or people
*SearchApi* | [**get_search_company**](docs/SearchApi.md#get_search_company) | **GET** /search/company | Search for companies
*SearchApi* | [**get_search_keyword**](docs/SearchApi.md#get_search_keyword) | **GET** /search/keyword | Search for keywords
*SearchApi* | [**list_discover_genreslider_movie**](docs/SearchApi.md#list_discover_genreslider_movie) | **GET** /discover/genreslider/movie | Get genre slider data for movies
*SearchApi* | [**list_discover_genreslider_tv**](docs/SearchApi.md#list_discover_genreslider_tv) | **GET** /discover/genreslider/tv | Get genre slider data for TV series
*ServiceApi* | [**get_service_radarr_by_radarr_id**](docs/ServiceApi.md#get_service_radarr_by_radarr_id) | **GET** /service/radarr/{radarrId} | Get Radarr server quality profiles and root folders
*ServiceApi* | [**get_service_sonarr_by_sonarr_id**](docs/ServiceApi.md#get_service_sonarr_by_sonarr_id) | **GET** /service/sonarr/{sonarrId} | Get Sonarr server quality profiles and root folders
*ServiceApi* | [**list_service_radarr**](docs/ServiceApi.md#list_service_radarr) | **GET** /service/radarr | Get non-sensitive Radarr server list
*ServiceApi* | [**list_service_sonarr**](docs/ServiceApi.md#list_service_sonarr) | **GET** /service/sonarr | Get non-sensitive Sonarr server list
*ServiceApi* | [**list_service_sonarr_lookup_by_tmdb_id**](docs/ServiceApi.md#list_service_sonarr_lookup_by_tmdb_id) | **GET** /service/sonarr/lookup/{tmdbId} | Get series from Sonarr
*SettingsApi* | [**create_cache_flush**](docs/SettingsApi.md#create_cache_flush) | **POST** /settings/cache/{cacheId}/flush | Flush a specific cache
*SettingsApi* | [**create_discover**](docs/SettingsApi.md#create_discover) | **POST** /settings/discover | Batch update all sliders.
*SettingsApi* | [**create_discover_add**](docs/SettingsApi.md#create_discover_add) | **POST** /settings/discover/add | Add a new slider
*SettingsApi* | [**create_initialize**](docs/SettingsApi.md#create_initialize) | **POST** /settings/initialize | Initialize application
*SettingsApi* | [**create_jobs_cancel**](docs/SettingsApi.md#create_jobs_cancel) | **POST** /settings/jobs/{jobId}/cancel | Cancel a specific job
*SettingsApi* | [**create_jobs_run**](docs/SettingsApi.md#create_jobs_run) | **POST** /settings/jobs/{jobId}/run | Invoke a specific job
*SettingsApi* | [**create_jobs_schedule**](docs/SettingsApi.md#create_jobs_schedule) | **POST** /settings/jobs/{jobId}/schedule | Modify job schedule
*SettingsApi* | [**create_main**](docs/SettingsApi.md#create_main) | **POST** /settings/main | Update main settings
*SettingsApi* | [**create_main_regenerate**](docs/SettingsApi.md#create_main_regenerate) | **POST** /settings/main/regenerate | Get main settings with newly-generated API key
*SettingsApi* | [**create_notifications_discord**](docs/SettingsApi.md#create_notifications_discord) | **POST** /settings/notifications/discord | Update Discord notification settings
*SettingsApi* | [**create_notifications_email**](docs/SettingsApi.md#create_notifications_email) | **POST** /settings/notifications/email | Update email notification settings
*SettingsApi* | [**create_notifications_gotify**](docs/SettingsApi.md#create_notifications_gotify) | **POST** /settings/notifications/gotify | Update Gotify notification settings
*SettingsApi* | [**create_notifications_lunasea**](docs/SettingsApi.md#create_notifications_lunasea) | **POST** /settings/notifications/lunasea | Update LunaSea notification settings
*SettingsApi* | [**create_notifications_pushbullet**](docs/SettingsApi.md#create_notifications_pushbullet) | **POST** /settings/notifications/pushbullet | Update Pushbullet notification settings
*SettingsApi* | [**create_notifications_pushover**](docs/SettingsApi.md#create_notifications_pushover) | **POST** /settings/notifications/pushover | Update Pushover notification settings
*SettingsApi* | [**create_notifications_slack**](docs/SettingsApi.md#create_notifications_slack) | **POST** /settings/notifications/slack | Update Slack notification settings
*SettingsApi* | [**create_notifications_telegram**](docs/SettingsApi.md#create_notifications_telegram) | **POST** /settings/notifications/telegram | Update Telegram notification settings
*SettingsApi* | [**create_notifications_webhook**](docs/SettingsApi.md#create_notifications_webhook) | **POST** /settings/notifications/webhook | Update webhook notification settings
*SettingsApi* | [**create_notifications_webpush**](docs/SettingsApi.md#create_notifications_webpush) | **POST** /settings/notifications/webpush | Update Web Push notification settings
*SettingsApi* | [**create_plex**](docs/SettingsApi.md#create_plex) | **POST** /settings/plex | Update Plex settings
*SettingsApi* | [**create_plex_sync**](docs/SettingsApi.md#create_plex_sync) | **POST** /settings/plex/sync | Start full Plex library scan
*SettingsApi* | [**create_radarr**](docs/SettingsApi.md#create_radarr) | **POST** /settings/radarr | Create Radarr instance
*SettingsApi* | [**create_sonarr**](docs/SettingsApi.md#create_sonarr) | **POST** /settings/sonarr | Create Sonarr instance
*SettingsApi* | [**create_tautulli**](docs/SettingsApi.md#create_tautulli) | **POST** /settings/tautulli | Update Tautulli settings
*SettingsApi* | [**delete_discover**](docs/SettingsApi.md#delete_discover) | **DELETE** /settings/discover/{sliderId} | Delete slider by ID
*SettingsApi* | [**delete_radarr**](docs/SettingsApi.md#delete_radarr) | **DELETE** /settings/radarr/{radarrId} | Delete Radarr instance
*SettingsApi* | [**delete_sonarr**](docs/SettingsApi.md#delete_sonarr) | **DELETE** /settings/sonarr/{sonarrId} | Delete Sonarr instance
*SettingsApi* | [**get_about**](docs/SettingsApi.md#get_about) | **GET** /settings/about | Get server stats
*SettingsApi* | [**get_cache**](docs/SettingsApi.md#get_cache) | **GET** /settings/cache | Get a list of active caches
*SettingsApi* | [**get_discover_reset**](docs/SettingsApi.md#get_discover_reset) | **GET** /settings/discover/reset | Reset all discover sliders
*SettingsApi* | [**get_main**](docs/SettingsApi.md#get_main) | **GET** /settings/main | Get main settings
*SettingsApi* | [**get_notifications_discord**](docs/SettingsApi.md#get_notifications_discord) | **GET** /settings/notifications/discord | Get Discord notification settings
*SettingsApi* | [**get_notifications_email**](docs/SettingsApi.md#get_notifications_email) | **GET** /settings/notifications/email | Get email notification settings
*SettingsApi* | [**get_notifications_gotify**](docs/SettingsApi.md#get_notifications_gotify) | **GET** /settings/notifications/gotify | Get Gotify notification settings
*SettingsApi* | [**get_notifications_lunasea**](docs/SettingsApi.md#get_notifications_lunasea) | **GET** /settings/notifications/lunasea | Get LunaSea notification settings
*SettingsApi* | [**get_notifications_pushbullet**](docs/SettingsApi.md#get_notifications_pushbullet) | **GET** /settings/notifications/pushbullet | Get Pushbullet notification settings
*SettingsApi* | [**get_notifications_pushover**](docs/SettingsApi.md#get_notifications_pushover) | **GET** /settings/notifications/pushover | Get Pushover notification settings
*SettingsApi* | [**get_notifications_slack**](docs/SettingsApi.md#get_notifications_slack) | **GET** /settings/notifications/slack | Get Slack notification settings
*SettingsApi* | [**get_notifications_telegram**](docs/SettingsApi.md#get_notifications_telegram) | **GET** /settings/notifications/telegram | Get Telegram notification settings
*SettingsApi* | [**get_notifications_webhook**](docs/SettingsApi.md#get_notifications_webhook) | **GET** /settings/notifications/webhook | Get webhook notification settings
*SettingsApi* | [**get_notifications_webpush**](docs/SettingsApi.md#get_notifications_webpush) | **GET** /settings/notifications/webpush | Get Web Push notification settings
*SettingsApi* | [**get_plex**](docs/SettingsApi.md#get_plex) | **GET** /settings/plex | Get Plex settings
*SettingsApi* | [**get_plex_sync**](docs/SettingsApi.md#get_plex_sync) | **GET** /settings/plex/sync | Get status of full Plex library scan
*SettingsApi* | [**get_public**](docs/SettingsApi.md#get_public) | **GET** /settings/public | Get public settings
*SettingsApi* | [**get_tautulli**](docs/SettingsApi.md#get_tautulli) | **GET** /settings/tautulli | Get Tautulli settings
*SettingsApi* | [**list_discover**](docs/SettingsApi.md#list_discover) | **GET** /settings/discover | Get all discover sliders
*SettingsApi* | [**list_jobs**](docs/SettingsApi.md#list_jobs) | **GET** /settings/jobs | Get scheduled jobs
*SettingsApi* | [**list_logs**](docs/SettingsApi.md#list_logs) | **GET** /settings/logs | Returns logs
*SettingsApi* | [**list_plex_devices_servers**](docs/SettingsApi.md#list_plex_devices_servers) | **GET** /settings/plex/devices/servers | Gets the user&#39;s available Plex servers
*SettingsApi* | [**list_plex_library**](docs/SettingsApi.md#list_plex_library) | **GET** /settings/plex/library | Get Plex libraries
*SettingsApi* | [**list_plex_users**](docs/SettingsApi.md#list_plex_users) | **GET** /settings/plex/users | Get Plex users
*SettingsApi* | [**list_radarr**](docs/SettingsApi.md#list_radarr) | **GET** /settings/radarr | Get Radarr settings
*SettingsApi* | [**list_radarr_profiles**](docs/SettingsApi.md#list_radarr_profiles) | **GET** /settings/radarr/{radarrId}/profiles | Get available Radarr profiles
*SettingsApi* | [**list_sonarr**](docs/SettingsApi.md#list_sonarr) | **GET** /settings/sonarr | Get Sonarr settings
*SettingsApi* | [**test_notifications_discord**](docs/SettingsApi.md#test_notifications_discord) | **POST** /settings/notifications/discord/test | Test Discord settings
*SettingsApi* | [**test_notifications_email**](docs/SettingsApi.md#test_notifications_email) | **POST** /settings/notifications/email/test | Test email settings
*SettingsApi* | [**test_notifications_gotify**](docs/SettingsApi.md#test_notifications_gotify) | **POST** /settings/notifications/gotify/test | Test Gotify settings
*SettingsApi* | [**test_notifications_lunasea**](docs/SettingsApi.md#test_notifications_lunasea) | **POST** /settings/notifications/lunasea/test | Test LunaSea settings
*SettingsApi* | [**test_notifications_pushbullet**](docs/SettingsApi.md#test_notifications_pushbullet) | **POST** /settings/notifications/pushbullet/test | Test Pushbullet settings
*SettingsApi* | [**test_notifications_pushover**](docs/SettingsApi.md#test_notifications_pushover) | **POST** /settings/notifications/pushover/test | Test Pushover settings
*SettingsApi* | [**test_notifications_slack**](docs/SettingsApi.md#test_notifications_slack) | **POST** /settings/notifications/slack/test | Test Slack settings
*SettingsApi* | [**test_notifications_telegram**](docs/SettingsApi.md#test_notifications_telegram) | **POST** /settings/notifications/telegram/test | Test Telegram settings
*SettingsApi* | [**test_notifications_webhook**](docs/SettingsApi.md#test_notifications_webhook) | **POST** /settings/notifications/webhook/test | Test webhook settings
*SettingsApi* | [**test_notifications_webpush**](docs/SettingsApi.md#test_notifications_webpush) | **POST** /settings/notifications/webpush/test | Test Web Push settings
*SettingsApi* | [**test_radarr**](docs/SettingsApi.md#test_radarr) | **POST** /settings/radarr/test | Test Radarr configuration
*SettingsApi* | [**test_sonarr**](docs/SettingsApi.md#test_sonarr) | **POST** /settings/sonarr/test | Test Sonarr configuration
*SettingsApi* | [**update_discover**](docs/SettingsApi.md#update_discover) | **PUT** /settings/discover/{sliderId} | Update a single slider
*SettingsApi* | [**update_radarr**](docs/SettingsApi.md#update_radarr) | **PUT** /settings/radarr/{radarrId} | Update Radarr instance
*SettingsApi* | [**update_sonarr**](docs/SettingsApi.md#update_sonarr) | **PUT** /settings/sonarr/{sonarrId} | Update Sonarr instance
*TmdbApi* | [**get_network_by_network_id**](docs/TmdbApi.md#get_network_by_network_id) | **GET** /network/{networkId} | Get TV network details
*TmdbApi* | [**get_studio_by_studio_id**](docs/TmdbApi.md#get_studio_by_studio_id) | **GET** /studio/{studioId} | Get movie studio details
*TmdbApi* | [**list_backdrops**](docs/TmdbApi.md#list_backdrops) | **GET** /backdrops | Get backdrops of trending items
*TmdbApi* | [**list_genres_movie**](docs/TmdbApi.md#list_genres_movie) | **GET** /genres/movie | Get list of official TMDB movie genres
*TmdbApi* | [**list_genres_tv**](docs/TmdbApi.md#list_genres_tv) | **GET** /genres/tv | Get list of official TMDB movie genres
*TmdbApi* | [**list_languages**](docs/TmdbApi.md#list_languages) | **GET** /languages | Languages supported by TMDB
*TmdbApi* | [**list_regions**](docs/TmdbApi.md#list_regions) | **GET** /regions | Regions supported by TMDB
*TvApi* | [**get_tv_by_tv_id**](docs/TvApi.md#get_tv_by_tv_id) | **GET** /tv/{tvId} | Get TV details
*TvApi* | [**get_tv_ratings**](docs/TvApi.md#get_tv_ratings) | **GET** /tv/{tvId}/ratings | Get TV ratings
*TvApi* | [**get_tv_recommendations**](docs/TvApi.md#get_tv_recommendations) | **GET** /tv/{tvId}/recommendations | Get recommended TV series
*TvApi* | [**get_tv_season_by_season_id**](docs/TvApi.md#get_tv_season_by_season_id) | **GET** /tv/{tvId}/season/{seasonId} | Get season details and episode list
*TvApi* | [**get_tv_similar**](docs/TvApi.md#get_tv_similar) | **GET** /tv/{tvId}/similar | Get similar TV series
*UsersApi* | [**create_auth_reset_password**](docs/UsersApi.md#create_auth_reset_password) | **POST** /auth/reset-password | Send a reset password email
*UsersApi* | [**create_auth_reset_password_by_guid**](docs/UsersApi.md#create_auth_reset_password_by_guid) | **POST** /auth/reset-password/{guid} | Reset the password for a user
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /user | Create new user
*UsersApi* | [**create_user_import_from_plex**](docs/UsersApi.md#create_user_import_from_plex) | **POST** /user/import-from-plex | Import all users from Plex
*UsersApi* | [**create_user_register_push_subscription**](docs/UsersApi.md#create_user_register_push_subscription) | **POST** /user/registerPushSubscription | Register a web push /user/registerPushSubscription
*UsersApi* | [**create_user_settings_main**](docs/UsersApi.md#create_user_settings_main) | **POST** /user/{userId}/settings/main | Update general settings for a user
*UsersApi* | [**create_user_settings_notifications**](docs/UsersApi.md#create_user_settings_notifications) | **POST** /user/{userId}/settings/notifications | Update notification settings for a user
*UsersApi* | [**create_user_settings_password**](docs/UsersApi.md#create_user_settings_password) | **POST** /user/{userId}/settings/password | Update password for a user
*UsersApi* | [**create_user_settings_permissions**](docs/UsersApi.md#create_user_settings_permissions) | **POST** /user/{userId}/settings/permissions | Update permission settings for a user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /user/{userId} | Delete user by ID
*UsersApi* | [**get_auth_me**](docs/UsersApi.md#get_auth_me) | **GET** /auth/me | Get logged-in user
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /user | Get all users
*UsersApi* | [**get_user_by_user_id**](docs/UsersApi.md#get_user_by_user_id) | **GET** /user/{userId} | Get user by ID
*UsersApi* | [**get_user_quota**](docs/UsersApi.md#get_user_quota) | **GET** /user/{userId}/quota | Get quotas for a specific user
*UsersApi* | [**get_user_requests**](docs/UsersApi.md#get_user_requests) | **GET** /user/{userId}/requests | Get requests for a specific user
*UsersApi* | [**get_user_settings_main**](docs/UsersApi.md#get_user_settings_main) | **GET** /user/{userId}/settings/main | Get general settings for a user
*UsersApi* | [**get_user_settings_notifications**](docs/UsersApi.md#get_user_settings_notifications) | **GET** /user/{userId}/settings/notifications | Get notification settings for a user
*UsersApi* | [**get_user_settings_password**](docs/UsersApi.md#get_user_settings_password) | **GET** /user/{userId}/settings/password | Get password page informatiom
*UsersApi* | [**get_user_settings_permissions**](docs/UsersApi.md#get_user_settings_permissions) | **GET** /user/{userId}/settings/permissions | Get permission settings for a user
*UsersApi* | [**get_user_watch_data**](docs/UsersApi.md#get_user_watch_data) | **GET** /user/{userId}/watch_data | Get watch data
*UsersApi* | [**get_user_watchlist**](docs/UsersApi.md#get_user_watchlist) | **GET** /user/{userId}/watchlist | Get the Plex watchlist for a specific user
*UsersApi* | [**list_plex_users**](docs/UsersApi.md#list_plex_users) | **GET** /settings/plex/users | Get Plex users
*UsersApi* | [**put_user**](docs/UsersApi.md#put_user) | **PUT** /user | Update batch of users
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /user/{userId} | Update a user by user ID


## Documentation For Models

 - [Cast](docs/Cast.md)
 - [Collection](docs/Collection.md)
 - [Company](docs/Company.md)
 - [CreateAuthLocalRequest](docs/CreateAuthLocalRequest.md)
 - [CreateAuthLogout200Response](docs/CreateAuthLogout200Response.md)
 - [CreateAuthPlexRequest](docs/CreateAuthPlexRequest.md)
 - [CreateAuthResetPasswordByGuidRequest](docs/CreateAuthResetPasswordByGuidRequest.md)
 - [CreateAuthResetPasswordRequest](docs/CreateAuthResetPasswordRequest.md)
 - [CreateDiscoverAddRequest](docs/CreateDiscoverAddRequest.md)
 - [CreateIssueCommentRequest](docs/CreateIssueCommentRequest.md)
 - [CreateIssueRequest](docs/CreateIssueRequest.md)
 - [CreateJobsScheduleRequest](docs/CreateJobsScheduleRequest.md)
 - [CreateMediaByStatusRequest](docs/CreateMediaByStatusRequest.md)
 - [CreatePlexSyncRequest](docs/CreatePlexSyncRequest.md)
 - [CreateRequestRequest](docs/CreateRequestRequest.md)
 - [CreateRequestRequestSeasons](docs/CreateRequestRequestSeasons.md)
 - [CreateUserImportFromPlexRequest](docs/CreateUserImportFromPlexRequest.md)
 - [CreateUserRegisterPushSubscriptionRequest](docs/CreateUserRegisterPushSubscriptionRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserSettingsMainRequest](docs/CreateUserSettingsMainRequest.md)
 - [CreateUserSettingsPasswordRequest](docs/CreateUserSettingsPasswordRequest.md)
 - [CreateUserSettingsPermissionsRequest](docs/CreateUserSettingsPermissionsRequest.md)
 - [CreditCast](docs/CreditCast.md)
 - [CreditCrew](docs/CreditCrew.md)
 - [Crew](docs/Crew.md)
 - [DiscordSettings](docs/DiscordSettings.md)
 - [DiscordSettingsOptions](docs/DiscordSettingsOptions.md)
 - [DiscoverSlider](docs/DiscoverSlider.md)
 - [Episode](docs/Episode.md)
 - [ExternalIds](docs/ExternalIds.md)
 - [Genre](docs/Genre.md)
 - [GetAbout200Response](docs/GetAbout200Response.md)
 - [GetCache200Response](docs/GetCache200Response.md)
 - [GetCache200ResponseApiCachesInner](docs/GetCache200ResponseApiCachesInner.md)
 - [GetCache200ResponseApiCachesInnerStats](docs/GetCache200ResponseApiCachesInnerStats.md)
 - [GetCache200ResponseImageCache](docs/GetCache200ResponseImageCache.md)
 - [GetCache200ResponseImageCacheTmdb](docs/GetCache200ResponseImageCacheTmdb.md)
 - [GetDiscoverMovies200Response](docs/GetDiscoverMovies200Response.md)
 - [GetDiscoverMoviesGenreByGenreId200Response](docs/GetDiscoverMoviesGenreByGenreId200Response.md)
 - [GetDiscoverMoviesLanguageByLanguage200Response](docs/GetDiscoverMoviesLanguageByLanguage200Response.md)
 - [GetDiscoverMoviesStudioByStudioId200Response](docs/GetDiscoverMoviesStudioByStudioId200Response.md)
 - [GetDiscoverTv200Response](docs/GetDiscoverTv200Response.md)
 - [GetDiscoverTvGenreByGenreId200Response](docs/GetDiscoverTvGenreByGenreId200Response.md)
 - [GetDiscoverTvLanguageByLanguage200Response](docs/GetDiscoverTvLanguageByLanguage200Response.md)
 - [GetDiscoverTvNetworkByNetworkId200Response](docs/GetDiscoverTvNetworkByNetworkId200Response.md)
 - [GetIssue200Response](docs/GetIssue200Response.md)
 - [GetIssueCount200Response](docs/GetIssueCount200Response.md)
 - [GetMedia200Response](docs/GetMedia200Response.md)
 - [GetMediaWatchData200Response](docs/GetMediaWatchData200Response.md)
 - [GetMediaWatchData200ResponseData](docs/GetMediaWatchData200ResponseData.md)
 - [GetMovieRatings200Response](docs/GetMovieRatings200Response.md)
 - [GetMovieRatingscombined200Response](docs/GetMovieRatingscombined200Response.md)
 - [GetMovieRatingscombined200ResponseImdb](docs/GetMovieRatingscombined200ResponseImdb.md)
 - [GetPersonCombinedCredits200Response](docs/GetPersonCombinedCredits200Response.md)
 - [GetPlexSync200Response](docs/GetPlexSync200Response.md)
 - [GetRequestCount200Response](docs/GetRequestCount200Response.md)
 - [GetSearch200Response](docs/GetSearch200Response.md)
 - [GetSearch200ResponseResultsInner](docs/GetSearch200ResponseResultsInner.md)
 - [GetSearchCompany200Response](docs/GetSearchCompany200Response.md)
 - [GetSearchKeyword200Response](docs/GetSearchKeyword200Response.md)
 - [GetServiceRadarrByRadarrId200Response](docs/GetServiceRadarrByRadarrId200Response.md)
 - [GetServiceSonarrBySonarrId200Response](docs/GetServiceSonarrBySonarrId200Response.md)
 - [GetStatus200Response](docs/GetStatus200Response.md)
 - [GetStatusAppdata200Response](docs/GetStatusAppdata200Response.md)
 - [GetTvRatings200Response](docs/GetTvRatings200Response.md)
 - [GetUser200Response](docs/GetUser200Response.md)
 - [GetUserQuota200Response](docs/GetUserQuota200Response.md)
 - [GetUserQuota200ResponseMovie](docs/GetUserQuota200ResponseMovie.md)
 - [GetUserRequests200Response](docs/GetUserRequests200Response.md)
 - [GetUserSettingsMain200Response](docs/GetUserSettingsMain200Response.md)
 - [GetUserSettingsPassword200Response](docs/GetUserSettingsPassword200Response.md)
 - [GetUserSettingsPermissions200Response](docs/GetUserSettingsPermissions200Response.md)
 - [GetUserWatchData200Response](docs/GetUserWatchData200Response.md)
 - [GetUserWatchlist200Response](docs/GetUserWatchlist200Response.md)
 - [GetUserWatchlist200ResponseResultsInner](docs/GetUserWatchlist200ResponseResultsInner.md)
 - [GotifySettings](docs/GotifySettings.md)
 - [GotifySettingsOptions](docs/GotifySettingsOptions.md)
 - [Issue](docs/Issue.md)
 - [IssueComment](docs/IssueComment.md)
 - [Job](docs/Job.md)
 - [Keyword](docs/Keyword.md)
 - [ListDiscoverGenresliderMovie200ResponseInner](docs/ListDiscoverGenresliderMovie200ResponseInner.md)
 - [ListGenresMovie200ResponseInner](docs/ListGenresMovie200ResponseInner.md)
 - [ListGenresTv200ResponseInner](docs/ListGenresTv200ResponseInner.md)
 - [ListLanguages200ResponseInner](docs/ListLanguages200ResponseInner.md)
 - [ListLogs200ResponseInner](docs/ListLogs200ResponseInner.md)
 - [ListPlexUsers200ResponseInner](docs/ListPlexUsers200ResponseInner.md)
 - [ListRegions200ResponseInner](docs/ListRegions200ResponseInner.md)
 - [LunaSeaSettings](docs/LunaSeaSettings.md)
 - [LunaSeaSettingsOptions](docs/LunaSeaSettingsOptions.md)
 - [MainSettings](docs/MainSettings.md)
 - [MediaInfo](docs/MediaInfo.md)
 - [MediaRequest](docs/MediaRequest.md)
 - [MediaRequestModifiedBy](docs/MediaRequestModifiedBy.md)
 - [MovieDetails](docs/MovieDetails.md)
 - [MovieDetailsCollection](docs/MovieDetailsCollection.md)
 - [MovieDetailsCredits](docs/MovieDetailsCredits.md)
 - [MovieDetailsProductionCountriesInner](docs/MovieDetailsProductionCountriesInner.md)
 - [MovieDetailsReleases](docs/MovieDetailsReleases.md)
 - [MovieDetailsReleasesResultsInner](docs/MovieDetailsReleasesResultsInner.md)
 - [MovieDetailsReleasesResultsInnerReleaseDatesInner](docs/MovieDetailsReleasesResultsInnerReleaseDatesInner.md)
 - [MovieResult](docs/MovieResult.md)
 - [Network](docs/Network.md)
 - [NotificationAgentTypes](docs/NotificationAgentTypes.md)
 - [NotificationEmailSettings](docs/NotificationEmailSettings.md)
 - [NotificationEmailSettingsOptions](docs/NotificationEmailSettingsOptions.md)
 - [PageInfo](docs/PageInfo.md)
 - [PersonDetails](docs/PersonDetails.md)
 - [PersonResult](docs/PersonResult.md)
 - [PersonResultKnownForInner](docs/PersonResultKnownForInner.md)
 - [PlexConnection](docs/PlexConnection.md)
 - [PlexDevice](docs/PlexDevice.md)
 - [PlexLibrary](docs/PlexLibrary.md)
 - [PlexSettings](docs/PlexSettings.md)
 - [ProductionCompany](docs/ProductionCompany.md)
 - [PublicSettings](docs/PublicSettings.md)
 - [PushbulletSettings](docs/PushbulletSettings.md)
 - [PushbulletSettingsOptions](docs/PushbulletSettingsOptions.md)
 - [PushoverSettings](docs/PushoverSettings.md)
 - [PushoverSettingsOptions](docs/PushoverSettingsOptions.md)
 - [PutUserRequest](docs/PutUserRequest.md)
 - [RadarrSettings](docs/RadarrSettings.md)
 - [RelatedVideo](docs/RelatedVideo.md)
 - [Season](docs/Season.md)
 - [ServarrTag](docs/ServarrTag.md)
 - [ServiceProfile](docs/ServiceProfile.md)
 - [SlackSettings](docs/SlackSettings.md)
 - [SlackSettingsOptions](docs/SlackSettingsOptions.md)
 - [SonarrSeries](docs/SonarrSeries.md)
 - [SonarrSeriesAddOptionsInner](docs/SonarrSeriesAddOptionsInner.md)
 - [SonarrSeriesImagesInner](docs/SonarrSeriesImagesInner.md)
 - [SonarrSeriesRatingsInner](docs/SonarrSeriesRatingsInner.md)
 - [SonarrSeriesSeasonsInner](docs/SonarrSeriesSeasonsInner.md)
 - [SonarrSettings](docs/SonarrSettings.md)
 - [SpokenLanguage](docs/SpokenLanguage.md)
 - [TautulliSettings](docs/TautulliSettings.md)
 - [TelegramSettings](docs/TelegramSettings.md)
 - [TelegramSettingsOptions](docs/TelegramSettingsOptions.md)
 - [TestRadarr200Response](docs/TestRadarr200Response.md)
 - [TestRadarrRequest](docs/TestRadarrRequest.md)
 - [TestSonarrRequest](docs/TestSonarrRequest.md)
 - [TvDetails](docs/TvDetails.md)
 - [TvDetailsContentRatings](docs/TvDetailsContentRatings.md)
 - [TvDetailsContentRatingsResultsInner](docs/TvDetailsContentRatingsResultsInner.md)
 - [TvDetailsCreatedByInner](docs/TvDetailsCreatedByInner.md)
 - [TvResult](docs/TvResult.md)
 - [UpdateDiscoverRequest](docs/UpdateDiscoverRequest.md)
 - [UpdateIssueCommentRequest](docs/UpdateIssueCommentRequest.md)
 - [UpdateRequestRequest](docs/UpdateRequestRequest.md)
 - [User](docs/User.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSettingsNotifications](docs/UserSettingsNotifications.md)
 - [WatchProviderDetails](docs/WatchProviderDetails.md)
 - [WatchProviderRegion](docs/WatchProviderRegion.md)
 - [WatchProvidersInner](docs/WatchProvidersInner.md)
 - [WebPushSettings](docs/WebPushSettings.md)
 - [WebhookSettings](docs/WebhookSettings.md)
 - [WebhookSettingsOptions](docs/WebhookSettingsOptions.md)


## Documentation For Authorization


## cookieAuth

- **Type**: API key
- **API key parameter name**: connect.sid
- **Location**: 


## apiKey

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## Author




