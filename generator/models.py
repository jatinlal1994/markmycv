from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    template_name = models.CharField(max_length = 200)
    data = models.TextField(blank=True, null=True)
    hashcode = models.CharField(max_length = 40)

    def __str__(self):
        return self.user_id.username + ' :: ' + self.template_name + ' :: ' + self.hashcode