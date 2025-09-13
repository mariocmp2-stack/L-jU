from fastapi import FastAPI, Depends
from .schemas import IntentRequest, ApiResponse, Product
from .security import api_key_security

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
        # Mock logic for searching products
        mock_products = [
            Product(
                name="Proteína Vegana SuperMix",
                price=45.99,
                url="/products/vegan-protein-supermix",
                in_stock=True
            ),
            Product(
                name="Suplemento de Proteína Eco",
                price=39.50,
                url="/products/eco-protein-supplement",
                in_stock=False
            ),
        ]
        return ApiResponse(
            status="success",
            action_taken="search_results",
            message=f"Found {len(mock_products)} products matching your query: '{request.query}'.",
            data=mock_products
        )

    # Handle unknown actions
    return ApiResponse(
        status="error",
        action_taken="unknown_action",
        message=f"Action '{request.action}' is not supported.",
        data=None
    )
