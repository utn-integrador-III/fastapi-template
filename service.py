from fastapi import FastAPI, Path, HTTPException

def addServiceLayer(api: FastAPI):
    # Health
    @api.add_api_route("/health", methods=["GET"], response_model=dict)
    def health_check():
        return {"status": "ok"}