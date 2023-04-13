from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Cashiers(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    brith_date = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Accounts(AbstractUser):
    cashiers_id = models.ForeignKey(Cashiers, on_delete=models.CASCADE, related_name='cashiers_id', null=True,
                                    verbose_name='Кассир')
    username = models.CharField(max_length=250, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=250, verbose_name='Пароль')

    def __str__(self):
        return self.username
