from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models import Manager
from django.db.models import Q

User = settings.AUTH_USER_MODEL


def media_uploads(instance, filename):
    return f"store_designs/{instance.design.store_branch.branch_name}/{instance.design.style}/{filename}"


class Store(models.Model):
    class StoreObjects(Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Store.ACCEPTED)

    PENDING = "P"
    ACCEPTED = "A"
    STORE_PUBLISH_STATUS = (
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
    )

    FULL_PAYMENT = "FPBP"
    PART_PAYMENT = "PPBP"
    PAYMENT_POLICY_TYPES = (
        (FULL_PAYMENT, "full_payment_before_processing"),
        (PART_PAYMENT, "part_payment_before_processing"),
    )

    store_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stores"
    )
    store_name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=254)
    about = models.TextField(blank=True, null=True)
    policy_type = models.CharField(
        max_length=50, choices=PAYMENT_POLICY_TYPES, default=FULL_PAYMENT
    )
    part_payment_percentage = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=15, choices=STORE_PUBLISH_STATUS, default=PENDING
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="store creation date",
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="store last updated")

    objects = models.Manager()
    storeobjects = StoreObjects()

    class Meta:
        ordering = ("-created_at",)
        constraints = [
            models.CheckConstraint(
                check=(Q(part_payment_percentage__lte=0.8)),
                name="Part payment percentage should be less than or equal 0.8",
            ),
        ]

    def __str__(self):
        return self.store_name


class Branch(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store_branch"
    )
    branch_name = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="branch name"
    )
    location = models.TextField()
    street_name = models.CharField(max_length=150, verbose_name="branch street name")
    digital_address = models.CharField(
        max_length=15, null=False, blank=False, verbose_name="branch digital address"
    )

    def __str__(self):
        return self.branch_name


class Design(models.Model):

    store_branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name="branch_designs"
    )
    style = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("design style"),
    )
    description = models.TextField(
        blank=True, null=True, verbose_name=_("style description")
    )
    fabric_available = models.BooleanField(default=False)
    price_with_store_fabric = models.DecimalField(max_digits=5, decimal_places=2)
    price_without_store_fabric = models.DecimalField(
        max_digits=5, decimal_places=2, null=False
    )

    def __str__(self):
        return self.style


class Media(models.Model):
    design = models.ForeignKey(
        Design, on_delete=models.CASCADE, related_name="design_images"
    )
    image = models.ImageField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("design image"),
        upload_to=media_uploads,
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text"),
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name=_("default design image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("upload date"),
    )
