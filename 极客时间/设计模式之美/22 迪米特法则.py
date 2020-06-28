class HtmlRequest:
    def __init__(self, url):
        pass

    def getAddress(self):
        pass

    def getContent(self):
        pass


class Html():
    pass


class NetworkTransporter():

    def send(self, address, data):
        pass


class HtmlDownloader():

    def __init__(self):
        self.transporter = NetworkTransporter()

    def downloadHtml(self, url):
        htmlRequest = HtmlRequest(url)
        rawHtml = self.transporter.send(htmlRequest.getAddress(), htmlRequest.getContent().getBytes())
        return Html(rawHtml)


class Document():
    def __init__(self, url, html):
        self.html = html
        self.url = url


class DocumentFactory():

    def DocumentFactory(self, downloader):
        self.downloader = downloader

    def createDocument(self, url):
        html = self.downloader.downloadHtml(url)
        return Document(url, html)
