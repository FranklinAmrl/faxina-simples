from django.db.models import TextChoices


class GenreChoices(TextChoices):
    FEMALE = "F"
    MALE = "M"
    OTHERS = "O"
