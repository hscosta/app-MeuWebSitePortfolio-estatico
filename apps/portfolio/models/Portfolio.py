from . import *


class Portfolio(models.Model):
    image = models.ImageField(
        upload_to='portfolio/',
    )
    github = models.CharField(
        max_length=254, null=True,
    )
    link = models.CharField(
        max_length=254,
    )

    def __str__(self):
        return f'Portfolio {self.id}'
