import uuid

def is_numeric(v):
    try:
        int(v)
        return True
    except:
        return False


def generate_numeric_variants(v):

    base = int(v)

    return [
        base - 1,
        base + 1,
        base + 2,
        base + 5,
        base + 10,
        base + 50,
        base + 100
    ]


def generate_uuid_variants():

    variants = []

    for _ in range(10):
        variants.append(str(uuid.uuid4()))

    return variants
