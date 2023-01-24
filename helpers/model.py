import tensorflow_hub as hub 
import tensorflow_text as text
#import keras
from tensorflow import keras

new_model = keras.models.load_model(
       ('Citas_RN.h5'),
       custom_objects={'KerasLayer':hub.KerasLayer}
)

new_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])