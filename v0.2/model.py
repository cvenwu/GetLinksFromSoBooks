
class Book():

    def __init__(self, name, info_url, author, baidu_url, baidu_password):
        self.name = name
        self.author = author
        self.info_url = info_url
        self.baidu_url = baidu_url
        self.baidu_password = baidu_password

    def __repr__(self):
        return "<Book %r>" % self.name


class Category():

    def __init__(self, name):
        self.name = name
