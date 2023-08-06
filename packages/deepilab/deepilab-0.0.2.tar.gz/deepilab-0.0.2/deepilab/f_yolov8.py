from ultralytics.yolo.utils.plotting import Annotator, colors
from ultralytics.yolo.data.augment import LetterBox
import copy
import cv2
from PIL import Image, ImageDraw
import numpy as np
import torch

def test():
	print('test success')

def imshow(img):
    cv2.imshow('image', img)
    cv2.waitKey() 
    cv2.destroyAllWindows()


def macshow(img):
    _img = copy.deepcopy(img)
    p_img = Image.fromarray(_img)
    p_img.show()


def imgload(Imgpath):
    img = cv2.imread(Imgpath)
    if img is None:
        img = Image.open(Imgpath)
        img = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB)
    return img


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def v8_processing(Result, conf = True, labels = True):
    annotator = Annotator(copy.deepcopy(Result.orig_img))
    pred_boxes = Result.boxes
    
    if len(Result.keys) == 1 and 'boxes' in Result.keys:
        
        names = Result.names
        
        for d in reversed(pred_boxes):
            c, conf, id = int(d.cls), float(d.conf) if conf else None, None if d.id is None else int(d.id.item())
            name = ('' if id is None else f'id:{id} ') + names[c]
            label = (f'{name} {conf:.2f}' if conf else name) if labels else None
            annotator.box_label(d.xyxy.squeeze(), label, color=colors(c, True))
        
        det = Result.boxes.data
        det = det.to(torch.device('cpu')).numpy()
        
    elif len(Result.keys) == 2 and 'masks' in Result.keys:
        pred_masks = Result.masks
        if 'cuda' in Result.boxes.xywh.device.type:
            img = LetterBox(pred_masks.shape[1:])(image=annotator.result())
            img_gpu = torch.as_tensor(img, dtype=torch.float16, device=pred_masks.masks.device).permute(
                2, 0, 1).flip(0).contiguous() / 255
        annotator.masks(pred_masks.data, colors=[colors(x, True) for x in pred_boxes.cls], im_gpu=img_gpu)
        
        det = Result.masks.xy
    
    d_img = annotator.result()
    
    return det, d_img