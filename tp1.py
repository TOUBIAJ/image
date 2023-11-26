
   
import cv2
import numpy as np
import matplotlib.pyplot as plt



def calculate_histogram(image):
    histogram = np.zeros(256, dtype=int)
    for row in image:
        for pixel in row:
            histogram[pixel] += 1 

    return histogram




image = cv2.imread ('/home/joe/Downloads/Images/lena.png')


histogram = calculate_histogram(image)

total_pixels = image.size
normalisation = histogram /total_pixels

plt.figure()
plt.title('Histogramme de l\'image en niveaux de gris')
plt.xlabel('Niveaux de gris')
plt.ylabel('Nombre de pixels')
plt.plot(normalisation)
plt.xlim([0, 256])
plt.show()





def etirement(image, a, b):
    min = np.min(image)
    max = np.max(image)
    
    i2= (b - a) * (image - min) / (max - min) + a
    i2 = np.clip(i2, a, b)
    
    return i2


a = int(input("Entrez la valeur minimale apres etirement : "))
b = int(input("Entrez la valeur maximale apres etirement : "))

i2 = etirement(image, a, b)

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.title('Image originale')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(122)
plt.title('Image apres etirement dhistogramme')
plt.imshow(i2, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()



def egalisation(image):
    
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_norm = cdf * hist.max() / cdf.max()

    #image2 = ((2 ** image.max() - 1) * cdf_norm[image] / (image.shape[0] * image.shape[1]))
    image2 = cv2.equalizeHist(image)
    
    return image2

image2 = egalisation(image)

   
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.title('Image originale')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(122)
plt.title('Image apres egalisation')
plt.imshow(image2, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()


"""
algo de filterage
1. Pour chaque pixel (x, y) de l'image :
   a. Initialiser une variable somme a zero.
   b. Pour i allant de -1 à 1 :
      Pour j allant de -1 à 1 :
         i.   Récupérer la valeur du pixel dans le voisinage de (x+i, y+j) de l'image en multipliant
              cette valeur par le coefficient correspondant du filtre : 
              pixel_value = image[x+i, y+j] * filter[i+1][j+1] 
         ii.  Ajouter pixel_value à la somme.
   c. Attribuer la valeur somme au pixel (x, y) de l'image de sortie.
2. Répéter le processus pour chaque pixel de l'image.
"""