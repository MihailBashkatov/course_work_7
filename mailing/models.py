from django.db import models


# Create Model Receiver
class Receiver(models.Model):
    name = models.CharField(
        max_length=300,
        help_text="Insert Name and surname of receiver",
        verbose_name="Name",
    )
    email = models.CharField(
        max_length=300,
        unique=True,
        help_text="Insert Email address of receiver",
        verbose_name="Email",
    )
    description = models.TextField(
        help_text="Insert comment", verbose_name="Comment"
    )

    receiver_chosen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}. Email: {self.email}"

    class Meta:
        verbose_name = "Receiver"
        verbose_name_plural = "Receivers"
        ordering = ["name", "email"]

    # def get_absolute_url(self):
        # return reverse('mailing', kwargs={'mailing_id': self.id})


# Create Model Message
class Message(models.Model):
    title = models.CharField(
        max_length=300,
        help_text="Insert title of message",
        verbose_name="Title",
    )

    message = models.TextField(help_text="Insert subject", verbose_name="Message")

    message_chosen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = [
            "title",
        ]


# Create Model Mailing
class Mailing(models.Model):
    CREATED = "Created"
    LAUNCHED = "Launched"
    COMPLETED = "Completed"

    STATUS_CHOICES = [
        (CREATED, "Created"),
        (LAUNCHED, "Launched"),
        (COMPLETED, "Completed"),
    ]

    first_sending = models.DateTimeField(
        auto_now=True, verbose_name="Date and time of first sending"
    )
    end_sending = models.DateTimeField(verbose_name="Date and time of ends sending", null=True, blank=True)

    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name="Message",
        related_name="mailings",
    )

    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default=CREATED,
        verbose_name="Mailing status",
    )

    receivers = models.ManyToManyField(
        Receiver,
        related_name="mailings",
        verbose_name="receivers",
    )

    def __str__(self):
        return f"Mailing title '{self.message}'"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
        ordering = ["first_sending"]


# Create Model Attempt
class Attempt(models.Model):
    NOT_STARTED = "Not Started"
    SUCCEED = "Succeed"
    NOT_SUCCEED = "Not Succeed"

    STATUS_CHOICES = [
        (NOT_STARTED, "Not Started"),
        (SUCCEED, "Succeed"),
        (NOT_SUCCEED, "Not Succeed"),
    ]

    attempt_time = models.TimeField(auto_now=True, verbose_name="Time of the attempt")
    attempt_status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=NOT_STARTED,
        verbose_name="Attempt status",
    )
    server_respond = models.TextField(verbose_name="Server respond")
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name="Mailing",
        related_name="attempts",
    )

    def __str__(self):
        return f"Attempt ID: {self.id}"

    class Meta:
        verbose_name = "Attempt"
        verbose_name_plural = "Attempts"
        ordering = ["attempt_time"]
