import { useEffect, useState } from "react";

import Header from "../components/Header";
import StatusBar from "../components/StatusBar";
import IncidentCard from "../components/IncidentCard";
import Loading from "../components/Loading";

import { getIncidents } from "../services/api";
import { connectWebSocket } from "../services/websocket";

import type { Incident } from "../types/incident";

function Dashboard() {
    const [incidents, setIncidents] =
        useState<Incident[]>([]);
    const [loading, setLoading] =
        useState(true);
    useEffect(() => {
        async function loadIncidents() {
            const data =
                await getIncidents();
            setIncidents(
                data.data.incidents
            );
            setLoading(false);
        }
        loadIncidents();
        const socket =
            connectWebSocket((event) => {
                if (
                    event.type !==
                    "NEW_INCIDENT"
                )
                    return;
                const incident =
                    event.payload.incident;
                setIncidents((prev) => {
                    if (
                        prev.some(
                            i =>
                                i.id ===
                                incident.id
                        )
                    )
                        return prev;
                    return [
                        incident,
                        ...prev
                    ];
                });
            });
        return () =>
            socket.close();
    }, []);

    return (
        <div className="dashboard">
            <Header />
            <StatusBar
                total={
                    incidents.length
                }
            />
            {
                loading ?
                    <Loading />
                    :
                    incidents.map(
                        incident =>
                            <IncidentCard
                                key={
                                    incident.id
                                }
                                incident={
                                    incident
                                }
                            />
                    )
            }
        </div>
    );
}

export default Dashboard;