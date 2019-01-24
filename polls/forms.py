from django.forms import ModelForm
from .models import Question

class QuestionModelForm(ModelForm):
    class Meta:
        model = Question
        fields = ['id']
