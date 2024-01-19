# Requirements

-   Python 3.10 이상
-   VSCode 확장 : `Microsoft Python` 설치

```bash
# Windows OS 기준

# 파이썬 버전 확인
python --version

# powershell 터미널을 관리자 권한을 기본으로 설정하기 위해
# 관리자 권한으로 터미널에 접속해서 입력
Set-ExecutionPolicy RemoteSigned

# 파이썬 venv가상환경 생성
python -m venv .venv

# 가상환경 접속
. .venv/Scripts/activate.ps1

# pip 업그레이드
python -m pip install --upgrade pip

# 프로젝트 다운 후 빌드하고 실행할 패키지 최초 1회 설치 명령어
pip install -r requirements.txt

# 신규 패키지 설치 명령어
pip install [LIBRARY_NAME]

# 신규 설치된 패키지 Export
pip freeze > requirements.txt

# 프로젝트 실행
# 배포서버 옵션 --proxy-headers --forwarded-allow-ips='*'
uvicorn main:app --host 127.0.0.1 --port 8000

```
