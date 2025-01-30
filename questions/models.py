from django.db import models
DJANGO_SETTINGS_MODULE = 'AceMed.settings'
# Create your models here.
class question (models.Model):
    question_text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=1)
    subject = models.IntegerField(default=0)
    week = models.IntegerField(default=0)
    topic = models.CharField(max_length=200)