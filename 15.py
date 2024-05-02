class ClassE(list):
    def __init__(self,type):
        self.type = type
        super().__init__()     #親クラスから名前だけ持ってくる

    def appenf(self,newitem):
        super().append(newitem) 
        if type(newitem) != self.type:
           raise TypeError('type error')    
        #ほえ〜raise TypeErrorっていう関数があるんだね。
       