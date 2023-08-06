import win32com.client
import time
import uiautomation as auto


def ie_execute_js(js_code: str, url: str):
    """ie执行js

    Args:
        js_code (str): js代码
        url (str): 具体执行js的网站

    Returns:
        执行返回js的结果
    """
    # 获取IE浏览器窗口句柄
    shell = win32com.client.Dispatch("Shell.Application")
    windows = shell.Windows()
    for window in windows:
        # print(dir(window))
        if "IE" in window.FullName:
            ie = window
            # print(ie.LocationURL)
            if url == ie.LocationURL:
                # 在当前窗口执行JS
                document = ie.Document
                
                print(dir(document.parentWindow))
                result = document.parentWindow.execScript(js_code)
                
                
               


def open_ie(url):
    """打开ie,访问网站,激活,最大化

    Args:
        url (_type_): 具体的url地址
    """
    # 根据不同的浏览器名称创建不同的com对象

    browser = win32com.client.Dispatch("InternetExplorer.Application")
    class_name = "IEFrame"

    # 打开浏览器并导航到指定的URL
    browser.Visible = True
    browser.Navigate(url)

    # 等待浏览器加载页面完成
    while browser.ReadyState != 4 or browser.Busy:
        time.sleep(1)

    # 激活浏览器窗口并最大化
    title = browser.Document.Title
    # print(title)
    # print(browser_name.capitalize())
    browser_window = auto.WindowControl(
        searchDepth=1, ClassName=class_name, SubName=title
    )
    browser_window.SetActive()
    browser_window.Maximize()


