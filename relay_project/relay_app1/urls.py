from django.urls import path
from .views import *

app_name= 'firstapp'
urlpatterns = [
    path('', services, name="service"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('blog_single/', blog_single, name="blog_single"),
    path('contact/', contact, name="contact"),
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio_single/', portfolio_single, name="portfolio_single"),
]