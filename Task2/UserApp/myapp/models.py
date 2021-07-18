from django.db import models

# Create your models here.


class Products(models.Model):
	product_name = models.CharField(max_length=100)
	product_price = models.CharField(max_length=100)


'''lass UserProfile(models.Model):
    business_type = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    industry_type = models.CharField(max_length=70)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    user_id = models.CharField(max_length=13)
    email_id = models.EmailField()
    email_preferences = models.BooleanField(default=False)
    push_notification_preferences = models.BooleanField(default=False)
    reference_username = models.ForeignKey(UserName, on_delete=models.CASCADE)
'''