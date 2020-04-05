from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30, primary_key=True, editable=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    money = models.BigIntegerField(default=0)
    has = models.CharField(max_length=1000, default='')
    cart = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username']
        verbose_name = '账户'
        verbose_name_plural = '账户'

class Item(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=30, primary_key=True, blank=False)
    content = models.CharField(max_length=200)
    birthday = models.DateField()
    age = models.BigIntegerField()
    sex = models.CharField(max_length=32,choices=gender)
    height = models.BigIntegerField()
    weight = models.BigIntegerField()
    img_url = models.CharField(max_length=200, null=False, blank=False)
    new = models.BooleanField(default = False)
    model =  models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '宠物项'
        verbose_name_plural = '宠物项'

class LiveModel(models.Model):
    title = models.CharField(max_length=30, primary_key=True, blank=False)
    pluginModelPath = models.CharField(max_length=200, null=False, blank=False) # 'live2d-widget-miku/assets/'
    model_jsonPath = models.CharField(max_length=200, null=False, blank=False) # '/live2dw/live2d-widget-model-miku/assets/miku.model.json'
    model_scale = models.DecimalField(decimal_places=4, max_digits=5, null=False, blank=False)
    display_position = models.CharField(max_length=20, null=False, blank=False)
    display_width = models.BigIntegerField(null=False, blank=False)
    display_height = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = '模型'
        verbose_name_plural = '模型'
