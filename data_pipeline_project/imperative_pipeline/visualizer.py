import matplotlib.pyplot as plt

def plot_line(rows, x_key, y_key, save_path=None):
    x = [r[x_key] for r in rows]
    y = [float(r[y_key]) for r in rows]

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(f"{y_key} over {x_key}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def plot_bar(rows, x_key, y_key, save_path=None):
    """
    Imperative version: rows = list of dicts
    """
    x = [str(r[x_key]) for r in rows]
    y = [float(r[y_key]) for r in rows]

    plt.figure()
    plt.bar(x, y)
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(f"{y_key} by {x_key}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
