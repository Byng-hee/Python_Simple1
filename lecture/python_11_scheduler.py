# 스케줄러(Scheduler)
#  - 정해진 일정에 맞춰서 프로그램을 동작!
#  예) 12시간에 한번씩
#      5분마다
#      특정일에만(크리스마스)

# 스케줄러 + 프로그램 → 완성 → 서버(동작)

# apscheduler
#  1.blocking
#   - 스케줄러 + 프로그래만 동작
#  2.background
#   - 동작은 하되 뒤에서 조용히!

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def print_now():
    print(datetime.now())

def print_love():
    print("I LOVE YOU")

# 1. 스케줄러 생성
scheduler =  BlockingScheduler()

# 2. 스케줄러 등록(일, 주기, 5초)
# -  date : 특정일, 특정날짜에만 동작
# -  interval : 간격별로(5초, 10분, 1시간)
# -  CRON(*) : 만능(매일 특정 시간에~)
scheduler.add_job(print_now, "interval", seconds=5)
scheduler.add_job(print_love, "cron", hour=13, minute=16)

# 3. 스케줄러 실행
scheduler.start()

# 임의로 work
while True:
    time.sleep(1)