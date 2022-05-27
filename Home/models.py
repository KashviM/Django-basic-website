from django.db import models

# make migrations: create changes and store in file
# migrate: apply pending changes created by create migations
# Create your models here
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    
    def __str__(self):
      return self.name

    

