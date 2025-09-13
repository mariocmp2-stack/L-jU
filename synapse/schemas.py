from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class IntentRequest(BaseModel):
    """
    Represents the request from an external agent.
    It defines the "intention" of the agent.
    """
    action: str = Field(
        ...,
        description="The action the agent wants to perform, e.g., 'search_product', 'get_product_details'.",
        examples=["search_product"]
    )
    query: Optional[str] = Field(
        None,
        description="The main natural language query, e.g., 'vegan protein without gluten'.",
        examples=["vegan protein without gluten"]
    )
    parameters: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional structured parameters to refine the action."
    )


class Product(BaseModel):
    """
    Represents a product item.
    """
    name: str
    price: float
    url: str
    in_stock: bool


class ApiResponse(BaseModel):
    """
    Represents the structured response sent back by Synapse.
    """
    status: str = Field(
        ...,
        description="The status of the response, e.g., 'success', 'error'.",
        examples=["success"]
    )
    action_taken: str = Field(
        ...,
        description="The action that was actually performed by the API.",
        examples=["search_results"]
    )
    message: Optional[str] = Field(
        None,
        description="A human-readable message summarizing the result.",
        examples=["Found 2 products matching your query."]
    )
    data: Optional[Any] = Field(
        None,
        description="The data payload of the response. The structure depends on the action taken."
    )
