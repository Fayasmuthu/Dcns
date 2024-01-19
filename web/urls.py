from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("service-detail/<slug:slug>/",views.ServiceDetailView.as_view(),name="service_detail"),
    path("updates/", views.UpdatesView.as_view(), name="updates"),
    path("updates-detail/<slug:slug>/",views.UpdatesDetailView.as_view(),name="updates_detail"),
    path("faq/", views.FaqView.as_view(), name="faq"),
    path("contact/", views.ContactView.as_view(), name="contact"),



]