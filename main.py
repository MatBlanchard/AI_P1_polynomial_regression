import numpy as np
import matplotlib.pyplot as plt

# Paramètres
noise = 0.2
nb_points = 10**5
polynomial_degree = 1

# Générer un nuage de point bruité
x = np.linspace(0, 1, nb_points)
coefficients = np.random.uniform(-0.1, 0.1, polynomial_degree+1)
func = np.polyval(coefficients, x)
y1 = np.random.normal(func, noise*max(abs(func)), nb_points)

# Trouver la courbe de tendance
y2 = np.polyval(np.polyfit(x, y1, polynomial_degree), x)


# Afficher les courbes
plt.scatter(x, y1, s=10**4/nb_points)
plt.plot(x, y2, 'r')
plt.get_current_fig_manager().full_screen_toggle()
plt.show()


