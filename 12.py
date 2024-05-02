class Score2:
    def __init__(self,name,math,english,japanese):
        self.name = name
        self.math = math
        self.english = english
        self.japanese = japanese

#def get_highscore_and_lecture(self):
#    scores=[('math',self.math),('japanese',self.japanese),('english',self.english)]
##    for lecture, score in scores:
   #     if score > max-score:
     #       max_score=score
   #         max_score_subject=lecture
    def get_highscore_and_lecture(self):
        max_score_lecture = ""
        max_score = 0

 
        if self.math > max_score:
            max_score_lecture = "math"
            max_score = self.math
        
        if self.japanese > max_score:
            max_score_lecture = "japanese"
            max_score = self.japanese

        if self.english > max_score:
           max_score_lecture = "english"
           max_score = self.english

        return max_score_lecture, max_score
 
    #'科目'とスコアの値をセットでリストにする