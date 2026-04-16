class Solution:

    def encode(self, strs: List[str]) -> str:
        mainstr = ""
        for string in strs:
            strlength = str(len(string))
            # print(type(strlength))
            string = strlength + "#" + string
            mainstr = mainstr + string
        
        print(mainstr)
        return mainstr
    def decode(self, s: str) -> List[str]:
        my_string = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            print(j)
            length = int(s[i:j])
            print(length)
            my_string.append(s[j+1:j+1+length])
            i = j + 1 + length
        return my_string

                  

