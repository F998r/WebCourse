from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'price', 'edition']

    title = forms.CharField(
        label="Title:",
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': "Enter title of book"}
        )
    )

    author = forms.CharField(
        label="Author:",
        max_length=50,
    )

    # Correct usage of FloatField
    price = forms.FloatField(
        label="Price:",
        initial=0.0,
        min_value=10,
        required=True
    )

    edition = forms.IntegerField(
        label="Edition:",
        required=True,
        min_value=1,
        initial=1
    )
