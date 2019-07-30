
from django.urls import path
from simplemooc.courses.views import courses , details

#coloca sempre o nome do APP, para identificar de onde irá vim a url.
#Em outros lugares ficará por conta disso assim:  "APP":"URL" . EX: courses:details

app_name = 'courses'
urlpatterns = [

    path('', courses, name='courses'),
    #path(r'(?P)<pk>\d+)',details, name='details')
    #path('<int:pk>/', details, name='details'),
    path('<slug:slug>/', details, name='details'),
]
