from django.urls import path
from storyapp.apis import GetAllStoriesAPI, AddStoryAPI, IndividualStoryAPI


urlpatterns = [
    path('', IndividualStoryAPI.as_view(), name='single_story'),
    path('all/', GetAllStoriesAPI.as_view(), name='all_stories'),
    path('add/', AddStoryAPI.as_view(), name='new_story'),    
]