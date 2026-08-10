from fastapi import FastAPI, Depends
from .schemas import IntentRequest, ApiResponse
from .security import api_key_security
from .actions import search_product_action

app = FastAPI(
    title="Synapse - Conversational API",
    description="An API for AI agents to interact with web services.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Synapse API"}


@app.post("/intent", response_model=ApiResponse)
def handle_intent(request: IntentRequest, authorized: bool = Depends(api_key_security)):
    """
    Main endpoint to handle agent intentions.
    """
    if request.action == "search_product":
        return search_product_action(request.query)

    # Handle unknown actions
    return ApiResponse(
        status="error",
        action_taken="unknown_action",
        message=f"Action '{request.action}' is not supported.",
        data=None
    )
