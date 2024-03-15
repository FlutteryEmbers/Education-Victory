from django.db import models


class Problemnew(models.Model):
    title = models.TextField(max_length=2000, default='algorithm')
    remark = models.TextField(max_length=2000, default='algorithm')

    def __str__(self) -> str:
        return self.title


