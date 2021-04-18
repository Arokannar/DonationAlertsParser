import random
import requests
import colorama
import time
import os
import threading
import datetime


COLBLUE = colorama.Fore.BLUE
COLCYAN = colorama.Fore.CYAN
COLRED = colorama.Fore.RED
COLGREEN = colorama.Fore.GREEN
COLMAGENTA = colorama.Fore.MAGENTA


def parse() -> object:
	while True:
		try:
			url = "http://static.donationalerts.ru/audiodonations/"
			a = random.randint(11111, 99999)
			b = random.randint(111,999)
			url = url + str(a) + '/'
			url = url + str(a) + str(b) + ".wav"
			r = requests.get(url, stream=True)
			if r.status_code == 200:
				now = datetime.datetime.now()
				ttime = now.strftime("%d_%m %H_%M_%S_%f")
				with open('results/' + ttime + ".mp3", 'wb') as f:
					f.write(r.content)
				print("  " + COLBLUE + url + COLMAGENTA + " - " + COLMAGENTA + "сохранен: " + COLGREEN + str(ttime))
		except:
			print(colorama.Fore.RED + "  Ошибка соеденения")
			time.sleep(2)


def start():
	for _ in range(10):
		threading.Thread(target=parse).start()


if __name__ == "__main__":
	print(COLCYAN + 'by Arokannar with love')
	print(COLCYAN + 'Найдено: ')

	try:
		os.mkdir("results")
	except OSError:
		pass


	start()
