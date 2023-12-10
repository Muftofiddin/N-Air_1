from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Sneakers(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "So'm"
    RU = "rubl"
    ENG = '$'
    th_price = (
        (UZ, "So'm"),
        (RU, "rubl"),
        (ENG, '$'),
    )
    price_type = models.ImageField(max_length=10,
                                    choices=th_price, default="So'm")
    price = models.TextField()
    images = models.ImageField()


    def __str__(self):
        return self.name



#Buy bu Function singleda sotib olish uchun ishlatiladi
# product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True) - Bu Bizga mahsulotni aniq olishimzga yordam beradi
#  ALL_SIZE = (
#         ("36", "36"),
#         ("37", '37'),
#         ("38", "38"),
#         ("39", "39"),
#         ("40", "40"),
#         ("41", "41"),
#         ("42", "42"),
#         ("43", "43"),
#         ("44", "44"),
#     ) - Bu esa mahsuloting razmerlari shu kurinishda yoziladi
#-------------------------------------------------------------------
# size = models.CharField(max_length=100, choices=ALL_SIZE) - Bu razmerga qarab nechta olishini aytadi
#    ALL_VALUES = (
#       ("1", "1"),
#       ("2", "2"),
#       ("3", "3"),
#       ("4", "4"),
#       ("5", "5"), - Bu Tanlangan mahsulotni nechta sotib olishini bildiradi.
class Buy(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    ALL_SIZE = (
        ("36", "36"),
        ("37", '37'),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
    )
    size = models.CharField(max_length=100, choices=ALL_SIZE)
    ALL_VALUES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=100, choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Advertising(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Register(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=30)




    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name




