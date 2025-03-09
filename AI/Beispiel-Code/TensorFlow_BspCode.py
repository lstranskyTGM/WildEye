from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models, layers

train_dir = "./train"
test_dir = "./test"
train_datagen = ImageDataGenerator(rescale=1.0/255.0)
test_datagen = ImageDataGenerator(rescale=1.0/255.0)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(28, 28),
    color_mode="grayscale",
    batch_size=8,
    class_mode="binary"
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(28, 28),
    color_mode="grayscale",
    batch_size=8,
    class_mode="binary"
)

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

num_epochs = 10
model.fit(
    train_generator,
    epochs=num_epochs,
    validation_data=test_generator
)
loss, accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
