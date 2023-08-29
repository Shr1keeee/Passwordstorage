from django.db import models

import datetime

class PasswordStorage(models.Model):
    title_storage = models.CharField(max_length=150, null=False, blank=False)
    user_password = models.CharField(max_length=150, null=False, blank=False)
    discription = models.TextField(max_length=150, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title_storage