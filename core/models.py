from django.db import models

from django.core import validators


# Create your models here.
class Contact(models.Model):
    """
    This models is for enquiry and contact
    """
    ENQUIRY_CHOICES = [
        ('complaint', 'Complaint'),
        ('information', 'Information'),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, validators=[validators.validate_email,])
    message = models.TextField(null=True, blank=True)
    enquiry_choice = models.CharField(max_length=255, null=True, blank=True, choices=ENQUIRY_CHOICES, default='complaint')
    ip_address = models.GenericIPAddressField(null=True, blank=True, validators=[validators.validate_ipv4_address])

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.full_name

    def get_enquiry_type(self):
        return self.enquiry_choice