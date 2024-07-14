from django import forms
from .models import Notes,Homework,Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registeration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']


class stuNotes(forms.ModelForm):
    class Meta:
        model=Notes
        fields='__all__'



class stuHomework(forms.ModelForm):
    class Meta:
        model=Homework
        fields='__all__'



class studyform(forms.Form):
    text=forms.CharField(max_length=128)



class todoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'



class ConversionForm(forms.Form):
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES=[('yard','Yard'),('foot','Foot')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the number'}
    ))
    measure1=forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )



class ConversionMassForm(forms.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the number'}
    ))
    measure1=forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )