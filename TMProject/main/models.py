from django.db import models


class MenuNode(models.Model):
    menu_name = models.CharField(max_length=128, default='Default Menu Name')
    is_head = models.BooleanField(default=False)
    display_name = models.CharField(max_length=128, default='Default Node')
    url_name = models.CharField(max_length=256, default='index')
    parent = models.ForeignKey(
        'MenuNode',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
    )
    
    def __str__(self) -> str:
        return self.display_name
