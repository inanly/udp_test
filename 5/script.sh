function AREA() {
    local width=$1
    local height=$2
    local result=$(echo "$width*$height*0.5" | bc)
    echo "Area = $result"
}

echo "請輸入三角形的底和高："
read width height

AREA $width $height
