from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/', blank=True)
    short_text = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


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
