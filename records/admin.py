from django.contrib import admin

from . import models


class RecordInline(admin.TabularInline):
    model = models.Record


class CaseAdmin(admin.ModelAdmin):
    inlines = [RecordInline]


admin.site.register(models.UserAadhar)
admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.Document)
admin.site.register(models.Record)
admin.site.register(models.RecordACL)
admin.site.register(models.Test)
