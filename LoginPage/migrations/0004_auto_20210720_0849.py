# Generated by Django 3.2.5 on 2021-07-20 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LoginPage', '0003_auto_20210720_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='username',
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]