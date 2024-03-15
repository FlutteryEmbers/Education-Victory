from django.db import models

def get_default_json():
    return {}

class Questionnew(models.Model):
    title = models.TextField(max_length=20000)
    type = models.IntegerField(default=0)
    problem = models.ForeignKey('problemnew.Problemnew', on_delete=models.CASCADE)
    payload = models.JSONField(default=get_default_json)
    stage = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title
