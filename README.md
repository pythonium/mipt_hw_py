# Неделя 3
1. Создайте произвольный текстовый файл с несколькими строками произвольного текста. Выведите в консоль строки файла, удалив лишние пробелы в начале и конце строк, если они есть (strip).
**1.py**
in:
```python
with open("1.txt", "r") as file:
        for line in file:
                print(line.strip())
```
out:
```python
hello world!!
goodbye world!!
```
2. Запишите в новый файл содержимое списка строк (каждую строку с новой строки) без использования цикла.
**2.py**
in:
```python
def write_array(array, file_name):
        array = '\n'.join(array)
        file_name.write(array)

array = ["hello", "user", "i'm", "glad", "to", "see", "you"]
with open("2.txt", "w") as file:
        write_array(array, file)
with open("2.txt", "r") as file:
        for line in file:
                print(line)
```
out:
```python
hello
user
i'm
glad
to
see
you
```
3. Вам дана в [архиве](http://cs.mipt.ru/advanced_python/extra/lab3/main.zip) файловая структура, состоящая из директорий и файлов.
Необходимо распаковать этот архив **средствами языка python**, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в **лексикографическом порядке**.
**3.py**
```python
def write_array(array, file_name):
        array = '\n'.join(array)
        file_name.write(array)

main_zip = zipfile.ZipFile("main.zip")
main_zip.extractall("main")

main_zip.close()
folder = []
for root, dirs, files in os.walk("main"):
        for file in files:
                if file.endswith(".py"):
                        folders = root.split('\\')
                        if folders[-1] not in folder:
                                folder.append(folders[-1])
folder.sort()
with open("3.txt", "w") as file:
        write_array(folder, file)
with open("3.txt", "r") as file:
        for line in file:
                print(line)
```
out:
```python
abslw
afkgv
armko
auqky
axqur
bcsow
bdcjg
bkfog
bpmhg
cazio
ckaab
ddnaa
djozj
dnyyv
dufxr
frtrl
ggfcr
grnfu
gvbnv
hapry
hgyoc
hlgup
hotgx
iaujh
iglcm
ilogc
isyki
itkcz
ivjta
izwwv
joejy
jqjsg
jqnsz
jtmnb
juoxd
jvmme
kafov
kehsm
kgdme
kjmeo
ksnof
ktkfx
kwawh
lirot
lldpv
lradw
lszec
main
mhqps
mmtsz
mwhci
nfcxf
nuiwj
otofk
phcap
phcud
purto
pxjip
qkseh
qosgw
qrxwt
qwlrx
rbyav
rcsvd
reshp
rhvqn
rjqjr
rnqwd
rpnzm
rvsfo
rwwuw
rzgzv
sgmoj
sitdc
sosdj
subdi
sxojq
taivr
tpdvr
tyapv
uaodv
ujtgh
uuyrs
uvvuz
vkntp
vydse
vynzv
wfnda
wtgrc
wthmo
wvwva
xjrqt
xpmcm
xriod
xroxl
xrvnu
xsbzr
yujjk
ywjka
ywjxy
ywucw
zfukg
zljoz
zyczx
```
7. Создать код, который выбрасывает `ZeroDivisionError`. Обернуть его в `try/except` и вывести "Делим на ноль" в случае деления на ноль.
**8.py** (случилась чехарда с названиями)
```python
try:
        x = 8/0
except ZeroDivisionError:
        print("Делим на ноль")
```
8. Создать код, который может выбросить `ValueError` (_это может быть попытка привести к `int` "плохую" строку_).
Окружить код `try/except` и добавить `finally` блок, где вывести "Дошел до finally".
Попробовать запустить программу нормально (без выбрасывания исключения) и с исключением.
В обоих случаях должен выполняться код из `finally`.
**9.py**
in[1]:
```python
try:
        int("asdf")
except ValueError:
        print("не интуится(((")
finally:
        print("дошел до \"finally\"")
```
out[1]:
```python
не интуится(((
дошел до "finally"
```
in[2]:
```python
try:
        int("235")
except ValueError:
        print("не интуится(((")
finally:
        print("дошел до \"finally\"")
```
out[2]:
```python
дошел до "finally"
```
9. Создать свое исключение (название любое).
Написать код, который выбрасывает его с неким сообщением.
**Не перехватывайте** это исключение в коде - цель задания заключается в том, чтобы увидеть, как он отображается в консоли.
**10.py**
in:
```python
class WrongUserName(Exception):
    def __init__(self, username):
        self.username = username
        self.message = "no such username"
        super().__init__(self.message)

username = 'maxlaimon'
if username != 'plutonium':
        raise WrongUserName(username)
```
out:
```python
Traceback (most recent call last):
  File "10.py", line 9, in <module>
    raise WrongUserName(username)
__main__.WrongUserName: no such username
```
10. Написать код, который вызывает функции в порядке `a() -> b() -> c()`, а в функцию `c` заложите `raise ValueError('my exception')` (_функции `a`, `b`, `c` надо самому объявить_).
Посмотрите на стек-трейс - видно ли, где из трех функций появилась ошибка?
Сделайте скриншот, залейте в репозиторий и будьте готовы ответить на вопросы по чтению stack trace.
**11.py**
in:
```python
def a():
        print("This is function a")
def b():
        print("This is function b")
def c():
        raise ValueError('my exception')
        print("This is function c")
a()
b()
c()
```
out:
```python
This is function a
This is function b
Traceback (most recent call last):
  File "11.py", line 11, in <module>
    c()
  File "11.py", line 7, in c
    raise ValueError('my exception')
ValueError: my exception
```
