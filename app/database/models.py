from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

from database.db import Base


class DataCrawl(Base):
    __tablename__ = 'data_crawl'

    id = Column(String, unique=False, nullable=False, primary_key=True)

    author = Column(String, unique=False, nullable=True)

    title = Column(String, unique=False, nullable=True)

    content = Column(String, unique=False, nullable=True)

    rating = Column(Integer, unique=False, nullable=True)

    source = Column(String, unique=False, nullable=False)

    crawl_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False, server_default=func.now(),
    )