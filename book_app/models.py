from django.db import models

# Create your models here.


class Publisher(models.Model):

    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    year_founded = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):

    TYPE_CHOICES = [
        ("SOF", "Soft"),
        ("HAR", "Hard")
    ]

    CATEGORY_CHOICES = [
        ("ROM", "Romance"),
        ("THR", "Thriller"),
        ("BIO", "Biography"),
        ("CLA", "Classic"),
        ("DRA", "Drama"),
        ("HIS", "History")
    ]

    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="assets/")
    isbn = models.CharField(max_length=20)
    year_published = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    dimensions = models.CharField(max_length=20)
    book_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    book_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return self.title
