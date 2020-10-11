from django.contrib import admin
from .models import People
from phonenumber_field.modelfields import PhoneNumberInternationalFallbackWidget

# Register your models here.

admin.site.register(People)
class ModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.IntegerFeild: {'widget': PhoneNumberInternationalFallbackWidget},
    }
        exclude = ('id')