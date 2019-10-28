from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from scraper.models import ScraperItemModel, create_table


def session_factory(pg_settings: dict) -> sessionmaker:
    conn = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db_name}".format(
        **pg_settings
    )
    engine = create_engine(conn)
    create_table(engine)
    return sessionmaker(bind=engine)


def item_exists(session: Session, url_hash: str) -> bool:
    q = session.query(ScraperItemModel).filter(ScraperItemModel.url_hash == url_hash)
    return session.query(q.exists()).scalar()


def get_item(session: Session, url_hash: str) -> ScraperItemModel:
    return (
        session.query(ScraperItemModel)
        .filter(ScraperItemModel.url_hash == url_hash)
        .first()
    )


def delete_items(session: Session, url_hashes: List[str]) -> List[str]:
    deleted_items = []
    for obj in (
        session.query(ScraperItemModel)
        .filter(ScraperItemModel.url_hash.in_(url_hashes))
        .all()
    ):
        deleted_items.append(obj.url_hash)
        session.delete(obj)
    return deleted_items
