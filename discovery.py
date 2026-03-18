ID_KEYWORDS = [
"id",
"user",
"user_id",
"uid",
"account",
"account_id",
"order",
"order_id",
"uuid",
"customer",
"profile"
]


def discover_parameters(params):

    found = []

    for key in params:

        if any(k in key.lower() for k in ID_KEYWORDS):
            found.append(key)

    return found
