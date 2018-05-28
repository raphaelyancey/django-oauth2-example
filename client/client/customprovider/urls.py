from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import CustomProvider

urlpatterns = default_urlpatterns(CustomProvider)
