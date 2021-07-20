# Generated by Django 3.2.5 on 2021-07-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0002_extendeduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='user',
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
