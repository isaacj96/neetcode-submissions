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
        my_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            my_list.append(s[j+1: j + length + 1])
            i = j + 1 + length
        return(my_list)
                  

