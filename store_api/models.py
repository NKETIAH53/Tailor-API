from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Design(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("design style"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('style description')
    )
    
    def __str__(self):
        return self.name


class Store(models.Model):
    
    class StoreObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='accepted')
        
    options = (
        ('pending', 'P'),
        ('accepted', 'A')
    )
        
    store_owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,  
        related_name='stores'
    )
    design = models.ManyToManyField(
        Design,
        null=True,
        through='DesignDetail'
    )
    store_name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254
    )
    about = models.TextField(
        blank=True, 
        null=True
    )    
    status = models.CharField(
        max_length=15,
        choices=options,
        default='pending'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='store creation date',
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='store last updated'
    )
    
    objects = models.Manager()
    storeobjects = StoreObjects()
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.store_name


class DesignDetail(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='store_design_details'
    )
    design = models.ForeignKey(
        Design,
        on_delete=models.SET_NULL,
        null=True,
        related_name='design_details'       
    ) 
    cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=299.99
    )
    
    def __str__(self):
        return self.design.name

class Media(models.Model):
    design_detail = models.ForeignKey(
        DesignDetail,
        on_delete=models.CASCADE,
        related_name='design_images'
    )
    img_url = models.ImageField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("design image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text"),
    )
    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("default design image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("upload date"),
    )
    

class Branch(models.Model):
    store = models.ForeignKey(
        Store, 
        on_delete=models.CASCADE, 
        related_name='store_branch'
    )
    branch_name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='branch name'
    )
    location = models.TextField()
    street_name = models.CharField(
        max_length=150,
        verbose_name='branch street name'
    )
    digital_address = models.CharField(
        max_length=15, 
        null=False, 
        blank=False,
        verbose_name='branch digital address'
    )

    def __str__(self):
        return self.branch_name
