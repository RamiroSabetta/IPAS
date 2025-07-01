from tortoise import fields
from tortoise.models import Model
from models.usuario import Usuario

class Contenedor(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=100)
    estado = fields.CharField(max_length=20)
    creado_por = fields.ForeignKeyField('models.Usuario', related_name='contenedores')
    creado_en = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
