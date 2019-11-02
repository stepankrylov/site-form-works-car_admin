from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        review_count = Review.objects.filter(car=self).count()
        return f'{review_count}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Публикация')
    text = models.TextField(verbose_name='Текст публикации')

    def __str__(self):
        return f'{self.car} {self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

