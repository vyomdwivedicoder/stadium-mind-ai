import SeverityBadge from "./SeverityBadge";
import type {
    Incident
} from "../types/incident";
interface Props {
  incident: Incident;
}

function IncidentCard({
  incident
}: Props) {
    return (
    <div className="incident-card">
      <div className="card-top">
          <h3>
            🚨 {incident.type}
          </h3>
          <SeverityBadge
            severity={
              incident.severity
            }
          />
      </div>
      <p>
        📍 {incident.location}
      </p>
      <p>
        {incident.description}
      </p>
      <p>
        Status:
        {" "}
        <strong>
          {incident.status}
        </strong>
      </p>
    </div>
  );
}

export default IncidentCard;