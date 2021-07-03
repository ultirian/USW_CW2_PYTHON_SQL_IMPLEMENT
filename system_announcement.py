# coding=utf-8
# Libraries
import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


# Classes
class SystemAnnouncement(Base):
    __tabename__ = 'system_announcement'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=50))
    time = Column(DateTime, default=datetime.datetime.utcnow)
    subject = Column(String(length=50))
    msg_body = Column(String(length=200))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref='system_announcement')

    def __init__(self, username, time, subject, msg_body):
        self.username = username
        self.time = time
        self.subject = subject
        self.msg_body = msg_body

    def __repr__(self):
        return "<SystemAnnouncement(from_admin_user='{0}', time ='{1}', subject='{2}, msg_body='{3}'>" \
            .format(self.from_admin_user, self.time, self.subject, self.msg_body)
