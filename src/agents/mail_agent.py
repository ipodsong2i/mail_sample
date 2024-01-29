import threading
import schedule
import time
from engines.mail_engine import send_email


# 스케쥴러 시작
def start_scheduler():
    def works():
        # 매일 오전 10시에 어제 날짜의 마음의 소리 발송
        schedule.every().day.at("10:00").do(send_email)

        while True:
            schedule.run_pending()
            time.sleep(1)

    # 스레드 생성
    scheduler_thread = threading.Thread(target=works)

    # 데몬 스레드로 설정하여 메인 프로세스 종료시 함께 종료되도록 함
    scheduler_thread.daemon = True

    # 스레드 시작
    scheduler_thread.start()


# 스케쥴러 중단
def stop_scheduler():
    schedule.clear()


# 스케쥴러 상태
def get_scheduler_status():
    jobs = schedule.get_jobs()
    status_strings = [f"Next Run: {job.next_run}" for job in jobs]
    return status_strings
