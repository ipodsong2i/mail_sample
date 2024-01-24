from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.maria_db_util import sessions, WorksMember, TheSoundOfHeart, Member
from enum import Enum
from utils.mail_util import send_ses_email
from datetime import datetime


class NaverWorksGroupType(Enum):
    Sports2i = 1
    Bigglz = 2


# 비글즈 직원의 네이버 웍스 아이디를 가져옴
def get_staff_id_list():
    # result = sessions['black'].query(WorksMember.works_member_id).filter(
    #     WorksMember.works_type_cd == NaverWorksGroupType.Bigglz.value).all()

    result = sessions['black'].query(WorksMember.works_member_id).filter(
        WorksMember.works_member_id == 'absolutecool18').all()

    return result


# 이메일 수신 리스트를 생성함
def get_email_receivers():
    result = []

    id_list = get_staff_id_list()
    for id in id_list:
        _id = id[0].strip("'")
        result.append(f'{_id}@bigglz.com')

    return result


# {date}에 해당하는 마음의 소리 내용을 가져옴
def get_sound_of_heart(date=None):
    reg_dt = date.strftime("%Y-%m-%d")
    result = sessions['red'].query(Member.nick_nm, TheSoundOfHeart.message_ct, TheSoundOfHeart.reg_dt).join(Member).filter(
        TheSoundOfHeart.reg_dt >= reg_dt + " 00:00:00",
        TheSoundOfHeart.reg_dt <= reg_dt + " 23:59:59"
    ).order_by(TheSoundOfHeart.the_sound_of_heart_se.asc()).all()

    return result


# 이메일 제목을 생성함
def get_email_subject(date: str = None):
    if not date:
        date = datetime.now()

    result = date.strftime("%Y년 %m월 %d일 마음의 소리")
    return result


# 이메일 내용을 생성함
def get_email_body(date: str = None):
    the_sound_of_hearts = get_sound_of_heart(date)
    result = str(the_sound_of_hearts)

    return result


# 이메일을 생성함
def create_email(sender_email, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))


# AWS SES 서비스를 이용해 메일을 전송함
def send_email(date: str = None):
    receiver_email_list = get_email_receivers()
    subject = get_email_subject(date)
    body = get_email_body(date)
    send_ses_email(subject, body, receiver_email_list)
