from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(date: str = None):
    sender_email = ""
    password = ""
    
    receiver_email_list = get_receiver_list()

    if date:
        subject = f"{date} 제목제목제목"
    else:
        date = datetime.now()
        date_string = date.strftime("%Y%m%d")
        subject = f"{date_string} 제목제목제목"
    
    body = get_body(date)

    # SMTP 서버에 연결 및 이메일 발송
    # TODO : 비글즈 smtp 서버로 바꾸기
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        
        for receiver_email in receiver_email_list:
            message = create_email(sender_email, receiver_email, subject, body)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
        
def get_receiver_list():
    result = []
    # TODO : DB에서 이메일 리스트 가져오기
    
    return result


def get_body(date):
    result = ""
    # TODO : DB에서 데이터 가져 와 body 만들기
    
    return result

        
def create_email(sender_email, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))