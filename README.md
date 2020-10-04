# Неделя 3
1. Создайте произвольный текстовый файл с несколькими строками произвольного текста. Выведите в консоль строки файла, удалив лишние пробелы в начале и конце строк, если они есть (strip).
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
