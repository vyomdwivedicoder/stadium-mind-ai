interface Props {
    message: string;
}

function ErrorBanner({
    message
}: Props) {
    return (
        <div className="error-banner">
            {message}
        </div>
    );
}

export default ErrorBanner;