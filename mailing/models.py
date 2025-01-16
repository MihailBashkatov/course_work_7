from django.db import models


# Create Model Reciever
class Receiver(models.Model):
    name = models.CharField(
        max_length=300,
        help_text="Insert Name and surname of receiver",
        verbose_name="Name and surname",
    )
    mail = models.CharField(
        max_length=300,
        unique=True,
        help_text="Insert Email address of receiver",
        verbose_name="Email",
    )
    description = models.TextField(
        help_text="Insert description", verbose_name="Description"
    )

    def __str__(self):
        return f"{self.name}. Email: {self.mail}"

    class Meta:
        verbose_name = "Receiver"
        verbose_name_plural = "Receivers"
        ordering = ["name", "mail"]
