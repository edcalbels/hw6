from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=1000, unique=True)  # "lorem ipsum"
    description = models.TextField(blank=True)  # "lorem ipsum"
    price = models.FloatField()  # 199.99
    is_active = models.BooleanField(default=True)  # False
    created_at = models.DateTimeField(auto_now_add=True)  # 2022-06-06 .....
    updated_at = models.DateTimeField(auto_now=True)  # 2022-06-06 .....
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text
