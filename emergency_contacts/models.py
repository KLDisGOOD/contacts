from django.db import models

#Main model
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.phone_number