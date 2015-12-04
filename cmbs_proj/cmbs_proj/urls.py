"""cmbs_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cmbs.views import MainView, AllView, DealView, LoanView, PropertyView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^all/', AllView.as_view(), name='all'),
    url(r'^deal_search/(?P<term>[\w]+)', DealView.as_view(), name='dealsearch'),
    url(r'^loan_search/(?P<term>[\w]+)', LoanView.as_view(), name='loansearch'),
    url(r'^property_search/(?P<term>[\w]+)', PropertyView.as_view(), name='propertysearch')
]
