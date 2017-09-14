from django.contrib import admin
from docmanager.models import *
# Register your models here.

exclude_filter = ['ISBN','title','id']
class AuthorAdmin(admin.ModelAdmin):
	list_display_links = None
	list_display = ["first_name","last_name"]
	list_filter = ["first_name","last_name"]
	list_editable = ["first_name","last_name"]
class DocumentAdmin(admin.ModelAdmin):
	list_display_links = None
	list_display = [f.name for f in Document._meta.fields]
	list_filter = [f.name for f in Document._meta.fields \
	if not f.name in exclude_filter]
	list_editable = [f.name for f in Document._meta.fields]
admin.site.register(Document,DocumentAdmin)
admin.site.register(Author,AuthorAdmin)