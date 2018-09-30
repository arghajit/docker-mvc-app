from django.db import models
import json

class User(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
