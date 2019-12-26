#!/bin/sh

cd ~/dev/python/NFLML/data/cleaned/

# subroutine to make it clean
clean() {
    
    for file in ./*.csv; do
        sed -i '' 's/^.\{1\}//' $file
    done
}

clean
