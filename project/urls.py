from rest_framework import routers
from .api import projectviewset

routers = routers.DefaultRouter()

routers.register('api/project', projectviewset, 'project')

urlpatterns = routers.urls
