import pymysql
import time

while True:
    try:
        conn = pymysql.connect(host="10.25.197.201", user="housys", password="housys", database="housys")
        x = conn.cursor()
        break
    except Exception as e:
        print("Not able to connect to database")
        time.sleep(10)


def poll_file(file_path):
    while True:
        try:
            file = open(file_path, 'r')
            data = file.read()
            if data:
                sql = """UPDATE vacancy_status SET vacancy = '%s'
                WHERE system_id='%s'""" % (data.split(',')[1], "10")
                x.execute(sql)
                conn.commit()
                print("Data updated in DB")
            file.close()
            time.sleep(28)
        except Exception as e:
            file.close()
            print("Not able to update values in database due to the error %s", str(e))
            try:
                conn = pymysql.connect(host="10.25.197.201", user="housys", password="housys", database="housys")
                x = conn.cursor()
            except Exception as e:
                pass
            time.sleep(10)

if __name__ == '__main__':
    file_path = 'C:\ParkManage\ParkManage.txt'
    #file_path = 'ParkManage.txt'
    poll_file(file_path)
