from . import *


class Profile(models.Model):
    about = models.ForeignKey(
        About, on_delete=models.CASCADE,
    )
    social_name = models.CharField(
        max_length=20,
    )
    link = models.CharField(
        max_length=254,
    )
