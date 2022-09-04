from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = {
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    }
    email = models.EmailField(
        verbose_name=_('Адрес email'),
        max_length=254,
        unique=True,
        blank=False,
        error_messages={
            'unique': _('Неуникальный email.'),
        },
        help_text=_('Укажите свой email'),
    )
    username = models.CharField(
        verbose_name=_('Логин'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _('Неуникальный никнейм.'),
        },
        help_text=_('Укажите свой никнейм'),
    )
    first_name = models.CharField(
        verbose_name=_('Имя'),
        max_length=150,
        blank=True,
        help_text=_('Укажите своё имя'),
    )
    last_name = models.CharField(
        verbose_name=_('Фамилия'),
        max_length=150,
        blank=True,
        help_text=_('Укажите свою фамилию'),
    )
    role = models.CharField(
        verbose_name=_('статус'),
        max_length=20,
        choices=ROLES,
        default=USER,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Дата регистрации'),
        auto_now_add=True,
    )
    password = models.CharField(
        verbose_name=_('Пароль'),
        max_length=150,
        help_text=_('Введите пароль'),
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()

    @property
    def is_moderator(self):
        return self.is_staff or self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.is_superuser or self.role == self.ADMIN


class Follow(models.Model):
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
        verbose_name='Автор рецепта',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='uniq_follow',
            ),
            models.CheckConstraint(
                check=~Q(user=F('author')),
                name='self_following',
            ),
        )

    def __str__(self):
        return f'{self.user} - {self.author}'
