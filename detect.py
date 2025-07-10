import queue
import time
import tensorflow as tf
import cv2
import numpy as np


class Detect:
    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path="./facemodel.tflite")
        self.interpreter.allocate_tensors()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        input_details = self.interpreter.get_input_details()
        self.input_index = input_details[0]["index"]
        self.input_dtype = input_details[0]["dtype"]
        _, self.height, self.width, _ = input_details[0]["shape"]
        self.floating_model = self.input_dtype == np.float32

        output_details = self.interpreter.get_output_details()
        self.output_index = output_details[0]["index"]
        self.output_quant = output_details[0].get("quantization", (1.0, 0.0))
        self.output_dtype = output_details[0]["dtype"]

        self.classname = ["authorized", "unauthorized"]
        self.detect_times = 5

    def detect_task(self, result_q: queue.Queue):
        ok_count = 0

        for i in range(self.detect_times):
            print(f"Detect: {i+1}/{self.detect_times}")

            ret, img = self.cap.read()
            if not ret:
                print("Error: Failed to capture image from camera.")
                continue

            # BGR -> RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Resize to model input size
            resized_img = cv2.resize(img_rgb, (self.width, self.height))

            input_data = np.expand_dims(resized_img, axis=0)
            if self.floating_model:
                input_data = (input_data.astype(np.float32) - 127.5) / 127.5
            else:
                input_data = input_data.astype(self.input_dtype)

            self.interpreter.set_tensor(self.input_index, input_data)
            self.interpreter.invoke()

            output_data = self.interpreter.get_tensor(self.output_index)
            predictions = np.squeeze(output_data)

            if self.output_dtype == np.uint8:
                scale, zero_point = self.output_quant
                predictions = scale * (predictions - zero_point)

            maxindex = int(np.argmax(predictions))
            prediction_label = self.classname[maxindex]
            print(f"Prediction: {prediction_label}")

            if prediction_label == "authorized":
                ok_count += 1

            time.sleep(0.2)  # 小休止（200ms）

        # 最終判定
        result = ok_count * 2 >= self.detect_times
        result_q.put(result)
