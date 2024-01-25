import boto3
from utils.config import config
from botocore.exceptions import ClientError

aws_config = config.get_config("AWS")


# AWS SED 서버 정보 가져옴
def get_aws_ses_info():
    # 서버 정보
    aws_access_key = aws_config['ACCESS_KEY']
    aws_secret_key = aws_config['SECRET_KEY']
    aws_region = aws_config['REGION']

    result = boto3.client('ses', aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key, region_name=aws_region)
    return result


# SES 서버에서 이메일 전송
def send_ses_email(subject, body, receiver_list):
    ses = get_aws_ses_info()

    try:
        response = ses.send_email(
            Source='suim0331@bigglz.com',
            Destination={
                'ToAddresses': receiver_list,
            },
            Message={
                'Subject': {
                    'Data': subject,
                },
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body,
                    },
                },
            },
        )
        print(f"Email sent! Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email: {e}")
