#!/bin/bash

# cd report/assets/input

# for i in *.mmd; do
#     ~/.yarn/bin/mmdc -c ../mermaid_config.json \
#          -i "$i" \
#          -o "../${i%.*}.svg"
# done

# for i in *.pikchr; do
#     fossil pikchr "$i" "../${i%.*}.svg"
# done

# cd ../../..

cp report/report.md report/temp_report.md
python report/add_code.py report/temp_report.md

cd report
pandoc metadata.yaml temp_report.md \
        --output=out.pdf \
        --syntax-definition=aqa.xml \
        --pdf-engine=xelatex \
        --table-of-contents \
        --number-sections


rm temp_report.md
cd ..

xdg-open report/out.pdf