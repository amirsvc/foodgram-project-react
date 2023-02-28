from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

username_validator = RegexValidator(
    regex=r'^[\w.@+-]+\Z',
    message='Должны быть только цифры, буквы и символы: .@+-',
)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'password',
    ]

    email = models.EmailField(
        max_length=settings.EMAIL_LENGTH,
        unique=True,
    )
    username = models.CharField(
        max_length=settings.FIELD_LENGTH,
        unique=True,
        validators=[username_validator],
    )
    first_name = models.CharField(
        'Имя',
        max_length=settings.FIELD_LENGTH,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=settings.FIELD_LENGTH,
    )
    password = models.CharField(
        max_length=settings.FIELD_LENGTH,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                name='unique_follower',
                fields=('user', 'author'),
            ),
            models.CheckConstraint(
                name='not_self_follow',
                check=~models.Q(user=models.F('author')),
            ),
        )
