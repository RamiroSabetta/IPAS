from tortoise import fields
from tortoise.models import Model
from models.usuario import Usuario
from models.contenedor import Contenedor

class Asignacion(Model):
    id = fields.IntField(pk=True)
    usuario = fields.ForeignKeyField('models.Usuario', related_name='asignaciones')
    contenedor = fields.ForeignKeyField('models.Contenedor', related_name='asignaciones')

    def __str__(self):
        return f"{self.usuario.username} - {self.contenedor.nombre}" 