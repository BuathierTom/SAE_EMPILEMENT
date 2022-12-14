import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def moyenne(image: list):
    """
    Fonction qui fais la moyenne des couleurs des images données en paramètre. 

    Args:
        image (list): chemin de l'image 
    """
    image_list = []
    
    for i in range(len(image)):
        hdu_img = fits.open(image[i])
        hdu_img.info()
        #-------------- Recuperation de la data de l'image --------------
        image_data = hdu_img[0].data #type: ignore
        #-------------- Affichage de chaque image avant la moyenne --------------
        plt.imshow(image_data)
        plt.show(block=True)
        hdu_img.close()
        #-------------- On rajoute la data dans une liste pour la concatener plus tard --------------
        image_list.append(image_data)
    #-------------- Moyenne des couleurs et affichages --------------
    final_image = np.zeros(shape=image_list[0].shape)
    for image in image_list:
        final_image += image
    #-------------- Affichage de l'image empilés --------------
    plt.imshow(final_image)
    plt.colorbar()
    plt.show(block=True)
    
def median(image: list):
    """
    Fonction qui fais la median des couleurs des images données en paramètre. 

    Args:
        image (list): chemin de l'image 
    """
    image_list = []
    
    for i in range(len(image)):
        hdu_img = fits.open(image[i])
        hdu_img.info()
        #-------------- Recuperation de la data de l'image --------------
        image_data = hdu_img[0].data #type: ignore
        #-------------- Affichage de chaque image avant la moyenne --------------
        plt.imshow(image_data)
        plt.show(block=True)
        hdu_img.close()
        #-------------- On rajoute la data dans une liste pour la concatener plus tard --------------
        image_list.append(image_data)
        print(image_data)
    #-------------- Moyenne des couleurs et affichages --------------
    final_image = np.median(image_list, axis=0)
    #-------------- Affichage de l'image empilés --------------
    plt.imshow(final_image)
    plt.colorbar()
    plt.show(block=True)
        
if __name__ == '__main__':
    # Chemins a changer si ça ne fonctionne pas ou si vous voulez voir d'autre images
    
    images = ['./fits_tests/mini/mini0.fits', './fits_tests/mini/mini1.fits']
    print(moyenne(images))
    print(median(images))
    
    
    