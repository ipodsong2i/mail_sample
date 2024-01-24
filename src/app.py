from flask import Flask
from flask_restx import Api
from routers.mail_router import Scheduler
from utils.config import config

# 플라스크 앱 생성
app = Flask(__name__)

# API Setting config에서 가져오기
api_config = config.get_config("API_SETTING")

# API 설정
api = Api(
    app,
    version=api_config["VERSION"],
    title=api_config["TITLE"],
    prefix='/api',
    description=api_config["DESCRIPTION"],
    doc="/",
)

api.add_namespace(Scheduler, '/scheduler')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
