praceticStr = "wqxzxx3,223redv,fgh"

# 检测字符串是否只由字母组成
print(praceticStr.isalpha())

# 检测字符串是否由字母和数字组成
print(praceticStr.isalnum())

# 检测字符串是否只由数字组成
print(praceticStr.isdigit())

# 检测字符串是否只由数字组成。这种方法是只针对unicode对象。
# 注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，
print(praceticStr.isnumeric())

# 检测字符串是否只由空格组成
print(praceticStr.isspace())

#  检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print(praceticStr.istitle())

# 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print(praceticStr.title())

# 检测字符串是否由小写字母组成
print(praceticStr.islower())

# 检测字符串中所有的字母是否都为大写
print(praceticStr.isupper())

# 转换字符串中所有大写字符为小写.
print(praceticStr.lower())

# 转换字符串中的小写字母为大写
print(praceticStr.upper())

# 翻转 string 中的大小写
print(praceticStr.swapcase())

# 将序列中的元素以指定的字符连接生成一个新的字符串
print("-".join(["a", "b", "c"]))

# 返回对象（字符、列表、元组等）长度或项目个数
print(len(praceticStr))

# 字符串的第一个字符大写
print(praceticStr.capitalize())

# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
print(praceticStr.center(30, "="))

# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格
print(praceticStr.ljust(30, "="))

# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
print(praceticStr.rjust(30, "="))

# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
print(praceticStr.zfill(26))

# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(praceticStr.count("x"))

# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
print(praceticStr.encode(encoding="utf-8", errors="ignore"))

# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回
print(praceticStr.encode(encoding="utf-8").decode(encoding="utf-8"))

# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查
print(praceticStr.startswith("xx"))

# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束
print(praceticStr.endswith("xx"))

# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
print(praceticStr.expandtabs(tabsize=8))

# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
print(praceticStr.find("x"))

# 类似于 find()函数，不过是从右边开始查找.
print(praceticStr.rfind("x"))

# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
print(praceticStr.index("x"))

# 类似于 index()，不过是从右边开始.
print(praceticStr.rindex("x"))

# 截掉字符串左边的空格或指定字符。
print(praceticStr.lstrip("x"))

# 截掉字符串末尾的空格或指定字符。
print(praceticStr.rstrip("x"))

# 在字符串上执行 lstrip()和 rstrip()
print(praceticStr.strip())

# 用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
# 两个字符串的长度必须相同，为一一对应的关系。 内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# replace字符串长度可以不一致
t = str.maketrans("x", "t")
print(praceticStr.translate(t))

# 格式化字符串
print(praceticStr.format())

# 返回字符串 str 中最大的字母
print(max(praceticStr))

# 返回字符串 str 中最小的字母
print(min(praceticStr))

# 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),
# 如果 string 中不包含str 则 string_pre_str == string
print(praceticStr.partition("x"))

# 类似于 partition()函数,不过是从右边开始查找.
print(praceticStr.rpartition("x"))

# 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次
print(praceticStr.replace("x", "t", 2))

# 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
print(praceticStr.split(",", 3))

# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符
print(praceticStr.splitlines(True))
