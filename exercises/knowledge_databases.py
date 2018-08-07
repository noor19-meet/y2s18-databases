from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article():
	My_knowledge = Knowledge (
		topic = topic,
		title = title,
		rate = rate)
	session.add(My_knowledge)
	session.commit()

def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

