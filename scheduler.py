import os
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import cleanup_old_messages

def start_scheduler():
    if os.getenv("HF_SPACE") == "true":
        return

    scheduler = BackgroundScheduler()
    scheduler.add_job(cleanup_old_messages, "interval", days=1)
    scheduler.start()
