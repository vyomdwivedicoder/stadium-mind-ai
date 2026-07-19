from typing import List
from fastapi import WebSocket
import json
import logging

logger = logging.getLogger(
    "stadiummind.websocket"
)

class ConnectionManager:
    """
    Handles all active WebSocket connections.

    Responsibilities:
    - Accept new clients
    - Track active connections
    - Remove disconnected clients
    - Broadcast live stadium events
    """

    def __init__(self):

        self.active_connections: List[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket
    ):
        """
        Accept and store new websocket connection.
        """
        await websocket.accept()
        self.active_connections.append(
            websocket
        )

        logger.info(
            "WebSocket connected. Active clients: %s",
            len(self.active_connections)
        )

    def disconnect(
        self,
        websocket: WebSocket
    ):
        """
        Remove disconnected websocket.
        """
        if websocket in self.active_connections:

            self.active_connections.remove(
                websocket
            )

        logger.info(
            "WebSocket disconnected. Active clients: %s",
            len(self.active_connections)
        )

    async def broadcast(
        self,
        message: dict
    ):
        """
        Broadcast event to all connected dashboards.
        """
        disconnected = []

        logger.info(
            "Broadcasting event: %s",
            message.get("type")
        )

        for connection in self.active_connections:
            try:
                await connection.send_text(
                    json.dumps(
                        message,
                        default=str
                    )
                )
            except Exception as error:
                logger.error(
                    "WebSocket send failed: %s",
                    error
                )
                disconnected.append(
                    connection
                )

        # cleanup dead connections
        for connection in disconnected:
            self.disconnect(
                connection
            )

    def get_connection_count(self):
        return len(
            self.active_connections
        )

# Global manager instance
manager = ConnectionManager()