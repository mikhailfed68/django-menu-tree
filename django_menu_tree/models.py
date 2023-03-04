from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField('Custom URL', max_length=160, blank=True, null=True, help_text="You must not set the 'use_named_url' flag")
    use_named_url = models.BooleanField()
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
