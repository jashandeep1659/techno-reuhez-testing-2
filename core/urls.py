from django.urls import path
from . import views


urlpatterns = [
	path('',views.home , name="home"),
	path('<slug:slug>/<int:id>/',views.detail_view , name="detail_view"),
	path('add_news/',views.add_news, name="add_news"),
	path('add_deal/',views.add_deal, name="add_deal"),
	path('offers/',views.all_deals, name="all_deals"),
	path('add_phone/',views.add_phone, name="add_phone"),
	path('tech_news/',views.post_list_all, name="post_list_all"),
	path('tech_news/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
]