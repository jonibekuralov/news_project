from django.urls import path
from django.views.generic import TemplateView

from .views import news_list, news_detail, ContactPageView, homePageView, \
    LocalNewsView, SportNewsView, WorldNewsView, IqtisodNewsView, SubjectNewsView


urlpatterns = [
    path('', homePageView.as_view(), name="home"),
    path('news/', news_list, name="news_all"),
    path('news/<slug:news>/',news_detail, name="news_detail_page"),
    path('contact/', ContactPageView.as_view(), name="contact-us"),
    path('about/', TemplateView.as_view(template_name="news/about.html"), name="about-us"),
    path('local/',LocalNewsView.as_view(template_name="news/local.html"), name="local-news"),
    path('world/', WorldNewsView.as_view(template_name="news/world.html"), name="world-news"),
    path('fan/', SubjectNewsView.as_view(template_name="news/fan.html"), name="fan-news"),
    path('sport/', SportNewsView.as_view(template_name="news/sport.html"), name="sport-news"),
    path('iqtisodiyot/', IqtisodNewsView.as_view(template_name="news/iqtisodiyot.html"), name="iqtisod-news"),
]