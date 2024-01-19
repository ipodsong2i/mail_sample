import schedule
import time

from agents.mail import send_email

def start_scheduler():
    # 매일 오전 9시에 이메일 발송
    schedule.every().day.at("09:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

def stop_scheduler():
    schedule.clear()


def get_scheduler_status():
    return schedule.get_jobs()