echo "請輸入一個字串："
read input

input_clean="${input// /}"

reverse_input=$(echo "$input_clean" | rev)

if [ "$input_clean" == "$reverse_input" ]; then
    echo "是"
else
    echo "否"
fi
