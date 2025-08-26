
import random
import cv2
import numpy as np

# Tile = 牌
# style = 筒CI、條BA、萬CH、字HO、花FL
# number = 1-9、東1南2西3北4中5發6白7、春1夏2秋3冬4梅5蘭6竹7菊8

############################################################## class


# En2Chi = {("1","HO"):"東風", ("2","HO"):"南風", ("3","HO"):"西風", ("4","HO"):"北風", ("5","HO"):"紅中", ("6","HO"):"青發", ("7","HO"):"白皮", 
#           ("1","FL"):"春1花",("2","FL"):"夏2花",("3","FL"):"秋3花",("4","FL"):"冬4花",
#           ("5","FL"):"梅1花",("6","FL"):"蘭2花",("7","FL"):"竹3花",("8","FL"):"菊4花",
#            "CH":"萬", "BA":"條", "CI":"筒"}

# class Tile:
#     def __init__(self, number, style):
#         self.style = style
#         self.number = number
    
    
#     def display(self):
#         if self.style == "CH" or self.style == "BA" or self.style == "CI":
#             print("this tile is ", self.number, En2Chi[self.style])
#         else:
#             print("this tile is ", En2Chi[str(self.number), self.style])
#         print("")


# for dataset link: https://universe.roboflow.com/project-xv49e/mahjong-x5dzz/dataset/2
# 1萬-9萬: 1m-9m
# 1筒-9筒: 1p-9p
# 1條-9條: 1s-9s
# 東南西北白發中: 1z-7z

En2Chi = {"1":"一","2":"二","3":"三","4":"四","5":"五","6":"六","7":"七","8":"八","9":"九",
          "m":"萬","p":"筒","s":"條",
          "1z":"東風","2z":"南風","3z":"西風","4z":"北風","5z":"白皮","6z":"發財","7z":"紅中",}

class Tile:
    def __init__(self, name):
        self.name = name
    
    
    def print_that_shit(self):
        if self.name[1] == "z" :
            print("this tile is ", En2Chi[self.name])
        else:
            print("this tile is "+ En2Chi[self.name[0]] + En2Chi[self.name[1]])
        print("")


class TileGroup:
    def __init__(self):
        self.alltile_set()
        self.tilegroup = random.sample(self.Characters+self.Bamboos+self.Circles+self.Honors, 16)  # 先排除花牌
        self.sort()

    def alltile_set(self):
        self.Characters = [] # 萬
        self.Bamboos = [] # 條
        self.Circles = [] # 筒
        self.Honors = [] # 字
        self.Flowers = [] # 花

        for i in range(1,10):
            for _ in range(4): self.Characters.append(Tile(i, "CH"))
            for _ in range(4): self.Bamboos.append(Tile(i, "BA"))
            for _ in range(4): self.Circles.append(Tile(i, "CI"))

        for i in range(1,8):
            for _ in range(4): self.Honors.append(Tile(i, "HO"))

        for i in range(1,9):
            self.Flowers.append(Tile(i, "FL"))
    
    def sort(self):
        CH_list = []
        BA_list = []
        CI_list = []
        HO_list = []

        # classfier
        for tile in self.tilegroup:
            if tile.style == "CH":
                CH_list.append(tile)
            elif tile.style == "BA":
                BA_list.append(tile)
            elif tile.style == "CI":
                CI_list.append(tile)
            else:
                HO_list.append(tile)

        # sort base on each tile's number
        CH_list = sorted(CH_list, key=lambda x: x.number)
        BA_list = sorted(BA_list, key=lambda x: x.number)
        CI_list = sorted(CI_list, key=lambda x: x.number)
        HO_list = sorted(HO_list, key=lambda x: x.number)

        # concatenation
        self.tilegroup = CH_list + BA_list + CI_list + HO_list


    def display(self):
        
        # get each tile pattern
        image = []
        for tile in self.tilegroup:
            tile.display()
            path = "Pattern\\Tiles\\" + str(tile.number) + "_" + str(tile.style)  +   ".png"
            image.append(path)

           
        # create window
        window = np.ones((700, 1350, 3), dtype=np.uint8) * 255  #white background

        # resize to 90*64
        image = [cv2.resize(cv2.imread(png_file), (64, 90), interpolation=cv2.INTER_LINEAR) for png_file in image if cv2.imread(png_file) is not None]

        # default value xy = first tile left-top position
        h, w = 90, 64
        x, y = 40, 550
            
        # check image read successfully
        if image is not None:
            for i in range(len(image)):
                window[y:y+h, x+(w*i)+5*i:x+(w*(i+1)+5*i)] = image[i]

            # show
            cv2.imshow('Mahjong', window)

            # wait user press any key
            cv2.waitKey(0)

            # close window
            cv2.destroyAllWindows()
        else:
            print('無法讀取圖片')









# # check tile png work 
# # 創建一個白色背景的視窗
# window = np.ones((700, 1200, 3), dtype=np.uint8) * 255  # 白色背景

# # 讀取圖片
# image = [r'Pattern\Tiles\1_BA.png', r'Pattern\Tiles\2_BA.png' ]
# #image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
# image = [cv2.resize(cv2.imread(png_file), (64, 90), interpolation=cv2.INTER_LINEAR) for png_file in image if cv2.imread(png_file) is not None]

# h, w = image[0].shape[:2]

# # 檢查圖片是否成功讀取
# if image is not None:
#     # 將圖片放入視窗中央
    
#     print("h=", h)
#     print("w=", w)
#     y = 500
#     x = 100
#     for i in range(len(image)):
#         window[y:y+h, x+(w*i)+5*i:x+(w*(i+1)+5*i)] = image[i]

#     # 顯示視窗
#     cv2.imshow('Window with Image', window)
#     # 等待用戶按下任意鍵關閉視窗
#     cv2.waitKey(0)
#     # 關閉視窗
#     cv2.destroyAllWindows()
# else:
#     print('無法讀取圖片')












        
        




