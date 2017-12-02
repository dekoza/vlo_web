from rest_framework import routers
from news.views import EntryViewSet

v1 = routers.DefaultRouter()

v1.register('entries', EntryViewSet)
