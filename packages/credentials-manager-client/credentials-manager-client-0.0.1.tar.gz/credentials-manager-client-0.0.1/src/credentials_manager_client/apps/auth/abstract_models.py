from src.credentials_manager_client.db.base_model import Model
from sqlalchemy import (
    Column, String, Integer
)


class AbstractBaseDataModel(Model):
    """
    Base attributes
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, info={
        "verbose_name": "Почта пользователя"
    })
    hashed_password = Column(String(128), info={
        "verbose_name": "Пароль пользователя"
    })
