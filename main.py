import threading
from logger import logger
from config import HTTP_HOST, HTTP_PORT
from worker.queue_worker import worker
from web.web_server import app


def main():
    logger.info("=== Запуск VK бота ===")

    threading.Thread(target=worker, daemon=True).start()

    app.run(
        host=HTTP_HOST,
        port=HTTP_PORT,
        threaded=True
    )


if __name__ == "__main__":
    main()