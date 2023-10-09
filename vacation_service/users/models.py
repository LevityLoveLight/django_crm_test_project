from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'


class User(AbstractUser):

    ROLE = (
        (USER, 'user'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
    )
    email = models.EmailField('e-mail', unique=True)
    username = models.CharField("Логин", max_length=50, unique=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    position = models.CharField('Должность', max_length=50, null=True, blank=True)
    role = models.CharField("Роль пользователя", max_length=10,
                            choices=ROLE, default=USER)

    class Meta:
        ordering = ['id']

    @property
    def is_admin(self):
        return any(
            [self.role == ADMIN, self.is_superuser, self.is_staff]
        )

    @property
    def is_moderator(self):
        return self.ROLE == MODERATOR

    def __str__(self):
        return self.username


class Vacation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='vacation',
    )
    vacation_days = models.IntegerField("Количество дней отпуска", null=True, blank=True)
    vacation_date_start = models.DateField("Начало отпуска", default=None, null=True, blank=True)
    vacation_date_end = models.DateField("Конец отпуска", default=None, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
