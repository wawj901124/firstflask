import time
from myfirstvideotest.base_camera import BaseCamera
import numpy as np
import cv2


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of"""

    @staticmethod
    def frames():
        # 在这里实现自己视频帧的获取和处理
        i = 0
        while True:
            time.sleep(0.5)
            img = np.ones((640, 1080, 3), np.uint8) * 188
            cv2.putText(img, str(i), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img_encode = cv2.imencode('.jpg', img)[1]
            img_byte = img_encode.tobytes()

            yield img_byte
            i = i + 1
            i = i % 1000