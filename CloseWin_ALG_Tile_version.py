# for dataset link: https://universe.roboflow.com/project-xv49e/mahjong-x5dzz/dataset/2
# 1萬-9萬: 1m-9m
# 1筒-9筒: 1p-9p
# 1條-9條: 1s-9s
# 東南西北白發中: 1z-7z


# 判斷是否為一搭
def check_3(s):
    # print("\n\n in check3")
    # print(s, "\n\n")
    if s[0][1]==s[1][1]==s[2][1]:
        if s[0][1]==s[1][1]==s[2][1]=="z": #都是大字 要成搭只能三個一樣
            return s[0][0]==s[1][0]==s[2][0]
        return s[0][0]==s[1][0]==s[2][0] or int(s[0][0])==int(s[1][0])-1==int(s[2][0])-2
    return False

# 判斷是否為眼睛
def check_2(s):
    return s[0][1] == s[1][1] and s[0][0]==s[1][0]

# s is sub string on l, return l without s
def get_remain_string(l, s):
    # l = list(l)
    # s = list(s)

    for ss in s:
        l.remove (ss)

    # return ''.join(l)
    return l


# 依據輸入牌型 和 需要形成的牌型 回傳聽甚麼牌 ex. input=(23,搭) output=14, input=(9,眼) output=9, 若沒有聽則回傳None
def get_closewin_tile(s, style):
    closewintile = []

    if style == "B":
        closewintile.append(s[0])
        return closewintile
    
    elif s[0][1] != s[1][1]:
        return None

    # elif int(s[0][0]) == int(s[1][0])-1 or int(s[0][0])-1 == int(s[1][0]): # 聽雙頭
    # print(s)
    maxx = max(int(s[0][0]),int(s[1][0]))
    minn = min(int(s[0][0]),int(s[1][0]))

    if maxx-1 == minn and s[0][1] != "z": # 聽雙頭
        if minn != 1: # not 12
            closewintile.append (str(minn-1) + s[0][1])
        if maxx != 9: # not 89
            closewintile.append (str(maxx+1) + s[1][1])

    elif maxx-2 == minn and s[0][1] != "z": # 聽中洞
        closewintile.append(str(minn+1) + s[0][1])

    elif maxx == minn: # 聽刻子
        closewintile. append(s[0])
    
    else:
        return None
    
    return closewintile

# multi-dimension list => 1-dimension list
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


# key function
def Detect_ReadyHand(s, ans): 
    # print(s)
    # print(ans)
    if len(ans)==1: 
        # print("here")
        return get_closewin_tile(s, ans[0]) 
    else: 
        close = []
        
        # check 3 
        if "A" in ans: 
            for i in range(len(s)-3+1): # for 012, 123, 234 ...(n-2)(n-1)n
                # print ("s- ", s) 
                # print("3ans= ?,ans) 
                # print(s)
                # print(ans)
                subs = s.copy()
                sub_ans = ans.copy() 
                
                if check_3(subs[i:i+3]): # 012, 123, 234 ...(n-2)(n-1)n
                    sub_ans.remove("A") 
                    # print("ans- ", ans) 
                    close.append( Detect_ReadyHand( get_remain_string(subs, subs[i:i+3]), sub_ans) ) 
        
        # check 2 
        if "B" in ans: 
            for i in range(len(s)-2+1): # remain
                # print ("s- ", s) 
                # print("3ans= ?,ans) 
                subs = s.copy()
                sub_ans = ans.copy() 
                if check_2(subs [i:i+2]): 
                    sub_ans.remove("B") 
                    # print("ans- ", ans) 
                    close.append( Detect_ReadyHand( get_remain_string(subs, subs[i:i+2]), sub_ans) ) 
        
        return close






if __name__ == "__main__":
    #                         ['7p', '7s', '3z', '3m', '3s', '3z', '9s', '8m', '7m', '2s', '4s', '8s', '4m', '6p', '8p', '5m']
    result = Detect_ReadyHand(['7s', '8s', '9s', '4s', '3s', '2s', '6p', '8p', '7p','3m', '4m', '5m', '3z', '3z', '8m', '7m'], ["A", "A", "A", "A", "A", "B"])  # input => list of Tile class 
    # result = Detect_ReadyHand(["6m", "7m"], ["A"])  # input => list of Tile class 

    result = list( set(flatten(result)) )
    # if filter_re != {None}: 
    #     filter_re.remove(None) 

    print("聽: ", result)
    # print(type(result))

    # k = ["1", "2", "3", "4"]
    # kk = ["2"]

    # print(get_remain_string(k,kk)) 22