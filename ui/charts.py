import matplotlib.pyplot as plt

def plot_capital(no_fee, with_fee):
    fig, ax = plt.subplots()
    ax.plot(no_fee, label="Sans frais de gestion")
    ax.plot(with_fee, label="Avec frais de gestion")
    ax.set_xlabel("Mois")
    ax.set_ylabel("Capital ($)")
    ax.legend()
    return fig
