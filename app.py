import subprocess

def start_mlflow_server(host="0.0.0.0", port=8000, backend_uri="sqlite:///mlflow.db", artifact_root="./mlruns"):
    """
    Starts an MLflow tracking server with authentication using --app-name basic-auth.
    
    :param host: Host address to bind the MLflow server to.
    :param port: Port to run the MLflow server on.
    :param backend_uri: URI for the backend store (default: SQLite database).
    :param artifact_root: Path for storing artifacts.
    :param username: Username for basic authentication.
    :param password: Password for basic authentication.
    """
    try:
        command = [
            "mlflow", "server",
            "--host", host,
            "--port", str(port),
            "--app-name", "basic-auth",
            "--backend-store-uri", backend_uri,
            "--default-artifact-root", artifact_root
        ]
        print(f"Starting MLflow server at {host}:{port} with authentication...")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting MLflow server: {e}")

if __name__ == "__main__":
    start_mlflow_server()
