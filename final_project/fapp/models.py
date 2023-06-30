import math
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ckeditor_uploader import fields as ckmediafields
from django.utils import timezone
from fapp.custom_managers import MyUserManager
from final_project import settings


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField("Email address", unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=150)
    last_name = models.CharField(verbose_name="last name", max_length=150)
    tel = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=150, null=True)
    in_mailing_list=models.BooleanField(default=False)
    post_code = models.IntegerField(null=True)
    viewed10_products = models.ManyToManyField('Product', related_name='viewed_in_users', through='SortViewedProducts')


    # This need for create_user works with first_name, last_name, password
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'first_name', 'last_name', 'password'

    def __str__(self):
        return self.username or self.email


    def liked_products_count(self):
        return self.liked_products.count()

    def ordered_products_count(self):
        """get user products in order with pending status"""
        try:
            return self.orders.get(status='pending').order_products.count()
        except ObjectDoesNotExist:
            return 0

class SortViewedProducts(models.Model):
    """Through model for User and Product models(for control by product added date)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

class IndependentMail(models.Model):
    """
    This model has been created for give users possible receive info about new products without registration(with only email).
    If any product  from mailing list  user will like, he will be motivated to register on the site to buy product.
    """
    mail = models.EmailField(verbose_name='Independent mail', unique=True)

    def __str__(self):
        return self.mail


class Brand(models.Model):
    """Common brand model, can it may have products"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Category(models.Model):
    """Category(it may have products), can be nested"""
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='child_cats', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_replace = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class BlogCategory(models.Model):
    """Category(it may have blog)"""
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
    """User order model"""
    status_choices = ('pending', 'pending'), ('rejected', 'rejected'), ('payed', 'payed')

    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=status_choices, max_length=20, default='pending')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.status in ('payed', 'rejected'):
            self.payment_date = timezone.now()
        super().save(*args, **kwargs)


    def code(self):
        """Unique code for each order"""
        return f'{self.user.id}-{self.id}'

    def total_prices_sum(self):
        """Return order products sum"""
        return self.order_products.aggregate(models.Sum('price'))['price__sum']

    def __str__(self):
        return f'{self.user.__str__()} - {self.status}'

class Product(models.Model):
    """Product, per each creating send mail to all users in mail list"""
    price = models.IntegerField()
    saled_price = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150)
    colors = models.CharField(verbose_name='Write colors separated with comma', max_length=250)
    resolution = models.CharField(verbose_name='Write resolution separated with comma', max_length=250)
    delivery_days = models.IntegerField()
    desc = models.TextField()
    optional_characteristics = models.JSONField(blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default='000000')
    liked_in_users = models.ManyToManyField(User, related_name='liked_products', blank=True)
    ordered_in_orders = models.ManyToManyField(Order, related_name='order_products', blank=True)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, message='Quantity can\'t be less than 0')],
        default=1
    )

    def save(self, *args, **kwargs):
        independent_mails = IndependentMail.objects.values_list('mail', flat=True)
        user_mails = User.objects.filter(in_mailing_list=True).values_list('email', flat=True)
        # Works fine, but send mails with each product update...
        # html_msg=\
        # f"""
        #     <h1>Price: {self.saled_price or self.price}$<h1>
        #     <h2>Brand: {self.brand}</h2>
        #     <p>{self.desc}</p>
        #     Delivery days: {self.delivery_days} <br>
        #     <a href="https://127.0.0.1:8080/#/products/{self.id}">See detail</a>
        # """
        # send_mail(
        #     self.name,
        #     html_msg,
        #     settings.EMAIL_HOST_USER,
        #     [*independent_mails, *user_mails],
        #     html_message=html_msg,
        # )
        return super().save(*args, **kwargs)

    @property
    def available(self):
        return True if self.quantity >= 1 else False

    @property
    def sale_new_hit(self):
        """
        Define product top right circle content(in frontEnd slide).
        If product liked for >= 10 user - 'HIT!',
        elif product sale >= 50% - 'saleXX',
        else 'NEW!'
        """
        if self.liked_in_users.count() >= 10:
            return 'HIT!'
        elif self.saled_price and 100 - (self.saled_price / self.price) * 100 >= 20:
            return f'sale{100 - int((self.saled_price / self.price) * 100)}'

        return 'NEW'

    @property
    def stars_avg(self):
        """Return avg from stars in product comments"""
        stars_avg = self.comments.aggregate(models.Avg('stars'))['stars__avg']
        return math.ceil(stars_avg) if stars_avg else stars_avg

    @property
    def comments_count(self):
        return self.comments.count()

    def get_resolutions(self):
        """Split resolutions from string"""
        return tuple(map(lambda res: res.strip(), self.resolution.split(',')))

    def __str__(self):
        if self.saled_price:
            return f'{self.name} --- {self.saled_price}$ ({self.price})'
        return f'{self.name} --- {self.price}$'

class Comment(models.Model):
    """Common comment"""
    product = models.ForeignKey(Product, related_name='comments' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
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
    """Model for multiple images in product and not only"""
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.SET_NULL, blank=True, null=True)
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.SET_NULL, blank=True, null=True)


