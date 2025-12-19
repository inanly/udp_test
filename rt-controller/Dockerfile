# 1. 建置階段 (Builder)
FROM golang:latest as builder

# 設定工作目錄
WORKDIR /app

# 複製 Go 模組定義並下載依賴
COPY go.mod go.sum ./
RUN go mod download

# 複製原始碼
COPY main.go .

# 編譯 Go 程式 (CGO_ENABLED=0 表示建立靜態二進位檔，不依賴系統 C 函式庫)
RUN CGO_ENABLED=0 GOOS=linux go build -o rt-controller main.go

# 2. 執行階段 (Runner) - 使用超輕量映像檔
FROM alpine:latest

WORKDIR /root/

# 從建置階段複製編譯好的程式
COPY --from=builder /app/rt-controller .

# 啟動指令
CMD ["./rt-controller"]