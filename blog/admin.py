from django.contrib import admin
from .models import Post, Tag

#subclass to determine how the model is displayed 
class PostAdmin(admin.ModelAdmin): 
  # can also take exclude for example exclude = ["slug"], fields does exactly opposite of exclude , list_display 
  prepopulated_fields = {"slug": ("title", )} # updates slug field when title changes

  
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


