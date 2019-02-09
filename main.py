import bs4
import requests
import openpyxl
from selenium import webdriver

URL = 'https://sobooks.cc/xuexijiaoyu/page/3'

# TODO: 创建并打开电子表格
excel = openpyxl.Workbook()
sheet = excel.get_sheet_by_name('Sheet')
sheet['A1'] = '书名'
sheet['B1'] = '作者'
sheet['C1'] = '百度网盘'
sheet['D1'] = '提取码'

# TODO: 获取主页
resp = requests.get(URL)
respBSoup = bs4.BeautifulSoup(resp.text)

# TODO: 获取所有书的集合
bookNameList = respBSoup.select('.card-item h3 a')
bookAuthorList = respBSoup.select('.card-item p a')


nextPage = True
# TODO: 判断是否有下一页
while nextPage:
    # TODO: 获取每本书的名称 作者 链接
    for i in range(len(bookNameList)):
        bookName = bookNameList[i].text
        bookAuthor = bookAuthorList[i].text
        bookUrl = bookNameList[i].get('href')

        # TODO: 打开每本书的链接
        browser = webdriver.Chrome()
        browser.get(bookUrl)

        # TODO: 模拟输入密码 2018919
        passwordInput = browser.find_element_by_name('e_secret_key')
        passwordInput.send_keys('2018919')
        passwordInput.submit()

        # TODO: 获取提取码
        extractPassword = browser.find_elements_by_tag_name('strong')
        extractPassword = extractPassword[len(extractPassword)-1].text[-4:]
        # print(len(extractPassword))
        # print(extractPassword)

        # TODO: 获取百度网盘链接
        netdiskLink = browser.find_element_by_link_text('百度网盘').get_attribute('href')
        netdiskLink = netdiskLink[31:]
        print(bookName, bookAuthor, netdiskLink)
        print(extractPassword)

        # TODO: 输出到excel文件中
        sheet['A' + str(i+2)] = bookName
        sheet['B' + str(i + 2)] = bookAuthor
        sheet['C' + str(i + 2)] = netdiskLink
        sheet['D' + str(i + 2)] = extractPassword
        browser.close()
    nextPage = browser.find_element_by_link_text('下一页')

excel.save('book.xlsx')


