from django.db import models

# Create your models here.
class Log(models.Model):
    q = models.CharField(max_length=200)
    a = models.CharField(max_length=200)

    class Meta:
        db_table = 'Chat_Log'
        verbose_name = 'log'
        verbose_name_plural = 'log'