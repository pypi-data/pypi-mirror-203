from ctypes import *
from retrying import retry
import time
from utils_uiauto.driver import VK
# from dd_code import VK
# 加载动态链接库（加载之前需要激活证书）
from pathlib import Path
pwd = Path(__file__).parent.joinpath("dll","2.General","DD64.dll").as_posix()
dd_dll = windll.LoadLibrary(pwd)





class DD_Driver_Mouse_Keybord:
    def __init__(self) -> None:
       self._initialize_dd()
            
    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def _initialize_dd(self):
        st = dd_dll.DD_btn(0)  # DD Initialize
        if st == 1:
            print("OK")
        else:
            print("Error Initialize defeat")
            raise Exception("DD Initialize failed")

    def mouse_click(self, btn: int, mode: int = 0):
        """鼠标点击

        Args:
            btn (int):
                1 =左键按下 ,2 =左键放开
                4 =右键按下 ,8 =右键放开
                16 =中键按下 ,32 =中键放开
                64 =4键按下 ,128 =4键放开
                256 =5键按下 ,512 =5键放开
            mode (int):
                mode = 0 -> 直接点击并释放
                仅仅针对左右键
                

            example:
                模拟鼠标右键 只需要连写(中间可添加延迟)
                dd_btn(4); dd_btn(8);

        """
        if mode == 0:
            if btn == 1 :
                dd_dll.DD_btn(1)
                dd_dll.DD_btn(2)
            elif btn == 4:
                dd_dll.DD_btn(4)
                dd_dll.DD_btn(8)
                
        else:  

            
            dd_dll.DD_btn(btn)

    def mouse_mov_absolute(self,x: int, y: int):
        """鼠标绝对移动

        Args:
            x (int): 默认0
            y (int): 默认0
            屏幕左上角为原点
        """
        dd_dll.DD_mov(x, y)

    def mouse_mov_Relative(self,dx: int, dy: int):
        """鼠标相对移动

        Args:
            x (int): 默认0
            y (int): 默认0
            屏幕左上角为原点
        example:
            把鼠标向左移动10像素
            DD_movR(-10,0) ;
        """
        dd_dll.DD_movR(dx, dy)

    def mouse_whl(self,whl: int):
        
        
        """模拟鼠标滚动

        Args:
            whl (int):
                1 = 前
                2 = 后
        example:
            向前滚一格,
            DD_whl(1)
        """
        dd_dll.DD_whl(whl)
    
    def keybord_press_input(self,*args:VK,duration: float = 0.15):
        """使用按键的方法输入

        Args:
            duration (float, optional): _description_. Defaults to 0.15.
        """
        for arg in args:
            #按下并松开
            dd_dll.DD_key(arg, 1)
            dd_dll.DD_key(arg, 2)
            time.sleep(duration)

            
        
    def keybord_combination(self,*args: VK, press_duration: float = 0.15):
        """组合键
        """
        #按下
        for arg in args:
            dd_dll.DD_key(arg, 1)
            time.sleep(press_duration)
        #松开
        for arg in args:
              dd_dll.DD_key(arg, 2)
            

            
    def keybord(self,ddcode: VK, flag: int):
        """键盘按键

        Args:
            ddcode (int): 参考DD虚拟键盘码
            flag (int): 1 = 按下,2= 松开

        example:
            单键WIN,
            DD_key(601, 1);
            DD_key(601, 2);
            组合键:ctrl+alt+del
            DD_key(600,1);
            DD_key(602,1);
            DD_key(706,1);
            DD_key(706,2);
            DD_key(602,2);
            DD_key(600,2);
        """
        dd_dll.DD_key(ddcode, flag)

    def keybord_input_str(self,input_string: str, duration: float=0.25):
        """直接输入键盘上可见的字符和空格

        Args:
            string (str): 字符串
            dutation (int): 输入一个字符的间隔时间
        """
        for char in input_string:
            # 但是char为单字节字符串
            time.sleep(duration)
            dd_dll.DD_str(char)
            

