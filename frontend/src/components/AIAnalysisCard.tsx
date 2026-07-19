interface Props {
    summary: string;
    risk: string;
    action: string;
}

function AIAnalysisCard({
    summary,
    risk,
    action
}: Props) {
    return (
        <div className="ai-card">
            <h3>
                🤖 AI Analysis
            </h3>
            <p>
                {summary}
            </p>
            <p>
                Risk:
                {" "}
                <strong>
                    {risk}
                </strong>
            </p>
            <p>
                {action}
            </p>
        </div>
    );
}

export default AIAnalysisCard;