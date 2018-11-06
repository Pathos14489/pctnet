# Generated by Django 2.1.2 on 2018-11-05 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('screenname', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='')),
                ('bio', models.TextField(default='')),
            ],
        ),
    ]
