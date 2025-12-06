import matplotlib.pyplot as plt

def plot_line(df, x, y, save_path=None):
    plt.figure()
    plt.plot(df[x], df[y], marker='o')
    plt.xlabel(x); plt.ylabel(y)
    plt.title(f'{y} over {x}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def plot_bar(df, x, y, save_path=None):
    plt.figure()
    plt.bar(df[x].astype(str), df[y])
    plt.xlabel(x); plt.ylabel(y)
    plt.title(f'{y} by {x}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
