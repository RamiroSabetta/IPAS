from tortoise import fields
from tortoise.models import Model
from models.imagen import Imagen

class Contenedor(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=100, null=False)
    descripcion = fields.TextField(null=True)
    imagen = fields.ForeignKeyField('models.Imagen', related_name='contenedores', null=False)
    estado = fields.CharField(max_length=20, null=True)
    puertos = fields.JSONField(null=True)

    def __str__(self):
        return self.nombre
