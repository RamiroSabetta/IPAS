from tortoise import fields
from tortoise.models import Model

class Usuario(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    perfil = fields.CharField(null=True, max_length=20)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username
