from django.db import models

from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=500)     
    slug = models.SlugField(max_length=500)
    image = models.ImageField(upload_to="updates/")
    description = RichTextField(blank=True, null=True)
    is_service = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    is_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "service"
        verbose_name_plural = "services"

    def get_absolute_url(self):
        return reverse("web:service_detail", kwargs={"slug": self.slug})
    
    def _str_(self):
        return self.name


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
    )
    message = models.TextField()
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return str(self.full_name())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()

    def _str_(self):
        return self.title
    

class Enquiryform(models.Model):
    services = models.CharField(max_length=100,editable=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.services}  "
