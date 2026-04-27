import requests
from config import VK_ACCESS_TOKEN, VK_API_VERSION
from logger import logger


def send_vk_message(user_id: int, message_text: str) -> bool:
    if not VK_ACCESS_TOKEN:
        logger.error("VK_ACCESS_TOKEN не настроен!")
        return False

    url = "https://api.vk.com/method/messages.send"
    params = {
        "user_id": user_id,
        "random_id": 0,
        "message": message_text,
        "access_token": VK_ACCESS_TOKEN,
        "v": VK_API_VERSION
    }

    try:
        response = requests.post(url, params=params, timeout=10)
        data = response.json()

        if "error" in data:
            logger.error(f"VK error to {user_id}: {data['error']['error_msg']}")
            return False

        return True

    except Exception as e:
        logger.exception(f"Ошибка отправки VK: {e}")
        return False