# Django Пользователи: Сигналы, Кастомная модель, Аутентификация и Оптимизация

## 📡 Сигналы в Django

Сигналы позволяют выполнять действия при создании, обновлении или удалении объектов. Например, при создании пользователя — автоматически создаётся его профиль.

### Пример: Создание профиля пользователя при регистрации

#### `users/signals.py`

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


Результат

    ✅ Автоматическое создание профилей пользователей

    ✅ Гибкая система аутентификации с кастомной моделью

    ✅ Повышение производительности запросов

    Для запуска проекта:
    🛠️ Установите зависимости: pip install -r requirements.txt
    🚀 Запустите сервер: python manage.py runserver
