from preprocess import pre
import pickle
import cv2

MODEL_PATH = 'random.pkl'

class ff():
    def __init__(self):
        with open(MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)
    
    def predict(self, img):
        x = pre(img)
        array = self.model.predict(x)
        return self.tostr(array)
    
    def tostr(self, array):
        cl = array[0]
        if cl==0:
            return 'fire'
        return 'nofire'
    
if __name__ == '__main__':
    ff = ff()
    img = cv2.imread('fire_0003.jpg')
    print(ff.predict(img))