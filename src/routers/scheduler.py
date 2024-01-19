from flask import jsonify
from flask_restx import Resource, Namespace
from agents.agent import get_scheduler_status, start_scheduler, stop_scheduler
from agents.mail import send_email
from utils.log import logger

Scheduler = Namespace('Scheduler')

@Scheduler.route('/start-scheduler')
class StartScheduler(Resource):
    def post(self):
        try:
            # 백그라운드 스케줄러 시작
            start_scheduler()
            data = {'status': 200}
        
        except Exception as e:
            logger.error(e)
            data = {'status': 500, 'message' : 'Internal Server Error'}
            
        return jsonify(data)


@Scheduler.route('/stop-scheduler')
class StopScheduler(Resource):
    def post(self):
        try:
            # 백그라운드 스케줄러 중단
            stop_scheduler()
            data = {'status': 200}
        
        except Exception as e:
            logger.error(e)
            data = {'status': 500, 'message' : 'Internal Server Error'}
            
        return jsonify(data)
    

@Scheduler.route('/check-scheduler')
class CheckScheduler(Resource):
    def get(self):
        try:
            # 백그라운드 스케줄러 상태확인
            status = get_scheduler_status()
            data = {'status': 200, 'data': status}
        
        except Exception as e:
            logger.error(e)
            data = {'status': 500, 'message' : 'Internal Server Error'}
            
        return jsonify(data)
    

@Scheduler.route('/send/<string:date>')
class Send(Resource):
    def post(self, date):
        try:
            send_email(date)
            data = {'status': 200}
        
        except Exception as e:
            logger.error(e)
            data = {'status': 500, 'message' : 'Internal Server Error'}
            
        return jsonify(data)