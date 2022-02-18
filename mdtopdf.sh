#!/bin/bash

mkdir -p /tmp/

in_dir=$(dirname $1)
in_filename="$(basename ${1%.*})"
out_filepath="$in_dir/$in_filename.pdf"


python3 /mdtohtml.py $1 /tmp/


wkhtmltopdf --enable-local-file-access /tmp/$in_filename.html $out_filepath

echo $out_filepath