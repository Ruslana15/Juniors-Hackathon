from django.db import models


class Vacancy(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


