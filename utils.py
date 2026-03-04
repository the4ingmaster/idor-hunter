import re
import uuid

UUID_PATTERN = r'[a-f0-9\-]{36}'

def is_uuid(value):
    return re.fullmatch(UUID_PATTERN, value.lower()) is not None


def generate_uuid_variants():
    variants = []
    for _ in range(10):
        variants.append(str(uuid.uuid4()))
    return variants


def is_numeric(value):
    try:
        int(value)
        return True
    except:
        return False


def generate_numeric_variants(value):

    base = int(value)

    return [
        base - 1,
        base + 1,
        base + 2,
        base + 5,
        base + 10,
        base + 50,
        base + 100
    ]