# Generated by Django 4.1.7 on 2023-02-25 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_alter_provider_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Срок годности'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='providers.provider', verbose_name='Поставщики'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
