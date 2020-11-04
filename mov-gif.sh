#!/bin/bash
movie=$1
height=$(mdls -name kMDItemPixelHeight ${movie} | grep -o '[0-9]\+')
width=$(mdls -name kMDItemPixelWidth ${movie} | grep -o '[0-9]\+')
dimensions="${width}x${height}"
name=$(basename ${movie} '.mov')
ffmpeg -i ${movie} -s ${dimensions} -pix_fmt rgb24 -r 10 -f gif ${name}.gif