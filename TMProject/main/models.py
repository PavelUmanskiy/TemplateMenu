from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, default='Default Menu Name')


class MenuNode(models.Model):
    menu = models.ForeignKey(
            'Menu',
            on_delete=models.CASCADE,
            related_name='nodes'
    )
    display_name = models.CharField(max_length=128, default='Default Node')
    url = models.URLField(default='/')
    children = models.ManyToManyField('MenuNode', related_name='parent')
    
    def __str__(self) -> str:
        return self.display_name
    
