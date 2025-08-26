from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import html

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tasks = relationship("Task", back_populates="user")
    
    def __repr__(self):
        return f"<User {html.escape(self.name)} ({html.escape(self.email)})>"

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")
    
    def __repr__(self):
        status = "✅" if self.completed else "❌"
        try:
            user_name = html.escape(self.user.name) if self.user else 'No User'
        except AttributeError:
            user_name = 'No User'
        return f"{self.id}. {html.escape(self.title)} ({user_name}) - {status}"

engine = create_engine('sqlite:///tasks.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)