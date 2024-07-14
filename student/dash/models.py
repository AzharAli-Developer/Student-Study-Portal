from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    discription=models.CharField(max_length=128)

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"


class Homework(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=28)
    title=models.CharField(max_length=128)
    discription=models.CharField(max_length=128)
    due=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    status=models.BooleanField(default=False)


    class Meta:
        verbose_name="todo"
        verbose_name_plural="todo"
