from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ckeditor_uploader import fields as ckmediafields
from fapp.custom_managers import MyUserManager


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=150, unique=True)
    last_name = models.CharField(verbose_name="last name", max_length=150, unique=True)
    tel = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    in_mailing_list=models.BooleanField(default=False)
    post_code = models.IntegerField()

    objects = MyUserManager()

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = 'last_name', 'email',

    def __str__(self):
        return self.username or f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='child_cats', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_replace = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Blog categories'

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, related_name='blogs', on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    short_desc = models.CharField(max_length=200, blank=True, null=True)
    desc = ckmediafields.RichTextUploadingField(blank=True)

    def __str__(self):
        return self.header

class Order(models.Model):
    status_choices = ('pending', 'pending'), ('rejected', 'rejected'), ('payed', 'payed')

    status = models.CharField(choices=status_choices, max_length=20, default='pending')
    profile = models.ForeignKey(Profile, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.__str__()} - {self.status}'

class Product(models.Model):
    price = models.IntegerField()
    saled_price = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150)
    colors = models.CharField(verbose_name='Write colors separated with comma', max_length=250)
    resolution = models.CharField(verbose_name='Write resolution separated with comma', max_length=250)
    delivery_days = models.IntegerField()
    desc = models.TextField()
    optional_characteristics = models.JSONField(blank=True, null=True)
    available = models.BooleanField(verbose_name='Product available?')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default='000000')
    liked_products = models.ManyToManyField(Profile, related_name='liked_products', blank=True)
    order_products = models.ManyToManyField(Order, related_name='order_products', blank=True)

    @property
    def sale_new_hit(self):
        if self.liked_products.count() >= 10:
            return 'HIT!'
        elif self.saled_price and 100 - (self.saled_price / self.price) * 100 >= 50:
            return f'sale{100 - int((self.saled_price / self.price) * 100)}'

        return 'NEW'

    @property
    def stars_avg(self):
        all_stars = tuple(self.comments.values_list('stars', flat=True))
        if all_stars:
            return sum(all_stars) // len(all_stars)

    @property
    def comments_count(self):
        return self.comments.count()

    def get_resolutions(self):
        return tuple(map(lambda res: res.strip(), self.resolution.split(',')))

    def __str__(self):
        if self.saled_price:
            return f'{self.name} --- {self.saled_price}$ ({self.price})'
        return f'{self.name} --- {self.price}$'

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments' ,on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    text = models.TextField()
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, message='GREATER THAN 0!'),
            MaxValueValidator(5, message='LESS THAN 6')
        ],
    )

    def __str__(self):
        return self.header

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.SET_NULL, blank=True, null=True)
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.SET_NULL, blank=True, null=True)

class IndependentMail(models.Model):
    mail = models.EmailField(verbose_name='Independent mail', unique=True)

    def __str__(self):
        return self.mail

