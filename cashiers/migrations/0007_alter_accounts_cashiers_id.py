# Generated by Django 4.1.7 on 2023-04-13 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashiers', '0006_alter_accounts_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='cashiers_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashiers_id', to='cashiers.cashiers'),
        ),
    ]