from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cashiers(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    brith_date = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name


class Accounts(models.Model):
    accounts_id = models.AutoField(primary_key=True)
    cashiers_id = models.ForeignKey(Cashiers, on_delete=models.CASCADE, related_name='cashiers_id')
    login = models.CharField(max_length=50, unique=True, verbose_name='Логин', null=False)
    password = models.CharField(max_length=250, null=False, verbose_name='Пароль')

    def __str__(self):
        return self.login
