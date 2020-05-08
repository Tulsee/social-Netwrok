from django.contrib import admin
from .models import UserDetail, UserSocialMedia, UserEducation


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user', )
    list_filter = ('user',)
    search_fields = ('user', )
    list_per_page = 15


class UserEducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)


admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(UserSocialMedia)
admin.site.register(UserEducation, UserEducationAdmin)
