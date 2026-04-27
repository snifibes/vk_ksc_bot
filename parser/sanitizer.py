import re


def remove_hashes(text: str) -> str:
    text = re.sub(r"SHA256:\s*[A-Fa-f0-9]{64}", "", text)
    text = re.sub(r"MD5:\s*[A-Fa-f0-9]{32}", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()