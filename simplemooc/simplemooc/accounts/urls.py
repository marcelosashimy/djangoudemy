
from django.urls import path , include
from django.contrib.auth.views import login
from simplemooc.accounts.views import register

#coloca sempre o nome do APP, para identificar de onde irá vim a url.
#Em outros lugares ficará por conta disso assim:  "APP":"URL" . EX: courses:details

app_name = 'accounts'
urlpatterns = [
	 path('entrar/', login,{'template_name':'accounts/login.html'}, name='login'),
	 path('cadastre-se/', register, name='register'),
]





#app_name = 'accounts'
#urlpatterns = [
#	 path('entrar/', include('django.contrib.auth.views.login'),{'template_name':'accounts/login.html'}, name='login'),
