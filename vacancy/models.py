from django.db import models
from django.contrib.auth.models import User


class Meta:
    db_table = 'resume_resume'


# Create your models here.
class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, related_name='author_of_vac', on_delete=models.CASCADE)
