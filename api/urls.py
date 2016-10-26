'''
Created on Aug 17, 2016

@author: ranjana wijerathne
'''
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
import api.apis as api

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'default_card', api.DefaultHealthCardStatesViewSet)
router.register(r'card', api.HealthCardViewSet)
router.register(r'states', api.HealthStateViewSet)
router.register(r'cardstates', api.HealthCardStatesViewSet)
router.register(r'participants', api.ParticipantViewSet)

admin_router = routers.SimpleRouter(trailing_slash=False)
admin_router.register(r'settings', api.AdminDefaultSettingsViewSet)
admin_router.register(r'card', api.AdminHealthCardViewSet)
admin_router.register(r'states', api.AdminHealthStateViewSet)
admin_router.register(r'cardstates', api.AdminHealthCardStatesViewSet)
admin_router.register(r'participants', api.AdminParticipantViewSet)


custom_router = routers.SimpleRouter(trailing_slash=False)
custom_router.register(r'states', api.HealthStateViewSet)

urlpatterns = [
               url(r'^survey/',include(router.urls)),
               url(r'^administrator/',include(admin_router.urls)),
               url(r'^survey/helth_card/(?P<param>[^/]+)/',include(custom_router.urls)),
               url(r'^login/$',api.Login.as_view()),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)