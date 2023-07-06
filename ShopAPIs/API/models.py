from django.db import models
import datetime

#- Product Id
# - Product Name
# - Product Company
# - Product Quantity
# - Product Price
# - Product Image
# - Product Category
# - Product Description

from datetime import datetime
def generate_custom_id():
    date_string = datetime.now().strftime('%Y%d%H%M%S')
    id = f"njsproduct{date_string}"
    return id
 

class Categoty(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Products(models.Model):
    id=models.CharField(max_length=50,default=generate_custom_id, editable=False, unique=True,primary_key=True)
    name=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    quantity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='Products')
    category=models.ForeignKey(Categoty,on_delete=models.CASCADE,blank=True)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.name