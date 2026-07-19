interface Props {
    severity: number;
}

function SeverityBadge({
    severity
}: Props) {
    let color =
        "#4caf50";
    if (severity >= 8)
        color = "#f44336";
    else if (severity >= 5)
        color = "#ff9800";
    return (
        <span
            style={{
                background: color,
                color: "white",
                padding: "5px 10px",
                borderRadius: "8px",
                fontWeight: 600
            }}
        >
            Severity {severity}
        </span>
    );
}

export default SeverityBadge;