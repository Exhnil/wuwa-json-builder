import re
import unicodedata


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower().strip()
    value = re.sub(r"[']", "-", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip()
