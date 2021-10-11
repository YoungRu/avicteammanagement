from django.forms import ModelForm
from django import forms
from .models import UserReg, Signin, Todo
import datetime

class UserForm(ModelForm):
    class Meta:
        model = UserReg
        fields = ['Username', 'Email', 'Password', 'Password2', 'Birthday', 'Position']
        startyear = 1900
        thisyear = datetime.date.today().year
        print(thisyear)
        i = 0
        BIRTH_YEAR_CHOICES = []
        for i in range(int(thisyear)-int(startyear)):
            i += 1
            startyear += 1
            BIRTH_YEAR_CHOICES.append(str(startyear))

        widgets = {
                'Birthday': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES ),
        }


class SigninForm(ModelForm):
    class Meta:
        model = Signin
        fields = ['Username', 'Password']

        widgets = {
            'Username':forms.Textarea(attrs={'class':'form-control','rows': 1}),
            'Password': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})
        }



class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['Work', 'Description','Assign', 'File']


        widgets = {
            'Work': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'Assign': forms.CheckboxSelectMultiple(attrs={
                "class": "column-checkbox"
            })
        }
        # Assign = forms.ModelMultipleChoiceField(queryset=UserReg.objects.all(),widget=forms.CheckboxSelectMultiple)


# a = 'hello world'
# b = 'hi world'
# tuple = (a,b)
# list = []
# print(type(a))
# print(type(tuple))
# list.append(tuple)
# print(list)