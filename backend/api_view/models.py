from django.db import models
import uuid

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=500)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.TextField(blank=True, null= True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.name