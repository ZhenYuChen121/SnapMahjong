from Class import Tile
import CloseWin_ALG_Tile_version as alg
from ultralytics import YOLO
import cv2 as cv

# My_tilegroup = TileGroup()
# My_tilegroup.display()

mm = {0: '1m', 1: '1p', 2: '1s', 3: '1z', 4: '2m', 5: '2p', 6: '2s', 7: '2z', 8: '3m', 9: '3p', 10: '3s', 11: '3z', 12: '4m', 13: '4p', 14: '4s', 15: '4z', 16: '5m', 17: '5p', 18: '5s', 19: '5z', 20: '6m', 21: '6p', 22: '6s', 23: '6z', 24: '7m', 25: '7p', 26: '7s', 27: '7z', 28: '8m', 29: '8p', 30: '8s', 31: '9m', 32: '9p', 33: '9s'}


model = YOLO("/root/Work/SideProject/Mahjong/model_m.pt")

image_path = "/root/Work/SideProject/Mahjong/Pattern/1.png"
image = cv.imread(image_path)

# results = model.predict(image, save= True)
results = model(image)[0]
print("--------------------------------------\n\n")



print(len(results.boxes.cls))
# for i in results.boxes.cls:
#     print(   mm[int(i.item())]   )


cls_list = [mm[int(i.item())] for i in results.boxes.cls]
# cls_list=[0]
if len(cls_list) == 16:
    # cls_list = ['1m','1m','1m','2m','3m', '4m', '5m', '7m', '6m', '8m', '9m', '9m', '9m',  '3z', '3z', '3z']
    print(cls_list)
    cls_list = sorted(cls_list, key=lambda x: (x[1], int(x[0])))
    





    print("----\n\n")
    #------------------------------------------------------- 
    result = alg.Detect_ReadyHand(cls_list, ["A","A","A","A","A", "B"])  # input => list of Tile class 

    result = list( set(alg.flatten(result)) )
    # if filter_re != {None}: 
    #     filter_re.remove(None) 

    print("聽: ", result)
else:
    print("predict error")
    print("len = ", len(cls_list))




















# print(model.names)

# print(len(results))
# # 繪製偵測框
# for result in results:
    
    # print(type(result.boxes.cls))
    
#     boxes = result.boxes.xyxy  # 取得所有預測框 (格式為 [x1, y1, x2, y2])
#     scores = result.boxes.conf  # 取得置信度
#     class_ids = result.boxes.cls  # 取得分類ID

#     for box, score, class_id in zip(boxes, scores, class_ids):
#         x1, y1, x2, y2 = map(int, box)  # 將座標轉為整數
#         label = f"{model.names[int(class_id)]}: {score:.2f}"  # 建立標籤文字

#         # 畫框與標籤
#         cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv.putText(image, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# # 保存結果圖片
# output_path = "/root/Work/SideProject/Mahjong/Pattern/output.png"
# cv.imwrite(output_path, image)

# print(f"結果已保存至 {output_path}")



