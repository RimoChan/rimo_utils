from cv2 import *
import numpy as np


def show(img):
    if img.dtype == np.float:
        img = (img * 255).astype(np.uint8)
    cv2.imshow('show', img)
    cv2.waitKey()


def read(img_path):
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
    if img is None:
        raise Exception('読み込み失敗')
    return img


def write(img, img_path, param=None):
    with open(img_path, 'wb') as f:
        if img.dtype in (np.float64, np.float32, np.float):
            img = (img * 255).astype(np.uint8)
        if param:
            _, data = cv2.imencode(img_path, img, param)
        else:
            _, data = cv2.imencode(img_path, img)
        f.write(data)


def VideoCapGen(source, size: tuple = None):
    cap = cv2.VideoCapture(source)
    if size:
        x, y = size
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, x)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, y)
    while True:
        _, img = cap.read()
        if img is None:
            raise Exception('没图')
        yield img
