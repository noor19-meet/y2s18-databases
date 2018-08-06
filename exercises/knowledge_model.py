from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge'
	student_id = Column(Integer, primary_key=True)
	topic = Column(String)
	title = Column(String)
	rate = Column(Integer)
	def __repr__(self):
		return ("if you want to learn about {}" "open {}" "it is rated {} out of 10!" ).format(
			self.topic,
			self.title,
			self.rate)
a = Knowledge(topic="electricity ", title = "https://en.wikipedia.org/wiki/Electricity ", rate=9)
print(a)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the   
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.