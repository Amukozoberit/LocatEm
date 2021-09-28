from django.urls import path
from .views import home, prof
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.home, name='index'),
    
    path('biz/<str:id>/',views.biz,name='biz'),
    path('profile',views.update_profile,name='profile'),
    path('prof/<str:id>/',views.prof,name='prof'),
    path('search',views.search_results,name='search'),
    path('createPost',views.create_post,name='createPost'),
    path('news', views.news,name='news'),
    path('createHood',views.create_neiba,name='createHood'),
    path('delHood/<str:name>',views.delHood,name='delHood'),
    path('neibahood',views.neibas,name='neibaHood'),
    path('users',views.users,name='users'),
    path('updateHood/<str:id>',views.update_Neibas,name='updateHood'),
    path('updateoCC/<str:id>',views.update_Occupants,name='updateoCC'),
    path('createnews/',views.create_news,name='createnews'),
    path('deletebiz/<str:id>',views.deletebiz,name='deletebiz'),
    path('updatebiz/<str:id>',views.updatebiz,name='updatebiz'),
]