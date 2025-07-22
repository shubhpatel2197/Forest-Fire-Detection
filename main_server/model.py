from preprocess import pre
import pickle
import cv2

def predict(img):
    x = pre(img)
    with open('random.pkl', 'rb') as f:
        model = pickle.load(f)
    return(model.predict(x))

if __name__ == '__main__':
    original_image = cv2.imread('nofire_0097.jpg')
    print(predict(original_image))