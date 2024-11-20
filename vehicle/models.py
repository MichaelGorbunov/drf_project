from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name="машина"
        verbose_name_plural = "машинs"


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name="moto"
        verbose_name_plural = "motos"

class Milage(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True,related_name="milage")
    moto = models.ForeignKey(Moto,on_delete=models.CASCADE,null=True,blank=True,related_name="milage")
    milage = models.PositiveIntegerField(verbose_name="пробег")
    year = models.PositiveSmallIntegerField(verbose_name="year")

    def __str__(self):
        return f"{self.moto if self.moto else self.car} - {self.year}"

    class Meta:
        verbose_name = "пробег"
        verbose_name_plural = "пробеги"
        ordering =["-year"]


