from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form, EmailInput, TextInput, PasswordInput, FileField, ClearableFileInput
from django.contrib.auth import password_validation
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name')

        widgets = {'email':EmailInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Email'}),
                   'name':TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Name'}),
                   'password1':PasswordInput(attrs={'class':'form-control', 'required':True, 'autocomplete':False, 'placeholder':'Password', 'help_text':password_validation.password_validators_help_text_html()}),
                   'password2':PasswordInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Password Confirmation'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadFileForm(Form):
    files = MultipleFileField()