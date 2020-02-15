o="$(nmcli connection | tail -n +2)"
IFS=$'  '
while IFS= read -r line
do
   tmp=($line)
   nmcli connection delete ${tmp[0]}
done < <(printf '%s\n' "$o")
