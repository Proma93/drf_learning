from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'', TodoModelViewSet, basename='todo')

urlpatterns = [
#    path('', home, name='home'),
#    path('get-todo/', get_todo, name='get_todo'),
#    path('post-todo/', post_todo, name='post_todo'),
#    path('patch-todo/<uuid:uid>/', patch_todo, name='patch_todo'),

#    path('', HomeView.as_view(), name='home'),
#    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
#    path('todos/<uuid:uid>/', TodoUpdateView.as_view(), name='todo-update'),

    path('modelviewset/', include(router.urls)),
]