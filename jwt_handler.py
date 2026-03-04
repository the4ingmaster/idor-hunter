import jwt


def decode_jwt(token):

    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except:
        return None


def mutate_jwt_ids(payload):

    mutations = []

    for key in payload:

        if "id" in key.lower():

            base = payload[key]

            if isinstance(base, int):

                payload_copy = payload.copy()
                payload_copy[key] = base + 1
                mutations.append(payload_copy)

                payload_copy = payload.copy()
                payload_copy[key] = base + 10
                mutations.append(payload_copy)

    return mutations