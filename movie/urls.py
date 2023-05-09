from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('movie/<int:movie_id>', detail, name='detail'),
    path('movie/<int:movie_id>/create', createreview, name='createreview'),
    path('review/<int:review_id>', updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', deletereview, name='deletereview'),
]
