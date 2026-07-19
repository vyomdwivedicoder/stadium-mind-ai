from uuid import uuid4

def generate_event_id():
    return str(
        uuid4()
    )

def severity_color(level: int):
    if level >= 9:
        return "critical"
    if level >= 7:
        return "high"
    if level >= 4:
        return "medium"
    return "low"