from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

# Contact
class Contact_Page(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Event
# class Categories(models.Model):
    
#     CATEGORY = (
#         ('EDUCATIONAL','EDUCATIONAL'), 
#         ('SPORTS','SPORTS'),
#         ('CAREER','CARRER'),
#         ('SPIRITUAL','SPIRITUAL'),
#         ('COMEDY','COMEDY'),
#         ('CULTURAL','CULTURAL'),
#         ('OTHERS','OTHERS'),
#     )
#     category_name = models.CharField(max_length=200,choices=CATEGORY)

#     def __str__(self):
#         return self.category_name



# class Price_Type(models.Model):
#     PRICE = (('FREE','FREE'),('PAID','PAID'))
#     price_tag = models.CharField(max_length=200,choices=PRICE)
    

#     def __str__(self):
#         return self.price_tag



class Event_Details(models.Model):

    CATEGORY = (
        ('EDUCATIONAL','EDUCATIONAL'), 
        ('SPORTS','SPORTS'),
        ('CAREER','CARRER'),
        ('SPIRITUAL','SPIRITUAL'),
        ('COMEDY','COMEDY'),
        ('CULTURAL','CULTURAL'),
        ('OTHERS','OTHERS'),
    )
    PRICE = (('FREE','FREE'),('PAID','PAID'))

    STATUS = (('Publish','Publish'),('Draft','Draft')) 

    # unique_id = models.CharField(max_length=200,null=True,blank=True,unique=True)   

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Event_images/img') 
    date = models.DateTimeField()
    price_type = models.CharField(max_length=100,choices=PRICE, default='fixed')
    price = models.IntegerField(default='0')
    category = models.CharField(max_length=100,choices=CATEGORY, default='fixed')
    location = models.CharField(max_length=500)
    description = RichTextField(null=True)
    timings = RichTextField(null=True)
    main_guest = RichTextField(null=True)
    instruction = RichTextField(null=True)
    status = models.CharField(max_length=100,choices=STATUS,default='fixed')
    # created_date = models.DateTimeField(default=timezone.now)

    # def save(self,*args,**kwargs):
    #     if self.unique_id is None and self.created_date and self.id:
    #         self.unique_id = self.created_date.strftime('75%Y%m%d23')+str(self.id)
    #     return super().save(*args,**kwargs)
    


    def __str__(self):
        return self.name





