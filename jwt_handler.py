import jwt


def decode_token(token):

    try:
        payload = jwt.decode(token,options={"verify_signature":False})
        return payload
    except:
        return None


def mutate_jwt(payload):

    mutations = []

    for k,v in payload.items():

        if "id" in k.lower() and isinstance(v,int):

            p = payload.copy()
            p[k] = v + 1
            mutations.append(p)

            p = payload.copy()
            p[k] = v + 10
            mutations.append(p)
