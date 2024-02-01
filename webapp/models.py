from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Donor(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)
    d_email = models.EmailField(max_length=50)
    d_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.d_name

class WigRecipient(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=255)
    r_email = models.EmailField(max_length=50)
    distribution_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.r_name

class Wig(models.Model):
    wig_id = models.AutoField(primary_key=True)
    wig_name = models.CharField(max_length=50)
    wig_color = models.CharField(max_length=50)

    def __str__(self):
        return self.wig_name



class DistributionHistory(models.Model):
    record_id = models.AutoField(primary_key=True)
    r_id = models.ForeignKey(WigRecipient, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    wig_id = models.ForeignKey(Wig, on_delete=models.CASCADE)
    distribution_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Distribution of {self.wig_id.wig_name}Wig to {self.r_id.r_name} on {self.distribution_date}"

class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    image = models.ImageField(upload_to='images/')
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['email']



    def __str__(self):
        return self.first_name