from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(
        'Custom URL',
        max_length=250,
        blank=True,
        null=True,
        help_text="If you use custom url you must not set the 'use_named_url' flag"
    )
    use_named_url = models.BooleanField(
        default=True,
        help_text="Required True if you use 'named url'",
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительское меню',
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
