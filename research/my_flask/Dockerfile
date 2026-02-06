# 1. 使用官方的 Python 3.9 slim 版本作為我們打包的基礎
FROM python:3.9-slim

# 2. 在容器內部建立一個叫做 /app 的工作目錄
WORKDIR /app

# 3. 先只複製需求文件進去，並安裝套件
#    這樣做可以善用 Docker 的快取機制，如果未來程式碼改動但套件不變，就不用重新安裝
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. 將當前目錄下的所有檔案 (.) 複製到容器的 /app 目錄下
COPY . .

# 5. 告訴 Docker，這個容器對外會開放 5000 這個埠號 (Port)
EXPOSE 5000

# 6. 當容器啟動時，要執行的預設指令 (就是運行我們的 app.py)
CMD ["python", "app.py"]