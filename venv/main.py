#!C:\Users\rdfx\PycharmProjects\qr\venv\Scripts\python.exe

import os
import tempfile
import csv
import zipfile
import tkinter as tk
from tkinter import filedialog
import qrcode

class CreateWindow:
    csvPath = ''
    root = None
    canvas1 = None
    tmpDir = ''
    csvData = {}

    def __init__(self):
        self.tmpDir = tempfile.gettempdir()
        self.root = tk.Tk()

    def drawMainW(self):
        self.root.title('Генератор QR кодов')
        self.canvas1 = tk.Canvas(self.root, width=700, height=300)
        self.canvas1.pack()
        selCSVBtn = tk.Button(text='Select CSV', command=self.selCSV, bg='#ccc', fg='#000')
        self.canvas1.create_window(350, 100, window=selCSVBtn)
        self.root.mainloop()

    def drawStartBtn(self):
        startBtn = tk.Button(text='START', command=self.generateQR, bg='green', fg='#fff')
        self.canvas1.create_window(350, 200, window=startBtn)

    def selCSV(self):
        fn = filedialog.askopenfilename()
        fnPrint = tk.Label(self.root, text=fn, fg='black', font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(350, 150, window=fnPrint)
        self.csvPath = fn
        if len(fn) > 0:
            self.drawStartBtn()
        return fn

    def generateQR(self):
        tmpDir = self.makeTmpDir()
        self.parseCSV()

    def makeTmpDir(self):
        tmpName = os.path.basename(self.csvPath)
        tmpDirPath = os.path.join(self.tmpDir, tmpName)
        if os.path.exists(tmpDirPath) is False:
            os.rmdir(tmpDirPath)
        os.mkdir(tmpDirPath)
        return tmpDirPath

    def parseCSV(self):
        with open(self.csvPath) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=',')
            lineCount = 1
            for row in csvReader:
                if lineCount > 0:
                    self.csvData[lineCount] = {
                        'fileName': row[0],
                        'value': row[1]
                    }
                    lineCount += 1




cl = CreateWindow()
cl.drawMainW()