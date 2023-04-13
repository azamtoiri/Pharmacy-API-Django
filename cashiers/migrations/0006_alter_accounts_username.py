# Generated by Django 4.1.7 on 2023-04-13 07:51

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashiers', '0005_alter_accounts_options_alter_accounts_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
