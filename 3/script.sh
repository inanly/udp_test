tempfile=$(mktemp)

while IFS=: read -r name englishScore unixScore
do
  
  avg=$(echo "scale=2;($englishScore + $unixScore)/2" | bc)

  printf "%-10s %5d %5d avg=%.2f\n" "$name" "$englishScore" "$unixScore" "$avg" >> "$tempfile"
done < testdata.txt

sort -k5 -nr -o "$tempfile" "$tempfile"
cat "$tempfile"
rm "$tempfile"
