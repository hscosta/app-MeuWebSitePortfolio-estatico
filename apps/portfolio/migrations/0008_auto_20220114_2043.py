# Generated by Django 3.2.9 on 2022-01-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_skiil_name_skills_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
