# 安装证书
在driver/dll下有不同的dll文件
HID:键鼠一体
General：通用,需要根据win7，win10系统选择 在管理员权限下运行setup.cmd
Simple:简单

# example
```
from utils_uiauto.driver import DD_Driver_Mouse_Keybord 

dd = DD_Driver_Mouse_Keybord()
dd.keybord_input_str("123456")

