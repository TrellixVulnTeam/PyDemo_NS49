from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


##循环遍历枚举值
for name, member in Month.__members__.items():
    print(name, "==>", member, ',', member.value)