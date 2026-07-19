const BASE_URL = "http://127.0.0.1:8000";

export async function getIncidents() {
    const response =
        await fetch(
            `${BASE_URL}/incidents/`
        );
    return response.json();
}