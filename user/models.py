from django.db import models

from django.contrib.auth.password_validation import validate_password

from django.core.validators import RegexValidator

from user.consts import GenreChoices

# Create your models here.
class Base(models.Model):
    created = models.DateField("Data de criação", auto_now_add=True)
    uptaded = models.DateField("Data de atualização", auto_now=True)

    class Meta:
        abstract = True


class User(Base):
    username = None
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    phone = models.IntegerField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}",
                message="O número de telefone deve ser inserido no formato '0412 345 678', '+61412345678', '+5581912345678', '+55 81 91234-5678', '+61 0412-345-678', '0412345678'. Dígitos permitidos de 8 Até 24.",
            )
        ],
    )
    birthday = models.DateField()
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
