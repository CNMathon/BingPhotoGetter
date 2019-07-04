# 模块引入
# 注意：请务必手动安装 request 和 BeautifulSoup 作为依赖，否则可能会报错
# pip install requests
# pip install bs4
import requests
from bs4 import BeautifulSoup
import os
import datetime

# 目标URL
url = 'https://www.bing.com'
# 图片保存路径（注意斜杠方向）
file_folder = 'C:/Users/Mathon/Pictures/BingWallpapar'

# 生成并打印 文件信息
nowYear = str(datetime.datetime.now().year)
nowMonth = str(datetime.datetime.now().month)
nowDay = str(datetime.datetime.now().day)
if (len(nowMonth) < 2):
    nowMonth = '0' + nowMonth
if (len(nowDay) < 2):
    nowDay = '0' + nowDay
file_name = nowYear + nowMonth + nowDay + '.jpg'
file_path = file_folder + '/' + file_name
print('[File_folder] ' + file_folder)
print('[File_name] ' + file_name)
print('[File_path] ' + file_path)

# 
app_path = os.getcwd().replace('\\', '/')
print('[App_path] ' + app_path)

# 对目标站点发起 GET 请求
req_web = requests.get(url)

# 将网站编码设置为 UTF-8 (保险操作，防止乱码)
req_web.encoding = 'utf-8'

# 打印状态信息
print('[URL] ' + url)
print('[Status_code] ' + str(req_web.status_code))

# 解析并打印 图片相对路径
soup = BeautifulSoup(req_web.text, 'html.parser')
imgPath_rel = soup.find('link', id='bgLink').attrs['href']
print('[ImgPath_rel] ' + imgPath_rel)

# 解析并打印 图片绝对路径
imgPath_abs = url + imgPath_rel
print('[ImgPath_abs] ' + imgPath_abs)

# 图片下载
req_img = requests.get(imgPath_abs)
print('[Download] The main program is preparing to download resources...')
with open(file_path, 'wb') as f:
    f.write(req_img.content)

# 下载完成提示
print('[Download] Download completed!')