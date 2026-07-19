export interface Incident {
    id: number;
    type: string;
    location: string;
    severity: number;
    description: string;
    status: string;
    created_at: string;
}