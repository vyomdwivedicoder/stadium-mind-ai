from typing import Any
from services.ai_service import ai_service
from utils.logger import logger

class RuleEngine:
    """
    Responsible for deciding how every incident
    should be handled.
    """
    def evaluate(
        self,
        incident: dict[str, Any]
    ) -> dict:
        severity = incident["severity"]

        if severity <= 3:
            return self._low_priority(
                incident
            )

        if severity <= 6:
            return self._medium_priority(
                incident
            )

        if severity <= 8:
            return self._high_priority(
                incident
            )

        return self._critical_priority(
            incident
        )

    def _low_priority(
        self,
        incident: dict
    ) -> dict:
        logger.info(
            f"LOW priority incident #{incident['id']}"
        )
        return {
            "incident_id": incident["id"],
            "priority": "LOW",
            "requires_ai": False,
            "dispatch_team": "Operations",
            "estimated_response": "10 minutes",
            "recommended_action":
                "Monitor the situation.",
            "ai_analysis": None

        }

    def _medium_priority(
        self,
        incident: dict
    ) -> dict:
        logger.info(
            f"MEDIUM priority incident #{incident['id']}"
        )

        return {
            "incident_id": incident["id"],
            "priority": "MEDIUM",
            "requires_ai": False,
            "dispatch_team": "Security Team",
            "estimated_response": "5 minutes",
            "recommended_action":
                "Dispatch nearest response team.",
            "ai_analysis": None
        }


    def _high_priority(
        self,
        incident: dict
    ) -> dict:
        logger.info(
            f"HIGH priority incident #{incident['id']}"
        )
        analysis = ai_service.analyze(
            incident
        )

        return {
            "incident_id": incident["id"],
            "priority": "HIGH",
            "requires_ai": True,
            "dispatch_team": "Emergency Response",
            "estimated_response": "2 minutes",
            "recommended_action":
                analysis["recommended_action"],
            "ai_analysis": analysis
        }

    def _critical_priority(
        self,
        incident: dict
    ) -> dict:
        logger.warning(
            f"CRITICAL incident #{incident['id']}"
        )
        analysis = ai_service.analyze(
            incident
        )
        return {
            "incident_id": incident["id"],
            "priority": "CRITICAL",
            "requires_ai": True,
            "dispatch_team": "AI Command Center",
            "estimated_response": "Immediate",
            "recommended_action":
                analysis["recommended_action"],
            "ai_analysis": analysis
        }

rule_engine = RuleEngine()