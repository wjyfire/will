import web
import json
import csv
        
urls = (
    '/index', 'index',
)
app = web.application(urls, globals())

class index:
    def GET(self):
        data = web.input()
        if data:
            double_encode = json.dumps(data.content)

            rows = [
                [data.title, data.num],
                [data.name, double_encode,data.assertion],
                #['用例2 - iotId不存在', double_encode,'"data":true']
            ]

            with open(data.filename, 'w',newline='')as f:
                f_csv = csv.writer(f,delimiter='?',quotechar='|',quoting=csv.QUOTE_NONE)
                f_csv.writerows(rows)
            return open(r'test.html', 'r').read()
        else:
            return open(r'test.html', 'r').read()

if __name__ == "__main__":
    app.run()