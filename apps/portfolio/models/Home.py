from . import *


class Home(models.Model):
    name = models.CharField(
        max_length=100,
    )
    greettings_1 = models.CharField(
        max_length=10,
    )
    greettings_2 = models.CharField(
        max_length=10,
    )
    picture = models.ImageField(
        upload_to='picture/',
    )
    email = models.EmailField(
        null=True,
    )
    phone = models.CharField(
        max_length=20, null=True,
    )
    address = models.CharField(
        max_length=30, null=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
