import web
import json
import csv
import pymysql
        
urls = (
    '/index', 'index',
)
app = web.application(urls, globals())

class index:
    def GET(self):
        data = web.input()
        if data:
            db = pymysql.connect("localhost", "root", "", "test")
            cursor = db.cursor()
       
            sql = "INSERT INTO input_record(title, name, filename, json, assertion) \
                   VALUES ('%s', '%s',  '%s',  '%s',  '%s')" % \
                   (data.title, data.name, data.filename, json.dumps(data.content, ensure_ascii=False), data.assertion)

            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

            db.close()

            return open(r'test.html', 'r').read()
        else:
            return open(r'test.html', 'r').read()

if __name__ == "__main__":
    app.run()