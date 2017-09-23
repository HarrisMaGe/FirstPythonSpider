# -*- coding: utf-8 -*-
class Html_Outputer(object):
    def __init__(self):
        self.dates = []
        self.itemdates=[]

    def collectdate(self, new_date):
        if new_date is None:
            return None

        self.dates.append(new_date)

    def collectItemDte(self,date):
        if date is None:
            return None
        self.itemdates.append(date)


    def output(self):
        fout = open('output.html', 'w')
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write("<title>")
        fout.write("<meta charset='utf-8'>")
        fout.write("</title>")
        fout.write("<body>")
        fout.write("<table>")

        for date in self.itemdates:
            try:
                fout.write("<tr style='text-align:center;border:3px solid black;'>")
                fout.write("<td style='text-align:center;border:1px solid black;'>%s</td>" % date['name'].encode('utf-8'))
                #fout.write(
                    #"<td style='text-align:center;border:1px solid black;'>%s</td>" % date['catalog'].encode('utf-8'))
                fout.write(
                    "<td style='text-align:center;border:1px solid black;'>%s</td>" % date['shop'].encode('utf-8'))
                fout.write(
                    "<td style='text-align:center;border:1px solid black;'>%s</td>" % date['url'].encode('utf-8'))
                fout.write("</tr>")

            except:
                continue
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def outputItems(self):
        fout = open('output.html', 'w')
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write("<title>")
        fout.write("<meta charset='utf-8'>")
        fout.write("</title>")
        fout.write("<body>")
        fout.write("<table>")

        for date in self.dates:
            try:
                fout.write("<tr style='text-align:center;border:2px solid black;'>")
                fout.write("<td style='text-align:center;border:2px solid black;'>%s</td>" % date['url'])
                fout.write(
                    "<td style='text-align:center;border:2px solid black;'>%s</td>" % date['title'].encode('utf-8'))
            except:
                continue
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()