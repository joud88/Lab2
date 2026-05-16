from django import forms
from .models import Book, Student, Publisher, Author, Address, Student2, Address2, Course

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher', 'authors']

        widgets = {
            'pubdate': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'authors': forms.CheckboxSelectMultiple(),
        }

    pubdate = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        )
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = '__all__'


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ='__all__'