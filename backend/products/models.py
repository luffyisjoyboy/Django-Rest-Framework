from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    

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