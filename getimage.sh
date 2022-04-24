#!/usr/bin/env bash

videos_root=/home/
save_root=/home/output/

for video in $videos_root/*.mp4;
do
ffmpeg -i $video -f image2  -vf fps=fps=5 -qscale:v 2 $save_root${video##*/}-%05d.jpeg

done