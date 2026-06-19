import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

dragon = mpimg.imread('dragon.jpg', 'rgb')
print(dragon.shape)

def niveau_gris(image):
    l, c, p = image.shape  # on récupère ses dimensions
    M = np.zeros((l, c))   # on crée une nouvelle image en niveaux de gris de mêmes dimensions
    for i in range(l):
        for j in range(c):
            R, G, B = image[i, j, 0], image[i, j, 1], image[i, j, 2]  # on récupère les trois composantes RGB
            P = R*0.3 + G*0.3 + B*0.3  # on calcule leur moyenne
            M[i, j] = P          # on modifie la valeur
    return M


# Exemple d'utilisation :
dragon_gris = niveau_gris(dragon)
# plt.imshow(dragon_gris, cmap='gray')
# plt.axis('off')
# plt.show()

def inverser(image):
    # Cette fonction sert à inverser les couleurs d'une image en niveaux de gris
    image3 = image.copy()
    # image3 = 255 - image3 
    # return image3
    for i in range(len(l)):
        for j in range(len(c)):
            image3[i][j]=255-image3[i][j]

# Exemple d'utilisation :
dragon_inver = inverser(dragon_gris)  # dragon_grid hiya l'image li khrjat men niveau_gris
plt.imshow(dragon_inver, cmap=plt.cm.gray)
plt.show()