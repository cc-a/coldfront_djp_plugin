import djp
from .urls import urlpatterns as plugin_urlpatterns

@djp.hookimpl
def installed_apps():
    # A list of app strings to add to INSTALLED_APPS:
    return ["coldfront_djp_plugin"]


@djp.hookimpl
def urlpatterns():
    # A list of URL patterns to add to urlpatterns:
    return plugin_urlpatterns


@djp.hookimpl
def settings(current_settings):
    # Make changes to the Django settings.py globals here
    current_settings["DJP_PLUGIN_VALUE"] = "I am a plugin settings value!"


@djp.hookimpl
def middleware():
    # A list of middleware class strings to add to MIDDLEWARE:
    # Wrap strings in djp.Before("middleware_class_name") or
    # djp.After("middleware_class_name") to specify before or after
    return []
