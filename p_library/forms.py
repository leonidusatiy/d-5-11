from django import forms
from p_library.models import Author, Friend


class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class FriendForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'
