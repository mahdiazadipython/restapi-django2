from django.db import models


class Product(models.Model):
    created         = models.DateTimeField(auto_now_add =True)
    name            = models.CharField(max_length = 100)
    description     = models.TextField(blank =True,default ='')
    price           = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    def __str__(self):
        return self.name
