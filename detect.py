import queue
import tensorflow as tf
import cv2
import numpy as np


class Detect:
    def __main__(self):
        self.interpreter = tf.lite.Interpreter("./facemodel.tflite")
        self.interpreter.allocate_tensors()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        details = self.interpreter.get_input_details()
        _, self.height, self.width, _ = details[0]["shape"]

        self.classname = ["authorized", "unauthorized"]

        self.detect_times = 5

    def detect_task(self, result_q: queue.Queue[bool]):
        ok_count = 0
        for i in range(self.detect_times):
            _, img = self.cap.read()

            input_details = self.interpreter.get_input_details()
            floating_model = input_details[0]["dtype"] == np.float32
            input_data = np.expand_dims(img, axis=0)
            if floating_model:
                input_data = (np.float32(input_data) - 127.5) / 127.5

            tensor_index = self.interpreter.get_input_details()[0]["index"]
            input_tensor = self.interpreter.tensor(tensor_index)()[0]
            input_tensor[:, :] = img
            self.interpreter.invoke()
            output_details = self.interpreter.get_output_details()[0]
            predictions = np.squeeze(
                self.interpreter.get_tensor(output_details["index"])
            )
            if output_details["dtype"] == np.uint8:
                scale, zero_point = output_details["quantization"]
                predictions = scale * (predictions - zero_point)

            maxindex = np.argmax(predictions)
            if self.classname[maxindex] == "authorized":
                ok_count += 1

        if (ok_count * 2) >= self.detect_times:
            result_q.put(True)
        else:
            result_q.put(False)
