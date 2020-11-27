from threading import Thread
import subprocess


if __name__ == "__main__":


    hosts = ["google.com", "yandex.ru", "mail.ru", "vk.com", "bing.com", "yahoo.com",]

    threads = [Thread(target = subprocess.call, args = (["ping", host],)) for host in hosts]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
