import type {
    WebSocketEvent
} from "../types/websocket";

export function connectWebSocket(
    onMessage: (
        event: WebSocketEvent
    ) => void
) {
    const socket =
        new WebSocket(
            "ws://127.0.0.1:8000/ws"
        );
    socket.onopen = () => {
        console.log(
            "Connected"
        );
    };
    socket.onmessage = (event) => {
        const data =
            JSON.parse(
                event.data
            );
        onMessage(data);
    };
    socket.onerror = console.error;
    return socket;
}