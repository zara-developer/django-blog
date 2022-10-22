"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


DOCS_TITLE="Blog API"
DOCS_DESCRIPTION="SomeThings"

sitemaps = {
    'posts':PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('api/v1/',include('blog.urls')),
    path('api-auth/',include('rest_framework.urls')),
    # url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/' , include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/' , include('rest_auth.registration.urls')),
    path('schema/',get_schema_view(DOCS_TITLE,DOCS_DESCRIPTION)),
    path('docs/',include_docs_urls(DOCS_TITLE,DOCS_DESCRIPTION)),
    path('swagger-docs/',get_swagger_view(DOCS_TITLE)),
]
