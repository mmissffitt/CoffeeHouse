from django.db import models

class User(models.Model):
    email = models.EmailField("Почта", max_length=255)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    birth_date = models.DateField("Дата рождения")
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
class Staff(models.Model):
    email = models.EmailField("Почта", max_length=255)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    birth_date = models.DateField("Дата рождения")
    date_hiring = models.DateField("Дата приема на работу")
    position = models.ManyToManyField('Position', verbose_name='Должности')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.position}"
    
class Position(models.Model):
    position_name = models.CharField("Название должности", max_length=100)
    rate_per_hour = models.FloatField('Ставка в час')

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
       
    def __str__(self):
        return self.position_name
    
