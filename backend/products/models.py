from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL # auth.User

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def sale_price(self):
        # using % operator 
        # return "%.2f" %(float(self.price)*0.8)

        # str.format()
        # return "{:.2f}".format(float(self.price)*0.8)

        # using f-strings 
        # :.2f: This is the formatting specifier, which indicates that the result should be formatted as a floating-point number with two decimal places.
        return f"{float(self.price)*0.8:.2f}"
    

    def get_discount(self):
        return "122"