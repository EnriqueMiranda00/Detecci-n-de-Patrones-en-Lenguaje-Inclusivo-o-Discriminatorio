
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from .models import Profile
from .signals import ADMIN_GROUP, USER_GROUP

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombres_completos = forms.CharField(label="Nombres completos", max_length=150)
    rol = forms.ChoiceField(choices=[(ADMIN_GROUP, 'Administrador'), (USER_GROUP, 'Usuario')], initial=USER_GROUP)

    class Meta:
        model = User
        fields = ('username', 'email', 'nombres_completos', 'rol', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        rol = self.cleaned_data['rol']
        user.is_staff = (rol == ADMIN_GROUP)
        if commit:
            user.save()
            profile = user.profile
            profile.nombres_completos = self.cleaned_data['nombres_completos']
            profile.save()
            user.groups.clear()
            group = Group.objects.get(name=rol)
            user.groups.add(group)
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    nombres_completos = forms.CharField(max_length=150)
    is_active = forms.BooleanField(required=False, label='Activo')
    rol = forms.ChoiceField(choices=[(ADMIN_GROUP, 'Administrador'), (USER_GROUP, 'Usuario')])

    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'rol')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres_completos'].initial = self.instance.profile.nombres_completos
        self.fields['rol'].initial = ADMIN_GROUP if self.instance.groups.filter(name=ADMIN_GROUP).exists() else USER_GROUP

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        rol = self.cleaned_data['rol']
        user.is_staff = (rol == ADMIN_GROUP)
        if commit:
            user.save()
            profile = user.profile
            profile.nombres_completos = self.cleaned_data['nombres_completos']
            profile.save()
            user.groups.clear()
            group = Group.objects.get(name=rol)
            user.groups.add(group)
        return user
