import boto3
from utils.config import config
from botocore.exceptions import ClientError

aws_config = config.get_config("AWS")


def get_ses_server_info():
    # AWS 계정 및 리전 설정
    aws_access_key = aws_config['ACCESS_KEY']
    aws_secret_key = aws_config['SECRET_KEY']
    aws_region = aws_config['REGION']

    # SES 인스턴스 생성
    result = boto3.client('ses', aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key, region_name=aws_region)
    return result


def send_ses_email(subject, body, receiver_list):
    ses = get_ses_server_info()

    # SES 서버에 연결 및 이메일 발송
    sender = 'suim0331@bigglz.com'  # 보낸 사람의 이메일 주소
    try:
        response = ses.send_email(
            Source=sender,
            Destination={
                'ToAddresses': receiver_list,
            },
            Message={
                'Subject': {
                    'Data': subject,
                },
                'Body': {
                    'Text': {
                        'Data': body,
                    },
                },
            },
        )
        print(f"Email sent! Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email: {e}")
