export interface Decision {
    incident_id: number;
    decision: string;
    action: string;
    requires_ai: boolean;
    ai_analysis?: {
        summary: string;
        risk_level: string;
        recommended_action: string;
        predicted_outcome: string;
    };
}