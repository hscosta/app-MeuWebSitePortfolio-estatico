from . import *


class Skills(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
    )
    skill_name = models.CharField(
        max_length=50,
    )
