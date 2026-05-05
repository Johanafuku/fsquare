from django.db import models
from users.models import Designer

class Design(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='designs/')
    fabric_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    quantity_meters = models.FloatField(null=True, blank=True)
    pieces = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Design {self.id} - {self.fabric_type}"

