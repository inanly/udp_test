# 上傳 udp_test 到 GitHub（簡短教學）

1) 進入專案資料夾
cd "c:\C++\.vscode\research\udp_test"

2) 建立 .gitignore（範例）
# 建議忽略的檔案
__pycache__/
*.pyc
.vscode/
env/
# 如果使用 Docker 可加：
# .env

3) 初始化 git 並 commit
git init
git add .
git commit -m "Initial commit: udp_test files"

4) 在 GitHub 建 repository（兩種方式）
- 網站方法：登入 GitHub → New repository → 輸入名稱（例如 udp_test）→ 建立 → 複製 HTTPS 或 SSH URL。
- CLI 方法（已安裝 gh 且已登入）：
  gh repo create <your-username>/udp_test --public --source=. --remote=origin --push

5) 若用網站建立，接下來把遠端加上並推送
git branch -M main
git remote add origin https://github.com/<your-username>/udp_test.git
git push -u origin main

(若使用 SSH URL：git remote add origin git@github.com:<your-username>/udp_test.git)

6) 在另一台電腦下載（clone）
git clone https://github.com/<your-username>/udp_test.git
cd udp_test

7) 其他注意事項
- HTTPS 會在 push 時要求帳號密碼或 personal access token；SSH 需事先設定金鑰。
- 如果要讓別人能直接下載，repo 可設為 public。若 private，需給對方存取權或使用 token。
- 若有大檔案（>100MB），請使用 Git LFS。
