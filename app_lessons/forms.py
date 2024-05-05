from django.forms import ModelForm
from . import models


class LessonForm(ModelForm):
    class Meta:
        model = models.Lessons
        fields = '__all__'
