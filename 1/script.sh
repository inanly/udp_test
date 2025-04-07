while IFS=":" read -r product price quantity
do
  total=$((price * quantity))
  total=$(printf "%'.0f\n" $total)
  printf "%-10s %5d %5d %10s\n" $product $price $quantity $total
done < product.txt
