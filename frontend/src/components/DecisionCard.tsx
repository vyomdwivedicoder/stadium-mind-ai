interface Props {
    decision: string;
    action: string;
}

function DecisionCard({
    decision,
    action
}: Props) {
    return (
        <div className="decision-card">
            <h3>
                Decision Engine
            </h3>
            <p>
                <strong>
                    {decision}
                </strong>
            </p>
            <p>
                {action}
            </p>
        </div>
    );
}

export default DecisionCard;