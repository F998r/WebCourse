from django import forms
from .models import Books, Student,Address,Student2,Products

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


class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    name=forms.CharField(
        label='Student Name',
        required=True,
        max_length = 50,
        widget = forms.TextInput(
        attrs = {
        'placeholder' : 'Enter name of student'
             }
            )
     )

    age = forms.IntegerField(
        required=True,
        label = "Age",
        min_value = 7,
    )

    address = forms.CharField(
         max_length = 100
    )

class studentForm2(forms.ModelForm):
    class Meta:
        model=Student2
        fields=[ 'name' , 'age' , 'address2' ]

    name=forms.CharField(
        label='Student Name',
        required=True,
        max_length = 50,
        widget = forms.TextInput(
        attrs = {
            'placeholder' : 'Enter name of student'
            }
        )
    )

    age = forms.IntegerField(
        required=True,
        label = "Age",
        min_value = 10,
    )


    address2 = forms.ModelMultipleChoiceField(
        label="Address:",
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
    
    name = forms.CharField(
        label = 'Name of Product:',
        max_length = 50
    )

    desc = forms.CharField(
        label = 'Description:',
        max_length=100
    )

