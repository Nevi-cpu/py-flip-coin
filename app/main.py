import random

def flip_n_times(flips: int) -> int:
    heads = 0

    for _ in range(flips):
        flip = random.randint(0, 1)
        if flip == 1:
            heads += 1
    return heads


def flip_coin() -> dict:
    cases = 10000
    result = {head: 0 for head in range(0, 11)}

    for _ in range(cases):
        heads = flip_n_times(10)
        result[heads] += 1

    return {head: round(count / cases * 100, 2)
            for head, count in result.items()}

if __name__ == "__main__":
    data = flip_coin()
    print(data)
    print(data.values())
