from django import forms
from profiles.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {'image' : forms.FileInput(),
                   'bio' : forms.Textarea()}
        fields = ['first_name', 'last_name', 'age', 'bio', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['username'].error_messages = {'required': 'username required'}
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} cannot be empty!'.format(
                fieldname=field.label)}
            field.widget.attrs.update({'class': 'input-text'})
        self.fields['bio'].widget.attrs.update({'class': 'bio-box'})
        self.fields['image'].widget.attrs.update({'class': 'image_select'})

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age:
            if age < 0 or age > 100:
                raise forms.ValidationError("Invalid age.")
        return age
