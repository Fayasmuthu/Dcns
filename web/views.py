from django.db.models import Min, Q
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# form
from web.forms import ContactForm
from web.forms import EnquiryForm
# Model
from web.models import Service
from web.models import Updates
from web.models import Faq
from web.models import Client
from web.models import Testimonial


class IndexView(TemplateView):
    template_name = "web/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_index"] = True
        context["client"] = Client.objects.all()
        context["testimonials"] = Testimonial.objects.all()     
        return context
    

class AboutView(TemplateView):
    template_name = "web/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faq = Faq.objects.all()
        context["faq"] = faq
        context["is_about"] = True
        return context


class ServicesView(View):
    def get(self, request):
        services = Service.objects.filter(is_service=True)

        context = {
            "is_service": True,
            "services": services,
        }
        return render(request, "web/services.html", context)

    
class ServiceDetailView(DetailView):
    model = Service
    template_name = "web/services_detail.html"
    context_object_name = 'services'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
    
    def post(self, request, *args, **kwargs):
        form = EnquiryForm(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully Submitted",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return JsonResponse(response_data)


class UpdatesView(View):
    def get(self, request):

        updates = Updates.objects.filter(is_updates=True)

        context = {
            "is_updates": True,
            "updates": updates,
        }
        return render(request, "web/updates.html", context)  


class UpdatesDetailView(DetailView):
    model = Updates
    template_name = "web/updates-details.html"
    context_object_name = 'updates'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class FaqView(View):
    def get(self, request):
        faq = Faq.objects.all()
        context = {
            "is_faq": True,
            "faq" : faq,

        }      
        return render(request, "web/faq.html", context)
    

class ContactView(View):
    def get(self, request):
        form = ContactForm
        context = {
            "is_contact": True,
            "form": form,

        }      
        return render(request, "web/contact.html", context)
       
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully Submitted",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return JsonResponse(response_data)