from django.db import models


class Logins(models.Model):
    login = models.CharField(max_length=255, unique=True, null=False)
    password = models.BinaryField(null=False)

    def __str__(self):
        return f"{self.id} {self.login} {self.password}"

class Worker(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} " \
               f"{self.firstname} " \
               f"{self.lastname} " \
               f"{self.profession} " \
               f"{self.birth_date} " \
               f"{self.phone_number} " \
               f"{self.e_mail}"