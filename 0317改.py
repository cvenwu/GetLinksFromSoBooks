import bs4
import requests
import openpyxl
from selenium import webdriver

url = 'https://sobooks.cc/xuexijiaoyu/'

# TODO: 创建并打开电子表格
excel = openpyxl.Workbook()
sheet = excel.get_sheet_by_name('Sheet')
sheet['A1'] = '书名'
sheet['B1'] = '作者'
sheet['C1'] = '百度网盘'
sheet['D1'] = '提取码'

# TODO: 获取"下一页"的链接
nextPage = True
while nextPage:
    # 检测是否有下一页
    resp = requests.get(url)
    respBSoup = bs4.BeautifulSoup(resp.text, "html.parser")

    bookNameList = respBSoup.select('.card-item h3 a')
    bookAuthorList = respBSoup.select('.card-item p a')

    # 遍历列表获得书的信息
    for i in range(len(bookNameList)):
        bookName = bookNameList[i].text
        bookAuthor = bookAuthorList[i].text
        bookUrl = bookNameList[i].get('href')

        # TODO: 打开每本书的链接
        browser = webdriver.Chrome()
        browser.get(bookUrl)
        print("Download the info of {0}".format(bookName))

        # TODO: 模拟输入密码 201929
        passwordInput = browser.find_element_by_name('e_secret_key')
        passwordInput.send_keys('201929')
        passwordInput.submit()

        # TODO: 获取提取码
        extractPassword = browser.find_elements_by_tag_name('strong')
        extractPassword = extractPassword[len(extractPassword) - 1].text[-4:]
        # print(len(extractPassword))
        # print(extractPassword)

        # TODO: 获取百度网盘链接
        # 每次爬取到 用Python写网络爬虫 就报错
        netdiskLink = respBSoup.select('^="https://sobooks.cc/');
        print(type(netdiskLink))
        print(netdiskLink)
        # netdiskLink = browser.find_element_by_link_text('百度网盘').get_attribute('href')
        netdiskLink = netdiskLink[31:]
        print("Download the info of {0} Successfully!!!".format(bookName))

        # TODO: 输出到excel文件中
        sheet['A' + str(i + 2)] = bookName
        sheet['B' + str(i + 2)] = bookAuthor
        sheet['C' + str(i + 2)] = netdiskLink
        sheet['D' + str(i + 2)] = extractPassword
        browser.close()

    # 判断下一页是否存在
    nextPageLink = respBSoup.find("a", text='下一页')
    if nextPageLink is None:
        nextPage = False
        break
    url = nextPageLink["href"]

    excel.save('book.xlsx')

