import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Subjects(SqlAlchemyBase):
    __tablename__ = 'subjects'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    subtopics = orm.relation("Topics", back_populates='subjects')

class Topics(SqlAlchemyBase):
    __tablename__ = 'topics'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    subjects_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("subjects.id"))
    name = sqlalchemy.Column(sqlalchemy.String)
    subjects = orm.relation('Subjects')
    subtopics = orm.relation("Subtopics", back_populates='topics')


class Subtopics(SqlAlchemyBase):
    __tablename__ = 'subtopics'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("topics.id"))
    name = sqlalchemy.Column(sqlalchemy.String)
    theory = sqlalchemy.Column(sqlalchemy.String)
    topics = orm.relation('Topics')
    exercises = orm.relation("Exercises", back_populates='subtopics')

class Exercises(SqlAlchemyBase):
    __tablename__ = 'exercises'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    subtopics_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("subtopics.id"))
    text = sqlalchemy.Column(sqlalchemy.String)
    answer = sqlalchemy.Column(sqlalchemy.String)
    number = sqlalchemy.Column(sqlalchemy.Integer)
    subtopics = orm.relation("Subtopics")
    user_exercises = orm.relation("User_exercises", back_populates='exercises')









