import threading
import schedule
import time

from agents.mail import send_email

def start_scheduler():
    def works():
        # 매일 오전 9시에 이메일 발송
        schedule.every().day.at("09:00").do(send_email)

        while True:
            schedule.run_pending()
            time.sleep(1)
        
     # 스레드 생성
    scheduler_thread = threading.Thread(target=works)

    # 데몬 스레드로 설정하여 메인 프로세스 종료시 함께 종료되도록 함
    scheduler_thread.daemon = True

    # 스레드 시작
    scheduler_thread.start()
        

def stop_scheduler():
    schedule.clear()


def get_scheduler_status():
    jobs = schedule.get_jobs()
    status_strings = [f"Next Run: {job.next_run}" for job in jobs]
    return status_strings