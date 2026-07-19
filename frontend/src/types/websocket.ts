import type { Incident } from "./incident";
import type { Decision } from "./decision";

export interface WebSocketEvent {
    type: string;
    payload: {
        incident: Incident;
        decision: Decision;
    };
}