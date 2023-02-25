from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    amount = models.PositiveIntegerField(verbose_name='Количество')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider', verbose_name='Поставщики')
    end_date = models.DateField(null=True, blank=True, default=None, verbose_name='Срок годности')

    def __str__(self):
        return self.name
