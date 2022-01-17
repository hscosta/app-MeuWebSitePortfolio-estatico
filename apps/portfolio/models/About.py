from . import *


class About(models.Model):
    heading = models.CharField(
        max_length=100,
    )
    career = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        blank=False,
    )
    profile_img = models.ImageField(
        upload_to='media/profile/',
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.career
