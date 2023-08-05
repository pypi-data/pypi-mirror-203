from sqlalchemy import (
    Column, String, DateTime, Boolean
)
from abstract_models import AbstractBaseDataModel
from sqlalchemy.sql import func


class User(AbstractBaseDataModel):
    __tablename__ = 'user'

    class Meta:
        verbose_name = 'Пользователь'

    first_name = Column(String(100), nullable=True, info={
        "verbose_name": "Имя пользователя"
    })
    last_name = Column(String(100), nullable=True, info={
        "verbose_name": "Фамилия пользователя"
    })
    phone_number = Column(String(64), nullable=True, info={
        "verbose_name": "Номер телефона пользователя"
    })
    registered_at = Column(DateTime(timezone=True), server_default=func.now(), info={
        "verbose_name": "Дата регистрации пользователя"
    })
    activation_code = Column(String(128), nullable=True, info={
        "verbose_name": "Активационный код пользователя"
    })
    direction = Column(String(128), info={
        "verbose_name": "Направление пользователя"
    })
    is_active = Column(Boolean, default=False, info={
        "verbose_name": "Активный пользователь"
    })
    is_admin = Column(Boolean, default=False, info={
        "verbose_name": "Администратор"
    })
    is_superuser = Column(Boolean, default=False, info={
        "verbose_name": "Супер Администратор"
    })


class Company(AbstractBaseDataModel):
    __tablename__ = 'company'

    class Meta:
        verbose_name = "Компания"

    title = Column(String(100), nullable=True, info={
        "verbose_name": "Название компании"
    })
    description = Column(String(528), nullable=True, info={
        "verbose_name": "Описание компнии"
    })
    phone_number = Column(String(64), info={
        "verbose_name": "Номер телефона компании"
    })
