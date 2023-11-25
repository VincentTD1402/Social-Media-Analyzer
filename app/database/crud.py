from sqlalchemy.orm import Session
from database.models import DataCrawl
from database.schemas import DataCrawlSchema


# def get_comment(db: Session, comment: DataCrawlSchema) -> DataCrawl:
#     db_comment = DataCrawl(
#         id=comment.get("id"),
#         author=comment.get("author"),
#         title=comment.get("title"),
#         content=comment.get("content"),
#         rating=comment.get("rating"),
#         source=comment.get("source")
#     )
#     db.add(db_comment)
#     db.commit()
#     db.refresh(db_comment)
#     return db_comment


def get_comment(db: Session, comment: DataCrawlSchema) -> DataCrawl:
    existing_comment = db.query(DataCrawl).filter_by(id=comment.get("id")).first()

    if existing_comment:
        existing_comment.author = comment.get("author")
        existing_comment.title = comment.get("title")
        existing_comment.content = comment.get("content")
        existing_comment.rating = comment.get("rating")
        existing_comment.source = comment.get("source")
        db.commit()
        db.refresh(existing_comment)
        return existing_comment

    db_comment = DataCrawl(
        id=comment.get("id"),
        author=comment.get("author"),
        title=comment.get("title"),
        content=comment.get("content"),
        rating=comment.get("rating"),
        source=comment.get("source")
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment