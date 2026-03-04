ID_KEYS = [
"id",
"user",
"user_id",
"uid",
"account",
"account_id",
"order",
"order_id",
"uuid"
]

def discover_id_parameters(params):

    discovered = []

    for key in params:

        if any(word in key.lower() for word in ID_KEYS):
            discovered.append(key)

    return discovered