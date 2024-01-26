from enums.type import NaverWorksGroupType
from datetime import datetime
from models.black import WorksMember
from models.red import Member, TheSoundOfHeart
from template import email_template, data_template
from utils.config import config
from utils.mail import Mail
from utils.database import db


mail_config = config.get_config("AWS")
mail_config.update(config.get_config("MAIL"))
mail = Mail(mail_config)


# 이메일 수신 리스트를 생성함
def get_email_receivers():
    # 비글즈 직원의 네이버 웍스 아이디를 가져옴
    session = next(db['black']()) # 안되면 next 제거
    id_list = session.query(WorksMember.works_member_id).filter(
        WorksMember.works_type_cd == NaverWorksGroupType.Bigglz.value).all()
    
    # 이메일 수신 리스트 생성   
    result = [id[0].strip("'") + '@bigglz.com' for id in id_list]
        
    return result


# 이메일 제목을 생성함
def get_email_subject(date: str = None):
    if not date:
        date = datetime.now()

    result = date.strftime("[마음의 소리] %Y년 %m월 %d일")
    return result


# 이메일 내용을 생성함
def create_email_body(date: str = None):
    reg_dt = date.strftime("%Y-%m-%d")
    
    # DB에서 유저 피드백 가져옴
    session = next(db['red']()) # 안되면 next 제거
    user_feedback = session.query(Member.nick_nm, TheSoundOfHeart.message_ct, TheSoundOfHeart.reg_dt).join(Member).filter(
        TheSoundOfHeart.reg_dt >= reg_dt + " 00:00:00",
        TheSoundOfHeart.reg_dt <= reg_dt + " 23:59:59"
    ).order_by(TheSoundOfHeart.the_sound_of_heart_se.asc()).all()

    # 데이터 템플릿에 마음의 소리 내용을 매핑함
    user_data = ''.join([data_template.format(nickname=data[0], message=data[1], date=data[2])
                        for data in user_feedback])

    # 인트로 텍스트 생성
    intro_text = f'총 {len(user_feedback)}건의 마음의 소리가 등록되었습니다.'

    # 이메일 템플릿에 전체 데이터를 매핑함
    result = email_template.format(date=date.strftime("%Y-%m-%d"),
                                   intro_text=intro_text, data_list=user_data)

    return result


# AWS SES 서비스를 이용해 메일을 전송함
def send_email(date: str = None):
    receiver_email_list = get_email_receivers()
    subject = get_email_subject(date)
    body = create_email_body(date)

    mail.send_ses_email(subject, body, receiver_email_list)
