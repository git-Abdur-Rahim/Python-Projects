import re

def replaced_String(res4,String):

    if res4 != "":
        # print("< Empty String > ", res4("<EmptyString>"))
        #    res4 = re.sub("[^0-9]","",String)

        print("The resultant string : ", (re.sub("[0-9]", "#", res4)))
        # print(re.sub("[^0-9]", "", res4))

    else:

        print("The resultant string : < Empty String > ")

def replace_digits():
    String = str(input())
   # m = re.sub("\d", "#", String)  # https://stackoverflow.com/questions/57007469/is-there-a-regex-to-replace-the-digits-in-the-string-with-and-remove-all-the
    print("The original string is : " + str(String))
                  # /D  = /d = [0-9]
    res4 = re.sub("[^0-9]","", String)  #  https://www.kite.com/python/answers/how-to-remove-all-non-numeric-characters-from-a-string-in-python
   # print("The resultant string : ",(re.sub("[0-9]","#",res4)))

    replaced_String(res4,String)
   # return() # modified string which is after replacing the # with digits

replace_digits()
