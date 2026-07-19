interface Props {
    total: number;
}

function StatusBar({
    total
}: Props) {
    return (
        <div className="status-bar">
            <strong>
                Active Incidents
            </strong>
            <span>
                {total}
            </span>
        </div>
    );
}

export default StatusBar;