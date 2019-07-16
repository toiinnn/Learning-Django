from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name = 'index'),
]