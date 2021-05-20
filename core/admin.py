from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(Top_news)
admin.site.register(Latest_release)
admin.site.register(Price_range)
admin.site.register(Deal_products)
admin.site.register(Flip_or_ama)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'slug', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', )
	search_fields = ('title', 'para')
	prepopulated_fields = {'slug': ('short_line_to_define',)}
	date_hierarchy = 'publish'
	ordering = ('status', '-publish')