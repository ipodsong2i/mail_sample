from sqlalchemy import create_engine, Column, Integer, String, MetaData, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from utils.config import config
from sqlalchemy.ext.declarative import declarative_base


# config 파일에서 db 환경을 가져옴
db_configs = {
    "black": config.get_config("MARIA_DB.BLACK"),
    "red": config.get_config("MARIA_DB.RED")
}

# SQLAlchemy 엔진 및 세션 생성
engines = {}
sessions = {}

# 스키마 설정
for schema, db_config in db_configs.items():
    db_address = db_config["HOST"]
    db_port = db_config["PORT"]
    db_user = db_config["USERNAME"]
    db_password = db_config["PASSWORD"]
    db_name = db_config["DB_NAME"]

    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}"
    engines[schema] = create_engine(db_url)
    sessions[schema] = sessionmaker(bind=engines[schema])()


# 메타데이터 생성
metadata = MetaData()

Base = declarative_base(metadata=metadata)

# DB 테이블 매핑


class WorksMember(Base):
    __tablename__ = 'works_member'

    works_member_se = Column(Integer, primary_key=True)
    works_type_cd = Column(Integer)
    works_member_id = Column(String(50))


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
