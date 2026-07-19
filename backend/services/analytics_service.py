from collections import Counter
from services.incident_service import IncidentService

class AnalyticsService:
    @staticmethod
    def dashboard():
        incidents = IncidentService.get_all()
        severities = [
            item["severity"]
            for item in incidents
        ]
        average = (
            sum(severities) / len(severities)
            if severities
            else 0
        )
        categories = Counter(
            item["type"]
            for item in incidents
        )
        return {
            "total_incidents": len(incidents),
            "average_severity": round(
                average,
                2
            ),
            "categories": dict(categories)
        }