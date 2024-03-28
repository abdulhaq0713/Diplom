from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import HomeUserChangeForm, HomeUserCretionForm
from .models import HomeUser
class HomeUserAdmin(UserAdmin):
    add_form = HomeUserCretionForm
    form = HomeUserChangeForm
    model= HomeUser
    list_display = ['username', 'first_name', 'last_name', "email", 'age',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',)}),
    )

admin.site.register(HomeUser, HomeUserAdmin)