import queue
from logger import logger
from vk.users import get_all_users
from vk.sender import send_vk_message

task_queue = queue.Queue()


def worker():
    logger.info("Worker запущен")

    while True:
        task = task_queue.get()

        if task is None:
            break

        message = task['message']
        users = get_all_users()

        if not users:
            logger.warning("Нет пользователей для рассылки")
        else:
            for uid in users:
                send_vk_message(uid, message)

        task_queue.task_done()