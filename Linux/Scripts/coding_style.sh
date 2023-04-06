#!/bin/zsh

if [[ ! -f "$1" ]]; then
    echo -e "[\e[31mERROR\e[0m] No such file $1"
    return 
fi

cp "$1" /tmp/$(basename "$1")
clang-format -i "$1"
echo "Formatted $1"
