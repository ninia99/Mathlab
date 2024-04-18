from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post/', blank=True)
    short_text = models.TextField()
    category = models.ForeignKey("Category", related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class About(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class Contact(models.Model):
    number = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    map = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


'''
class Demo(models.Model):
    target_molecule = models.CharField(max_length=250)
    temperature = models.IntegerField()
    pressure_bar = models.IntegerField()
    wavelength_min = models.IntegerField()
    wavelength_max = models.IntegerField()
    wavelength_res = models.IntegerField()
    gaussian_contribution = models.IntegerField()
    Lorentzian_contribution = models.IntegerField()
    bandpass_wavelength_min = models.IntegerField()
    bandpass_wavelength_max = models.IntegerField()
    precalculated_gas_phase = models.CharField(max_length=250)
    user_defined_gas_phase = models.CharField(max_length=250)
    species = models.TextField()
    mole_fraction = models.IntegerField()

    def __str__(self):
        return self.target_molecule

    class Meta:
        verbose_name = 'demo'
        verbose_name_plural = 'demos'
'''
