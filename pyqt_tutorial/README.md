# PyQT Tutorial #

如何使用 Anaconda 設置 PyQT 來使用 Python GUI

### Setup ###

* Windows系統需先安裝 Anaconda
* Anaconda裡的環境會裝好PyQT

### Content ###

* Anaconda Prompt
* Spyder
* designer.exe

### Step ###

* 開啟 Anaconda Prompt
* Spyder 開啟指令
```
$ spyder
```
* 開啟 designer.exe

$ C:\ProgramData\Anaconda3\Library\bin\designer.exe

* 在 designer.exe裡設計UI，設計完儲存為 XXX.ui

* 用 Anaconda Promt 去到存放 XXX.ui 的資料夾中，打上指令

$ pyuic5 XXX.ui > XXX.py

* 每更新一次重複一次上面指令

* 新增 app.py 檔案，參考內容

* 執行方法

$ python app.py

* 參考來源: https://dotblogs.com.tw/zeus83157/2018/06/23/011440

* 參考來源2: https://blog.daychen.tw/2017/09/pyqt5-part-5-qt-designer-gui.html

* 打包程式參考: https://blog.daychen.tw/2017/03/pyqt5-pyqtdeploy.html

* 打包程式參考2: https://blog.daychen.tw/2017/03/pyqt5-pyqtdeploy_27.html