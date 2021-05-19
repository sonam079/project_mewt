from django.db import models


# Create your models here.
class Emails(models.Model):
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = 'emails'
