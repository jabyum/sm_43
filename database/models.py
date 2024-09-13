from sqlalchemy import (Column, String, Integer,
                        Float, DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    user_city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now())
    post_fk = relationship("UserPost", back_populates="user_fk")

class UserPost(Base):
    __tablename__ = "user_posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    main_text = Column(String, nullable=True)
    # column hashtag_name
    reg_date = Column(String)
    user_fk = relationship("User", lazy="subquery", back_populates="post_fk",
                           cascade="all, delete", passive_deletes=True)
# Hashtag, PostPhoto, Comment

