echo "請輸入一個整數:"
read N

echo "請輸入檔案名稱:"
read filename

for (( i=1; i<=N; i++ ))
do
    touch "${filename}${i}.txt"
done

echo "已成功建立${N}個檔案!"
