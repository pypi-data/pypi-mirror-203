#!/bin/bash

cd report
cp report.md temp_report.md

sed -i -e 's/≠/!=/g; s/≤/<=/g; s/≥/>=/g; s/╭/ /g; s/─/ /g; s/├/ /g; s/└/ /g' temp_report.md

pandoc metadata_no_font.yaml temp_report.md \
        --output=out.pdf \
        --syntax-definition=aqa.xml \
        --table-of-contents \
        --number-sections

rm temp_report.md

cd ..

# xdg-open report/out.pdf
