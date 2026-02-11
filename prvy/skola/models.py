from django.db import models

# Create your models here.
class Ucitel(models.Model):
    titul = models.CharField(max_length=10)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.titul}. {self.meno} {self.priezvisko}"
    class Meta:
        verbose_name = "Ucitel"
        verbose_name_plural = "Ucitelia"
        ordering = ["priezvisko"]

class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=10)
    def __str__(self):                        
        return f"{self.meno} {self.priezvisko} {self.trieda}"
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studenti"
        ordering = ["priezvisko"]
