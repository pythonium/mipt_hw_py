import zipfile
import os
import pathlib
import re


#stole textloader from maxlaimon :^)
class TextLoader:
    def __init__(self, address):
        with zipfile.ZipFile('sample.zip','r') as sample:
            sample.extractall(address)
        self.path = pathlib.Path('sample')
        self.files = [file for file in list(self.path.glob('**/*')) if file.is_file()]
        self.iterable = iter(self.files)

    def __len__(self):
        return len(self.files)

    def __iter__(self):
        return self

    def __next__(self):
        curr_file = next(self.iterable)

        with curr_file.open('r', encoding = 'utf-8') as file:
            text = file.read()

        with curr_file.open('w', encoding = 'utf-8') as file:
            file.write(self.normalize(text))
        file = curr_file.open('r', encoding = 'utf-8')
        return file

    def normalize(self, text):
        text = re.sub(r'[^\w\s]', ' ', text)
        text = text.lower()
        return text

    def __getstate__(self):
        print("pickling")
        return self.__dict__


    def __setstate__(self, d):
        print("unpickling with these values:" + repr(d))
        self.__dict__ = d
        self.files = [file for file in list(self.path.glob('**/*')) if file.is_file()]


#if __name__ == "__main__":
path = r"C:\Users\plutonium\mipt_hw_py\w9"

loaded = TextLoader(path)

for i in range(len(loaded)):
    try:
        asdf = next(loaded)
        print(asdf.read())
    except StopIteration:
        print("done")
