from .schemas import Product, ApiResponse

def search_product_action(query: str) -> ApiResponse:
    """
    Mock logic for searching products.
    """
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
        message=f"Found {len(mock_products)} products matching your query: '{query}'.",
        data=mock_products
    )
