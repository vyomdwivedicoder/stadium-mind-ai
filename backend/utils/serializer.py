from datetime import datetime

def serialize(data):
    if isinstance(data, dict):
        return {
            key: serialize(value)
            for key, value in data.items()
        }
    if isinstance(data, list):
        return [
            serialize(item)
            for item in data
        ]
    if isinstance(data, datetime):
        return data.isoformat()
    return data