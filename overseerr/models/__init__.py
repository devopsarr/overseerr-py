# coding: utf-8

# flake8: noqa

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from overseerr.models.cast import Cast
from overseerr.models.collection import Collection
from overseerr.models.company import Company
from overseerr.models.create_auth_local_request import CreateAuthLocalRequest
from overseerr.models.create_auth_logout200_response import CreateAuthLogout200Response
from overseerr.models.create_auth_plex_request import CreateAuthPlexRequest
from overseerr.models.create_auth_reset_password_by_guid_request import CreateAuthResetPasswordByGuidRequest
from overseerr.models.create_auth_reset_password_request import CreateAuthResetPasswordRequest
from overseerr.models.create_discover_add_request import CreateDiscoverAddRequest
from overseerr.models.create_issue_comment_request import CreateIssueCommentRequest
from overseerr.models.create_issue_request import CreateIssueRequest
from overseerr.models.create_jobs_schedule_request import CreateJobsScheduleRequest
from overseerr.models.create_media_by_status_request import CreateMediaByStatusRequest
from overseerr.models.create_plex_sync_request import CreatePlexSyncRequest
from overseerr.models.create_request_request import CreateRequestRequest
from overseerr.models.create_request_request_seasons import CreateRequestRequestSeasons
from overseerr.models.create_user_import_from_plex_request import CreateUserImportFromPlexRequest
from overseerr.models.create_user_register_push_subscription_request import CreateUserRegisterPushSubscriptionRequest
from overseerr.models.create_user_request import CreateUserRequest
from overseerr.models.create_user_settings_main_request import CreateUserSettingsMainRequest
from overseerr.models.create_user_settings_password_request import CreateUserSettingsPasswordRequest
from overseerr.models.create_user_settings_permissions_request import CreateUserSettingsPermissionsRequest
from overseerr.models.credit_cast import CreditCast
from overseerr.models.credit_crew import CreditCrew
from overseerr.models.crew import Crew
from overseerr.models.discord_settings import DiscordSettings
from overseerr.models.discord_settings_options import DiscordSettingsOptions
from overseerr.models.discover_slider import DiscoverSlider
from overseerr.models.episode import Episode
from overseerr.models.external_ids import ExternalIds
from overseerr.models.genre import Genre
from overseerr.models.get_about200_response import GetAbout200Response
from overseerr.models.get_cache200_response import GetCache200Response
from overseerr.models.get_cache200_response_api_caches_inner import GetCache200ResponseApiCachesInner
from overseerr.models.get_cache200_response_api_caches_inner_stats import GetCache200ResponseApiCachesInnerStats
from overseerr.models.get_cache200_response_image_cache import GetCache200ResponseImageCache
from overseerr.models.get_cache200_response_image_cache_tmdb import GetCache200ResponseImageCacheTmdb
from overseerr.models.get_discover_movies200_response import GetDiscoverMovies200Response
from overseerr.models.get_discover_movies_genre_by_genre_id200_response import GetDiscoverMoviesGenreByGenreId200Response
from overseerr.models.get_discover_movies_language_by_language200_response import GetDiscoverMoviesLanguageByLanguage200Response
from overseerr.models.get_discover_movies_studio_by_studio_id200_response import GetDiscoverMoviesStudioByStudioId200Response
from overseerr.models.get_discover_tv200_response import GetDiscoverTv200Response
from overseerr.models.get_discover_tv_genre_by_genre_id200_response import GetDiscoverTvGenreByGenreId200Response
from overseerr.models.get_discover_tv_language_by_language200_response import GetDiscoverTvLanguageByLanguage200Response
from overseerr.models.get_discover_tv_network_by_network_id200_response import GetDiscoverTvNetworkByNetworkId200Response
from overseerr.models.get_issue200_response import GetIssue200Response
from overseerr.models.get_issue_count200_response import GetIssueCount200Response
from overseerr.models.get_media200_response import GetMedia200Response
from overseerr.models.get_media_watch_data200_response import GetMediaWatchData200Response
from overseerr.models.get_media_watch_data200_response_data import GetMediaWatchData200ResponseData
from overseerr.models.get_movie_ratings200_response import GetMovieRatings200Response
from overseerr.models.get_movie_ratingscombined200_response import GetMovieRatingscombined200Response
from overseerr.models.get_movie_ratingscombined200_response_imdb import GetMovieRatingscombined200ResponseImdb
from overseerr.models.get_person_combined_credits200_response import GetPersonCombinedCredits200Response
from overseerr.models.get_plex_sync200_response import GetPlexSync200Response
from overseerr.models.get_request_count200_response import GetRequestCount200Response
from overseerr.models.get_search200_response import GetSearch200Response
from overseerr.models.get_search200_response_results_inner import GetSearch200ResponseResultsInner
from overseerr.models.get_search_company200_response import GetSearchCompany200Response
from overseerr.models.get_search_keyword200_response import GetSearchKeyword200Response
from overseerr.models.get_service_radarr_by_radarr_id200_response import GetServiceRadarrByRadarrId200Response
from overseerr.models.get_service_sonarr_by_sonarr_id200_response import GetServiceSonarrBySonarrId200Response
from overseerr.models.get_status200_response import GetStatus200Response
from overseerr.models.get_status_appdata200_response import GetStatusAppdata200Response
from overseerr.models.get_tv_ratings200_response import GetTvRatings200Response
from overseerr.models.get_user200_response import GetUser200Response
from overseerr.models.get_user_quota200_response import GetUserQuota200Response
from overseerr.models.get_user_quota200_response_movie import GetUserQuota200ResponseMovie
from overseerr.models.get_user_requests200_response import GetUserRequests200Response
from overseerr.models.get_user_settings_main200_response import GetUserSettingsMain200Response
from overseerr.models.get_user_settings_password200_response import GetUserSettingsPassword200Response
from overseerr.models.get_user_settings_permissions200_response import GetUserSettingsPermissions200Response
from overseerr.models.get_user_watch_data200_response import GetUserWatchData200Response
from overseerr.models.get_user_watchlist200_response import GetUserWatchlist200Response
from overseerr.models.get_user_watchlist200_response_results_inner import GetUserWatchlist200ResponseResultsInner
from overseerr.models.gotify_settings import GotifySettings
from overseerr.models.gotify_settings_options import GotifySettingsOptions
from overseerr.models.issue import Issue
from overseerr.models.issue_comment import IssueComment
from overseerr.models.job import Job
from overseerr.models.keyword import Keyword
from overseerr.models.list_discover_genreslider_movie200_response_inner import ListDiscoverGenresliderMovie200ResponseInner
from overseerr.models.list_genres_movie200_response_inner import ListGenresMovie200ResponseInner
from overseerr.models.list_genres_tv200_response_inner import ListGenresTv200ResponseInner
from overseerr.models.list_languages200_response_inner import ListLanguages200ResponseInner
from overseerr.models.list_logs200_response_inner import ListLogs200ResponseInner
from overseerr.models.list_notifications_pushover_sounds200_response_inner import ListNotificationsPushoverSounds200ResponseInner
from overseerr.models.list_plex_users200_response_inner import ListPlexUsers200ResponseInner
from overseerr.models.list_regions200_response_inner import ListRegions200ResponseInner
from overseerr.models.luna_sea_settings import LunaSeaSettings
from overseerr.models.luna_sea_settings_options import LunaSeaSettingsOptions
from overseerr.models.main_settings import MainSettings
from overseerr.models.media_info import MediaInfo
from overseerr.models.media_request import MediaRequest
from overseerr.models.media_request_modified_by import MediaRequestModifiedBy
from overseerr.models.movie_details import MovieDetails
from overseerr.models.movie_details_collection import MovieDetailsCollection
from overseerr.models.movie_details_credits import MovieDetailsCredits
from overseerr.models.movie_details_production_countries_inner import MovieDetailsProductionCountriesInner
from overseerr.models.movie_details_releases import MovieDetailsReleases
from overseerr.models.movie_details_releases_results_inner import MovieDetailsReleasesResultsInner
from overseerr.models.movie_details_releases_results_inner_release_dates_inner import MovieDetailsReleasesResultsInnerReleaseDatesInner
from overseerr.models.movie_result import MovieResult
from overseerr.models.network import Network
from overseerr.models.notification_agent_types import NotificationAgentTypes
from overseerr.models.notification_email_settings import NotificationEmailSettings
from overseerr.models.notification_email_settings_options import NotificationEmailSettingsOptions
from overseerr.models.page_info import PageInfo
from overseerr.models.person_details import PersonDetails
from overseerr.models.person_result import PersonResult
from overseerr.models.person_result_known_for_inner import PersonResultKnownForInner
from overseerr.models.plex_connection import PlexConnection
from overseerr.models.plex_device import PlexDevice
from overseerr.models.plex_library import PlexLibrary
from overseerr.models.plex_settings import PlexSettings
from overseerr.models.production_company import ProductionCompany
from overseerr.models.public_settings import PublicSettings
from overseerr.models.pushbullet_settings import PushbulletSettings
from overseerr.models.pushbullet_settings_options import PushbulletSettingsOptions
from overseerr.models.pushover_settings import PushoverSettings
from overseerr.models.pushover_settings_options import PushoverSettingsOptions
from overseerr.models.put_user_request import PutUserRequest
from overseerr.models.radarr_settings import RadarrSettings
from overseerr.models.related_video import RelatedVideo
from overseerr.models.season import Season
from overseerr.models.servarr_tag import ServarrTag
from overseerr.models.service_profile import ServiceProfile
from overseerr.models.slack_settings import SlackSettings
from overseerr.models.slack_settings_options import SlackSettingsOptions
from overseerr.models.sonarr_series import SonarrSeries
from overseerr.models.sonarr_series_add_options_inner import SonarrSeriesAddOptionsInner
from overseerr.models.sonarr_series_images_inner import SonarrSeriesImagesInner
from overseerr.models.sonarr_series_ratings_inner import SonarrSeriesRatingsInner
from overseerr.models.sonarr_series_seasons_inner import SonarrSeriesSeasonsInner
from overseerr.models.sonarr_settings import SonarrSettings
from overseerr.models.spoken_language import SpokenLanguage
from overseerr.models.tautulli_settings import TautulliSettings
from overseerr.models.telegram_settings import TelegramSettings
from overseerr.models.telegram_settings_options import TelegramSettingsOptions
from overseerr.models.test_radarr200_response import TestRadarr200Response
from overseerr.models.test_radarr_request import TestRadarrRequest
from overseerr.models.test_sonarr_request import TestSonarrRequest
from overseerr.models.tv_details import TvDetails
from overseerr.models.tv_details_content_ratings import TvDetailsContentRatings
from overseerr.models.tv_details_content_ratings_results_inner import TvDetailsContentRatingsResultsInner
from overseerr.models.tv_details_created_by_inner import TvDetailsCreatedByInner
from overseerr.models.tv_result import TvResult
from overseerr.models.update_discover_request import UpdateDiscoverRequest
from overseerr.models.update_issue_comment_request import UpdateIssueCommentRequest
from overseerr.models.update_request_request import UpdateRequestRequest
from overseerr.models.user import User
from overseerr.models.user_settings import UserSettings
from overseerr.models.user_settings_notifications import UserSettingsNotifications
from overseerr.models.watch_provider_details import WatchProviderDetails
from overseerr.models.watch_provider_region import WatchProviderRegion
from overseerr.models.watch_providers_inner import WatchProvidersInner
from overseerr.models.web_push_settings import WebPushSettings
from overseerr.models.webhook_settings import WebhookSettings
from overseerr.models.webhook_settings_options import WebhookSettingsOptions
