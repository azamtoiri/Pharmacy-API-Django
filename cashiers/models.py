from django.db import models


class Cashiers(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    brith_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name


class Accounts(models.Model):
    accounts_id = models.AutoField(primary_key=True)
    cashiers_id = models.ForeignKey(Cashiers, on_delete=models.CASCADE, related_name='cashiers_id')
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.login
