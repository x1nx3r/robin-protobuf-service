import io
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import waste_prediction_pb2 as waste_prediction_pb2
import waste_prediction_pb2_grpc as waste_prediction_pb2_grpc
from config import Config

ORGANIK = "organik"
ANORGANIK = "anorganik"
B3 = "B3"

class_labels_with_types = {
    "buah_sayuran": ORGANIK,
    "daun": ORGANIK,
    "elektronik": B3,
    "kaca": ANORGANIK,
    "kertas": ANORGANIK,
    "logam": ANORGANIK,
    "makanan": ORGANIK,
    "medis": B3,
    "plastik": ANORGANIK,
    "tekstil": ANORGANIK,
}

class_labels = list(class_labels_with_types.keys())

model = None

def load_model_from_dir():
    global model
    model = load_model(Config.EXTRACTED_MODEL_DIR)

# Implement the gRPC service
class WastePredictionServicer(waste_prediction_pb2_grpc.WastePredictionServicer):
    def PredictImage(self, request, context):
        try:
            # Load image from binary data
            image = Image.open(io.BytesIO(request.image)).resize((224, 224))
            image_array = np.expand_dims(np.array(image) / 255.0, axis=0)  # Normalize

            # Run the prediction
            prediction = model.predict(image_array)
            predicted_index = np.argmax(prediction[0])
            predicted_class = class_labels[predicted_index]
            waste_type = class_labels_with_types[predicted_class]

            # Prepare the response
            response = waste_prediction_pb2.PredictResponse(
                predicted_class=predicted_class,
                waste_type=waste_type,
                probabilities={
                    class_labels[i]: float(prob) for i, prob in enumerate(prediction[0])
                }
            )
            return response
        except Exception as e:
            context.set_details(f"Error processing image: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return waste_prediction_pb2.PredictResponse()