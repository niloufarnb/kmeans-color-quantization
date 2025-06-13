def create_quantized_image(centroids, assignments, image_shape):
    quantized_pixels = centroids[assignments]
    quantized_image = quantized_pixels.reshape(image_shape)
    return quantized_image
