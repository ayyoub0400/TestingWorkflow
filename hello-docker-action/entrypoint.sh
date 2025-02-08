#!/usr/bin/bash

set -e

usertext=""
while [ $# -gt 0 ]; do #whilst number of inputs is more than one
    case "$1" in

    --usertext)
        usertext="$2"
        shift 2
        ;;
    
    *)
        echo "unknown argument: $1"
        shift
        ;;
    esac
done

if [ -z "$usertext" ]; then
    usertext="World"
fi

usermessage="Hello, $usertext"
echo "::set-output name=greeting::$usermessage"

