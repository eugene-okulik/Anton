# Json schema for check response lesson_18


json_schema_create = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "year": {
                    "type": "integer"
                },
                "price": {
                    "type": "number",
                    "format": "float"
                },
                "CPU model": {
                    "type": "string"
                },
                "Hard disk size": {
                    "type": "string"
                }
            },
            "required": [
                "year",

                "CPU model",
                "Hard disk size"
            ]
        },
    },
    "required": [
        "id",
        "name",
        "data",
        "createdAt"
    ],
    "additionalProperties": False
}
json_schema_update = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "year": {
                    "type": "integer"
                },
                "price": {
                    "type": "number",
                    "format": "float"
                },
                "CPU model": {
                    "type": "string"
                },
                "Hard disk size": {
                    "type": "string"
                },
                "color": {
                    "type": "string"
                }
            },
            "required": [
                "year",
                "price",
                "CPU model",
                "Hard disk size",
                "color"
            ],
            "additionalProperties": False
        }
    },
    "required": [
        "id",
        "name",
        "updatedAt",
        "data"
    ],
    "additionalProperties": False
}
json_schema_update_patch = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "year": {
                    "type": "integer"
                },
                "price": {
                    "type": "number",
                    "format": "float"
                },
                "CPU model": {
                    "type": "string"
                },
                "Hard disk size": {
                    "type": "string"
                }
            },
            "required": [
                "year",
                "price",
                "CPU model",
                "Hard disk size"

            ],
            "additionalProperties": False
        }
    },
    "required": [
        "id",
        "name",
        "updatedAt",
        "data"
    ],
    "additionalProperties": False
}
