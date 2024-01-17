from django.contrib import admin
from .models import Contact,Service,Faq,Enquiryform
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Contact)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_preview" ,"name", "is_service")
    exclude = ("creator",)
    prepopulated_fields = {"slug": ("name",)}

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:50px;height:50px;object-fit:contain;">'
            )
        return None
    
    image_preview.short_description = "Image Preview"


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("title", )
    exclude = ("creator",)

class EnquiryformAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name" )
    readonly_fields = ['services']

admin.site.register(Enquiryform, EnquiryformAdmin)
