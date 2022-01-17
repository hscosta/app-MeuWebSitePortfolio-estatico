from . import *


class Category(models.Model):
    name = models.CharField(
        max_length=50,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
