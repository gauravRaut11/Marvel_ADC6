from django.conf import settings
from django.db import models

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2, max_digits=100)
    category=models.CharField(max_length=100)  
    pdf=models.FileField(upload_to='items/pdfs/')
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

   
        
    
    

        