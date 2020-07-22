from django.contrib import admin
from .models import UserProfile, ContactUs, Employee, About, news, category, subcategory, Comment
# customisation admin side


class UserProfileAdmin(admin.ModelAdmin):
    # display this data admin side
    list_display = ('user', 'age', 'gender', 'image')


# registerd userprofile model in admin side
admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('newsarticle', 'reporters', 'awardswon', 'yearold')


admin.site.register(About, AboutAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'positions', 'image')


admin.site.register(Employee, EmployeeAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(ContactUs, ContactUsAdmin)

admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(news)
admin.site.register(Comment)