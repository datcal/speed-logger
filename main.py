import speedtest
import sqlite3
import datetime


def speed_test():
    print("Starting")
    servers = []
    # If you want to test against a specific server
    # servers = [1234]
    threads = None
    # If you want to use a single threaded test
    # threads = 1
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()
    results_dict = s.results.dict()
    download = round((results_dict['download'] / 1000000), 2)
    upload = round((results_dict['upload'] / 1000000), 2)
    insert(download, upload)
    print("Finished")


def insert(download, upload):
    x = datetime.datetime.now()
    con = sqlite3.connect('speed.db')
    cur = con.cursor()
    cur.execute("insert into speeds(download,upload,ts) values (?, ?, ?)", (download, upload, x.strftime("%Y-%m-%d %H-%M-%S")))
    con.commit()
    con.close()


if __name__ == '__main__':
    speed_test()
