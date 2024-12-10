@echo off
setlocal enabledelayedexpansion

rem Loop through all .mp4 and .mkv files in the current directory
for %%f in (*.mp4 *.mkv) do (
    rem Use ffmpeg to cut the video into 120-second segments
    ffmpeg -i "%%f" -c copy -map 0 -segment_time 120 -f segment "%%~nf_part_%%03d.%%~xf"
)

endlocal
