# typing: ignore

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text, event
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils import URLType


class TimeStampMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow)
    created_at._creation_order = 9998
    updated_at = Column(DateTime, default=datetime.utcnow)
    updated_at._creation_order = 9998

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = datetime.utcnow()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_update", cls._updated_at)


class Base(TimeStampMixin):
    pass


DeclarativeBase = declarative_base(cls=Base)


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ScraperItemModel(DeclarativeBase):
    __tablename__ = "scraper_items"

    id = Column(Integer, primary_key=True)
    url = Column("url", URLType)
    url_hash = Column("url_hash", String(150), unique=True, index=True)
    title = Column("title", String(255))

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
