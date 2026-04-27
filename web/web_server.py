from flask import Flask, request
from urllib.parse import parse_qs

from logger import logger
from parser.formatter import format_message
from worker.queue_worker import task_queue
from config import MAX_MESSAGE_LENGTH

app = Flask(__name__)


@app.route('/event', methods=['POST'])
def handle_event():
    data = request.get_data(as_text=True)

    if not data:
        logger.warning("Пустой POST")
        return "Empty", 400

    logger.debug(f"RAW: {data[:500]}")

    parsed_raw = parse_qs(data, keep_blank_values=True)
    parsed = {k: v[0] for k, v in parsed_raw.items()}

    if not parsed:
        return "No data", 200

    message_text = format_message(parsed)

    if len(message_text) > MAX_MESSAGE_LENGTH:
        message_text = message_text[:MAX_MESSAGE_LENGTH] + "\n…(обрезано)"

    task_queue.put({'message': message_text})

    return "OK", 200


@app.route('/health', methods=['GET'])
def health():
    return "OK", 200