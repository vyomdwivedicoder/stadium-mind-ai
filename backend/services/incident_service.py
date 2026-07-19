from datetime import datetime
from models.incident_models import IncidentCreate
_incidents = []
_counter = 1

class IncidentService:
    @staticmethod
    def create(
        incident: IncidentCreate
    ):
        global _counter
        new = {
            "id": _counter,
            "type": incident.type,
            "location": incident.location,
            "severity": incident.severity,
            "description": incident.description,
            "status": "ACTIVE",
            "created_at": datetime.utcnow()
        }
        _incidents.append(new)
        _counter += 1
        return new
    @staticmethod
    def get_all():
        return _incidents
    @staticmethod
    def get(
        incident_id: int
    ):
        return next(
            (
                item
                for item in _incidents
                if item["id"] == incident_id
            ),
            None
        )