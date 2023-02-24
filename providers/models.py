from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider')
    end_date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
