from django.db import models
from django.urls import reverse


# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = (('do_zrobienia', 'Do_zrobienia'), ('w_trakcie', 'W_trakcie'), ('zrobione','Zrobione'))
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='do_zrobienia')

    object = models.Manager()
    class Meta:
        ordering=('-title',)

    def __str__(self):
        return self.title
