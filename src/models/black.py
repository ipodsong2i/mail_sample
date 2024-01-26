from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# 메타데이터 생성
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# DB 테이블 매핑
class WorksMember(Base):
    __tablename__ = 'works_member'

    works_member_se = Column(Integer, primary_key=True)
    works_type_cd = Column(Integer)
    works_member_id = Column(String(50))