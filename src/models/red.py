from sqlalchemy import Column, Integer, String, MetaData, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

# 메타데이터 생성
metadata = MetaData()
Base = declarative_base(metadata=metadata)


class TheSoundOfHeart(Base):
    __tablename__ = 'the_sound_of_heart'

    the_sound_of_heart_se = Column(Integer, primary_key=True)
    member_se = Column(Integer, ForeignKey('member.member_se'))
    message_ct = Column(LONGTEXT)
    reg_dt = Column(DateTime)

    # Member 테이블과의 관계 정의
    member = relationship('Member', back_populates='the_sound_of_heart')


class Member(Base):
    __tablename__ = 'member'

    member_se = Column(Integer, primary_key=True)
    nick_nm = Column(String(255))

    # TheSoundOfHeart 테이블과의 관계 정의
    the_sound_of_heart = relationship(
        'TheSoundOfHeart', back_populates='member')