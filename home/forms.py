from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import HomeUser


class HomeUserCretionForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = HomeUser
        fields =  ('username', 'first_name', 'last_name', "email", 'age',)
class HomeUserChangeForm(UserChangeForm):
    class Meta:
        model = HomeUser
        fields = ('username', 'first_name', 'last_name', "email", 'age',)