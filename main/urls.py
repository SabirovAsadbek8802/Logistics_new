from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', TemplateView.as_view(template_name="faq.html"), name="faq"),
    path('blog/', TemplateView.as_view(template_name="news.html"), name="blog"),
    path('blog/<int:pk>/', TemplateView.as_view(template_name="news-details.html"), name="blog-detail"),
    path('blog/<int:pk>/', TemplateView.as_view(template_name="news-details.html"), name="blog-detail"),
    path('services/', TemplateView.as_view(template_name="services.html"), name="services"),
]
