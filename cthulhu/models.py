from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User
from dataclasses import dataclass


class UserInfo(User):
    __tablename__ = "ab_user"


@dataclass
class UserData(Model):
    __tablename__ = "ab_user_data"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('ab_user.id'), nullable=False)
    user = relationship(UserInfo)
    user_icon = Column(String(20), nullable=False, default='default')
    user_country = Column(String(2), nullable=False, default='CL')
    user_tz = Column(String(100), nullable=False, default='America/Santiago')

    def __repr__(self):
        return self.user_id


@dataclass
class Service(Model):
    __tablename__ = "ab_service"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean)
    cid_origin = Column(String(20), nullable=False)
    url_ok = Column(String(255), nullable=False)
    url_nok = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name


@dataclass
class ServiceConfig(Model):
    __tablename__ = "ab_service_config"
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('ab_service.id'), nullable=False)
    service = relationship(Service)
    name = Column(String(255), nullable=False)
    data = Column(Text(), nullable=True)
    active = Column(Boolean, default=True, nullable=False)

    def __repr__(self):
        return self.name
