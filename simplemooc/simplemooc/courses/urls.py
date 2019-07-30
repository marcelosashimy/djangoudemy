
from django.urls import path
from simplemooc.courses.views import courses , details



urlpatterns = [

    path('', courses,name='courses'),
    #path(r'(?P)<pk>\d+)',details, name='details')
    path('<int:pk>/', details, name='details'),

]
