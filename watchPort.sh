tput sc
while :; do
    tput rc
    netstat -tulpn 2>/dev/null | grep "LISTEN"
    sleep 0.5
done
