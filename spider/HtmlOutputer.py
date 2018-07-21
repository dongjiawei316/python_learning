# 网页输出器
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 我们以html表格形式进行输出
    def output_html(self):
        fout = open("output.html", "w", encoding='utf-8')
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        # 以表格输出
        fout.write("<table>")
        for data in self.datas:
            # 一行
            fout.write("<tr>")
            # 每个单元行的内容
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"])
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        # 输出完毕后一定要关闭输出器
        fout.close()
