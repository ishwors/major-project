# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Add your custom fields here
    profile_pic = models.ImageField(default='default.png', null=True, blank=True) #stored in a separate media folder
    dob = models.DateField(null=True)
    blood_group = models.CharField(max_length=3,null=True)
    mobile = models.CharField(max_length=15 ,null=True)
    address = models.CharField(max_length=150 ,null=True)
    city = models.CharField(max_length=50 ,null=True)
    state = models.CharField(max_length=50 ,null=True)
    zip_code = models.CharField(max_length=10 ,null=True)
    country = models.CharField(max_length=100 ,null=True)
    

class Doctor(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add your custom fields here 
    profile_pic = models.ImageField(default='default.png', null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=True)
    dob = models.DateField(null=True)
    bio = models.TextField(blank=True)
    clinic_name = models.CharField(max_length=50, null=True)
    clinic_address = models.CharField(max_length=150, null=True)
    specialization = models.CharField(max_length=150 , null=True)
    address = models.CharField(max_length=150, null=True)
    pricing = models.IntegerField(null=True)
    degree = models.CharField(max_length=10, null=True)
    experience = models.CharField(max_length=5, null=True)
    designation = models.CharField(max_length=30, null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    
    def get_profile_url(self):
        return reverse("doctor-profile", kwargs={'slug': self.slug})

    
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.user.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = Doctor.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Doctor)
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.last_name == "Patient":
            Patient.objects.create(user=instance)

        elif instance.last_name == "Doctor":
            Doctor.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.last_name == "Patient":
        if instance.patient.profile_pic == "":
            instance.patient.profile_pic = "default.png"
        instance.patient.save()

    elif instance.last_name == "Doctor":
        instance.doctor.save()


# Review 

class Review(models.Model):

    rating = models.IntegerField()
    review_text = models.TextField(max_length=150)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE , null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE , null=True)
