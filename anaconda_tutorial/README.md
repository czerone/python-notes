# Anaconda Tutorial #

如何開啟 Anaconda 操作切換版本

### Setup ###

* Windows系統需先安裝 Anaconda

### Content ###

* Anaconda Prompt

### Create Environment ###

* 開啟 Anaconda Prompt
* 創建新環境
```
$ conda create -- name <env_name> <package_names>
```
* 切換環境

$ activate <env_name>

* 退出環境

$ deactivate

* 顯示已創建環境

$ conda env list

* 複製環境

$ conda create --name <new_env_name> --clone <copied_env_name>

* 刪除環境

$ conda remove --name <env_name> --all

* 查看安裝package

$ conda list

* 參考來源:https://zhuanlan.zhihu.com/p/32925500