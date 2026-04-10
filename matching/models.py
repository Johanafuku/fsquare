from django.db import models
from designs.models import Design
from suppliers.models import Supplier

class MatchResult(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    score = models.FloatField()
    ai_analysis = models.JSONField()  # Stores structured AI output
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match: Design {self.design.id} - {self.supplier.name}"
