from django.shortcuts import render

# Create your views here.

from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields = ('name','text','answer')