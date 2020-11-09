url = input("페이지 주소 : ")
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")]
my_str = my_str[0:3]
passwd = my_str + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 passwd는 {1}입니다.".format (str(url),passwd) )