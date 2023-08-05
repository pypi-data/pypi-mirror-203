def parse_strs(text: str) -> list[str]:
    return [i.strip() for i in text.strip().split(",")]


def parse_ints(text: str) -> list[int]:
    return [int(i) for i in parse_strs(text)]
