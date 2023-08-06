S_CRM_LEAD_CREATE = {
    "order_lines": {
        "type": "list",
        "empty": True,
        "schema": {
            "type": "dict",
            "schema": {
                "product_id": {"type": "integer", "required": True},
                "quantity": {"type": "integer", "required": True}
            }
        }
    }
}
