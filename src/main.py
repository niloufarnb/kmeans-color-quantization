import matplotlib.pyplot as plt
from clustring import *
from quanize import *
import os

image = plt.imread('input.jpg')
input_file_size = os.path.getsize('input.jpg')
# Convert image to a 2D array of pixels
# 2D array will have a shape of (height * width, 3)
pixels = image.reshape(-1, 3)

k = input('value of k: (E for exit): ')
while k != 'E' and k != 'e':
    k = int(k)
    centroids, assignments = k_means(pixels, k)
    quantized_image = create_quantized_image(centroids, assignments, image.shape)
    if quantized_image.dtype != np.uint8:
        quantized_image = quantized_image / 255.0
    output_path = 'output.jpg'
    plt.imsave(output_path, quantized_image)
    output_file_size = os.path.getsize('output.jpg')

    # Display the original and quantized images side by side
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(image)
    axs[0].set_title(f'Original Image\n\nFile size: {input_file_size / 1024:.2f} KB')
    axs[0].axis('off')

    axs[1].imshow(quantized_image)
    axs[1].set_title(f'Quantized Image\n\nFile size: {output_file_size / 1024:.2f} KB')
    axs[1].axis('off')

    plt.show()

    k = input('value of k: (E for exit): ')
