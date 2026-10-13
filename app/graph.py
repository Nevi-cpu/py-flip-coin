import matplotlib.pyplot as plt
from main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    plt.bar(x, y)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage %")
    plt.title("Gaussian Distribution")
    plt.show()

if __name__ == "__main__":
    draw_gaussian_distribution_graph()
