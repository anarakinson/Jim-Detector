import pickle
import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.preprocessing import Normalizer

def get_encode(face_encoder, face, size):
    '''
    Функция получает вырезанное с фото лицо
    и возвращает полученные по нему набор фичей 
    '''
    face = normalize(face)
    face = cv2.resize(face, size)
    encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
    return encode


def get_face(img, box):
    '''
    Функция получает изображение, ищет на нем лицо,
    и, если находит, возвращает 
    лицо отдельным изображением и его координаты на фото
    '''
    x1, y1, width, height = box
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = img[y1:y2, x1:x2]
    return face, (x1, y1), (x2, y2)


l2_normalizer = Normalizer('l2')


def normalize(img):
    '''
    Функция нормализации изображения
    '''
    mean, std = img.mean(), img.std()
    return (img - mean) / std


def plt_show(cv_img):
    img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


def load_pickle(path):
    with open(path, 'rb') as f:
        encoding_dict = pickle.load(f)
    return encoding_dict


def save_pickle(path, obj):
    with open(path, 'wb') as file:
        pickle.dump(obj, file)


def load_pickle(path):
    with open(path, 'rb') as file:
        return pickle.load(file)
