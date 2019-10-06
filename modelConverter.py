from tensorflow.contrib import lite
converter = lite.TFLiteConverter.from_keras_model_file('food.h5')
tfmodel = converter.convert()
open("model.tflite","wb").write(tfmodel)