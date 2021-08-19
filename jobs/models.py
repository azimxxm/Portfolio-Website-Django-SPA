from django.db import models

class About(models.Model):
    WORK_TYPES = (
        ('IT specialist', 'IT specialist'),
        ('Web Developer', 'Web Developer'),
        ('Android Developer', 'Android Developer'),
        ('Mobile Developer', 'Mobile Developer'),
        ('UX / UI Designer', 'UX / UI Designer'),
        ('IOS Developer', 'IOS Developer'),
    )
    DEGREES = (
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Middle', 'Middle'),
        ('Team lead', 'Team lead'),
    )
    image = models.ImageField(upload_to='About/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    work_type = models.CharField(max_length=50, choices=WORK_TYPES)
    info_work = models.TextField(max_length=255)
    birthday = models.DateField()
    website = models.URLField()
    phone = models.BigIntegerField()
    city = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    degree = models.CharField(max_length=20, choices=DEGREES)
    emil = models.EmailField()
    freelance = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    info = models.TextField(max_length=300, blank=True)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='Portfolio/')
    url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.firstName