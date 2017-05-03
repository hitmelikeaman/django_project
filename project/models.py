from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='photos')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    category = models.ForeignKey(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Question(models.Model):
    name = models.CharField(max_length=200)
    ease = models.DecimalField(max_digits=19, decimal_places=10)
    fonts_color = models.DecimalField(max_digits=19, decimal_places=10)
    simple_design = models.DecimalField(max_digits=19, decimal_places=10)
    animations = models.DecimalField(max_digits=19, decimal_places=10)
    table = models.DecimalField(max_digits=19, decimal_places=10)
    lists = models.DecimalField(max_digits=19, decimal_places=10)
    forms = models.DecimalField(max_digits=19, decimal_places=10)
    variables_data = models.DecimalField(max_digits=19, decimal_places=10)
    json = models.DecimalField(max_digits=19, decimal_places=10)
    flexbox = models.DecimalField(max_digits=19, decimal_places=10)
    do_anchors = models.DecimalField(max_digits=19, decimal_places=10)
    structure = models.DecimalField(max_digits=19, decimal_places=10)
    moves = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.name
