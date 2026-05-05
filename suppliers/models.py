from django.db import models
from django.contrib.auth.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fabric_types = models.JSONField(null=True, blank=True)
    colors_available = models.JSONField(null=True, blank=True)
    processing = models.JSONField(null=True, blank=True) #wooven, nonwooven, knitten
    min_meters = models.FloatField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    number_of_pieces = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


#portfolio of images from supplier
class SupplierImage(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="images"  
    )

    image = models.ImageField(upload_to="supplier_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image of {self.supplier.user.username}"