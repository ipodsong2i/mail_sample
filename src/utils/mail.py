import boto3
from botocore.exceptions import ClientError
from utils.log import logger

class Mail():
    def __init__(self, mail_config):
        # boto3 클라이언트 설정
        access_key = mail_config['ACCESS_KEY']
        secret_key = mail_config['SECRET_KEY']
        region = mail_config['REGION']
        self.boto3_client = boto3.client('ses', aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key, region_name=region)
        
        self.source = mail_config['SOURCE']
    
    # SES 서버에서 이메일 전송
    def send_ses_email(self, subject, body, receiver_list):
        try:
            response = self.boto3_client.send_email(
                Source=self.source,
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
            logger.info(f"Email sent! Message ID: {response['MessageId']}")
        except ClientError as e:
            logger.error(f"Error sending email: {e}")