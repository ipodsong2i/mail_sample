#####################################################################
# Config 모듈
#####################################################################

import json

# config 파일 경로 세팅
config_path = 'configs/config.json'


class Config():
    def __init__(self) -> None:
        with open(config_path, 'r', encoding='UTF8') as f:
            self.config = json.load(f)

    def get_config(self, config_name):
        try:
            keys = config_name.split('.')  # 입력된 문자열을 점으로 나누어 리스트로 변환
            value = self.config
            for key in keys:
                value = value[key]  # 중첩된 딕셔너리에서 값을 가져오기
            return value
        except (KeyError, TypeError):
            return None


config = Config()
