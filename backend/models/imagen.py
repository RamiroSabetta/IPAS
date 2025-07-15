from tortoise import fields
from tortoise.models import Model

class Imagen(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre 