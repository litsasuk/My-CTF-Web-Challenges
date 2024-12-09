#!/bin/sh
sed -i "s/D0g3xGA{www_ttt_pharpharphar}/$GZCTF_FLAG/" /root/flag

export GZCTF_FLAG=""
service apache2 start
tail -f /dev/null