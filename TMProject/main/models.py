from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=128,
        default='Default Menu Name',
        unique=True
    )
    
    def __str__(self):
        return self.name
    

class MenuNode(models.Model):
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        related_name='nodes'
    )
    is_head = models.BooleanField(default=False)
    display_name = models.CharField(max_length=128, default='Default Node')
    url_name = models.CharField(max_length=256, default='index')
    children = models.ManyToManyField('MenuNode', related_name='parent')
    
    def __str__(self) -> str:
        return self.display_name
