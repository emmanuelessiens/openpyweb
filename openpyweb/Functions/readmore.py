###
# Author : Emmanuel Essien
# Author Email : emmanuelessiens@outlook.com
# Maintainer By: Emmanuel Essien
# Maintainer Email: emmanuelessiens@outlook.com
# Created by Emmanuel Essien on 07/01/2020.
###
from openpyweb.Functions.validation import validation

class readmore(validation):


    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args,  **kwargs):

        if len(args) > 0 or len(kwargs) > 0:
            if all(args) is not False:
                self.strt = self.lstring(*args, **kwargs)
            else:
                self.strt = self.lstring(**kwargs)

        return None

    def __str__(self):

        return self.strt


    def lstring(self, text="", trim = 'False', length = '10000000000000', link="", label="Read more",  css="readmore"):

        if bool(trim) is True:
            new_text = self.trim(text)

        else:
            new_text = text
        readlable  = " <a class='{css}' href='{link}'> {label} </a>".format(css=css, link=link, label=label)
        data = self.limit(text=new_text, trim = trim, length = length, label=readlable)

        return data

    def limit(self, text="", trim = 'False', length = '10000000000000', label=""):

        if bool(trim) is True:
            new_text = self.trim(text)

        else:
            new_text = text

        data = (new_text[:int(length)] + str(label)) if len(new_text) > int(length) else new_text

        return data