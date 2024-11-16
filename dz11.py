import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.applications.MobileNetV2(weights='imagenet')
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (224, 224))
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(image_resized))
    return image, np.expand_dims(image_array, axis=0)

image_path = 'sea.jfif'
original_image, preprocessed_image = preprocess_image(image_path)

predictions = model.predict(preprocessed_image)
decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)

print("Результати класифікації:")
for _, name, score in decoded_predictions[0]:
    print(f"Object: {name}, Confidence: {score:.2f}")

pattern_coords = [(50, 50, 150, 150), (200, 50, 250, 100)]
mask_path = 'ship.png'
mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
height, width, _ = original_image.shape

for (x1, y1, x2, y2) in pattern_coords:
    if x1 < 0 or y1 < 0 or x2 > width or y2 > height:
        print(f"Coordinates {(x1, y1, x2, y2)} out of bounds for image size {(width, height)}")
        continue

    resized_mask = cv2.resize(mask, (x2 - x1, y2 - y1))

    if resized_mask.shape[-1] != 4:
        print("Mask is missing an alpha channel. Adding one.")
        alpha_channel = np.ones((resized_mask.shape[0], resized_mask.shape[1]), dtype=resized_mask.dtype) * 255
        resized_mask = np.dstack([resized_mask, alpha_channel])

    alpha_s = resized_mask[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(3):
        original_image[y1:y2, x1:x2, c] = (alpha_s * resized_mask[:, :, c] +
                                           alpha_l * original_image[y1:y2, x1:x2, c])

processed_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
plt.imshow(processed_image_rgb)
plt.axis('off')
plt.title("Sea")
plt.show()






