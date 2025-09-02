# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from overseerr.api.auth_api import AuthApi
    from overseerr.api.collection_api import CollectionApi
    from overseerr.api.issue_api import IssueApi
    from overseerr.api.media_api import MediaApi
    from overseerr.api.movies_api import MoviesApi
    from overseerr.api.other_api import OtherApi
    from overseerr.api.person_api import PersonApi
    from overseerr.api.public_api import PublicApi
    from overseerr.api.request_api import RequestApi
    from overseerr.api.search_api import SearchApi
    from overseerr.api.service_api import ServiceApi
    from overseerr.api.settings_api import SettingsApi
    from overseerr.api.tmdb_api import TmdbApi
    from overseerr.api.tv_api import TvApi
    from overseerr.api.users_api import UsersApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from overseerr.api.auth_api import AuthApi
from overseerr.api.collection_api import CollectionApi
from overseerr.api.issue_api import IssueApi
from overseerr.api.media_api import MediaApi
from overseerr.api.movies_api import MoviesApi
from overseerr.api.other_api import OtherApi
from overseerr.api.person_api import PersonApi
from overseerr.api.public_api import PublicApi
from overseerr.api.request_api import RequestApi
from overseerr.api.search_api import SearchApi
from overseerr.api.service_api import ServiceApi
from overseerr.api.settings_api import SettingsApi
from overseerr.api.tmdb_api import TmdbApi
from overseerr.api.tv_api import TvApi
from overseerr.api.users_api import UsersApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
