from fastapi import FastAPI

app = FastAPI(title="OceanShield Monitoring Platform")


@app.get("/")
def home():
    return {
        "message": "OceanShield Monitoring Platform is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/telemetry")
def telemetry():
    return {
        "asset_id": "CABLE-001",
        "asset_type": "Subsea Communication Cable",
        "temperature": 38,
        "signal_strength": 91,
        "pressure": 72,
        "status": "HEALTHY"
    }