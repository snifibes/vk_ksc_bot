from parser.sanitizer import remove_hashes


def format_message(parsed: dict) -> str:
    severity = parsed.get("SEVERITY", "").lower()

    severity_map = {
        "критическое": "🔴 КРИТИЧЕСКОЕ СОБЫТИЕ",
        "ошибка": "🟠 Ошибка",
        "предупреждение": "🟡 Предупреждение",
        "информационное": "🔵 Информация"
    }

    header = severity_map.get(severity, "🔔 Событие")

    computer = parsed.get("COMPUTER", "Неизвестно")
    event = parsed.get("EVENT", "")
    descr = remove_hashes(parsed.get("DESCR", ""))
    time_ = parsed.get("RISE_TIME", "")

    product = parsed.get("KL_PRODUCT", "")
    version = parsed.get("KL_VERSION", "")
    task = parsed.get("KLCSAK_EVENT_TASK_DISPLAY_NAME", "")

    ip = parsed.get("HOST_IP", "")
    conn_ip = parsed.get("HOST_CONN_IP", "")

    parts = [header]
    parts.append(f"💻 {computer}")

    if event:
        parts.append(f"📌 {event}")

    if descr:
        parts.append(f"\n📝 {descr}")

    details = []
    if product:
        details.append(product + (f" {version}" if version else ""))
    if task:
        details.append(f"Задача: {task}")
    if time_:
        details.append(f"⏱ {time_}")

    if details:
        parts.append("\n" + "\n".join(details))

    network = []
    if ip:
        network.append(f"IP: {ip}")
    if conn_ip:
        network.append(f"Conn: {conn_ip}")

    if network:
        parts.append("\n🌐 " + " | ".join(network))

    return "\n".join(parts)