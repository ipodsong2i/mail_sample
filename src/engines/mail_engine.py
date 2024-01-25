from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.maria_db_util import sessions, WorksMember, TheSoundOfHeart, Member
from enum import Enum
from utils.mail_util import send_ses_email
from datetime import datetime
from template import email_template, data_template


class NaverWorksGroupType(Enum):
    Sports2i = 1
    Bigglz = 2


# 비글즈 직원의 네이버 웍스 아이디를 가져옴
def get_staff_id_list():
    result = sessions['black'].query(WorksMember.works_member_id).filter(
        WorksMember.works_type_cd == NaverWorksGroupType.Bigglz.value).all()

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

    result = date.strftime("[마음의 소리] %Y년 %m월 %d일")
    return result


# 메일 본문의 인트로 텍스트를 가져옴
def get_intro_text(email_contents):
    return f'총 {len(email_contents)}건의 마음의 소리가 등록되었습니다.'


# 이메일 템플릿을 설정함
def set_email_template(date, email_contents):
    # 데이터 템플릿에 마음의 소리 내용을 매핑함
    user_data = ''.join([data_template.format(nickname=data[0], message=data[1], date=data[2])
                        for data in email_contents])

    # 이메일 템플릿에 전체 데이터를 매핑함
    result = email_template.format(date=date.strftime("%Y-%m-%d"),
                                   intro_text=get_intro_text(email_contents), data_list=user_data)

    return result


# 이메일 내용을 생성함
def create_email_body(date: str = None):
    user_feedback = get_sound_of_heart(date)
    result = set_email_template(date, user_feedback)

    return result


# AWS SES 서비스를 이용해 메일을 전송함
def send_email(date: str = None):
    receiver_email_list = get_email_receivers()
    subject = get_email_subject(date)
    body = create_email_body(date)

    send_ses_email(subject, body, receiver_email_list)
