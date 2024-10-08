###
# Author : Emmanuel Essien
# Author Email : emmanuelessiens@outlook.com
# Maintainer By: Emmanuel Essien
# Maintainer Email: emmanuelessiens@outlook.com
# Created by Emmanuel Essien on 08/01/2020.
###
import re

class iteration:


    def __getattr__(self, item):

        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:

            if all(args) != False:
                self.iter = self.iteri(*args, **kwargs)
            else:
                self.iter = self.iteri(**kwargs)
        return None

    def __str__(self):
        return self.iter


    def iteri(self, dictionary=[], itr="pid") -> list:

        i = 0
        if len(dictionary) > 0:
            dist, apend = [], []
            for l in dictionary:
                i += 1
                listv = l
                dist = {itr: i}
                dist.update(listv)
                apend.append(dist)
            return apend
        else:
            return dictionary



    def keyword(self, keywords, limit = 0):

        if type(keywords) == str:
            pattern = re.compile("\s*,\s*|\s+$")
            tag = pattern.split()
            splittag = [x for x in tag if x]
        elif type(keywords) == list:
            tag = keywords
            joinl = [x for x in tag if x]
            stag = " ".join(joinl)
            splittag = stag.split(",")



        try:

            if int(limit) > 0:
                lk = []
                ct = 0
                for nsl in splittag:
                    ct +=1
                    if ct < limit+1:
                        lk.append(nsl)

                return lk
            else:
                return splittag

        except Exception as err:
            return  err

