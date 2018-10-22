from django import forms
from grumblr.models import *
import datetime

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'image' : forms.FileInput(),
                   'text' : forms.Textarea()}
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'post_box', 'placeholder':'Less than 42 characters...'})
        self.fields['text'].widget.attrs.update({'id': 'text'})
        self.fields['image'].widget.attrs.update({'class': 'image_select'})
    def clean_text(self):
        cleaned_data = super(PostForm, self).clean()
        text = cleaned_data.get('text')
        if text and len(text) > 42:
            raise forms.ValidationError("Post should be less than 42 characters!\
                                        (delete this message to continue)")
        return text
