from django import forms

from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 200,
                               label = 'Username')
    first_name = forms.CharField(max_length = 200,
                                 label='First Name')
    last_name = forms.CharField(max_length = 200,
                                label = 'Last Name')
    password = forms.CharField(max_length = 200,
                                label='Password',
                                widget = forms.PasswordInput())
    confirm_password = forms.CharField(max_length = 200,
                                label='Confirm password',
                                widget = forms.PasswordInput())
    email = forms.EmailField(max_length=200,
                             label='Email',
                             widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # self.fields['username'].error_messages = {'required': 'username required'}
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} cannot be empty!'.format(
                fieldname=field.label)}
            field.widget.attrs.update({'class': 'input-text'})
        # self.fields['username'].widget.attrs.update({'class': 'input-text'})

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Confirm password does not match!")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")
        return username



