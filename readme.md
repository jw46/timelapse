A Python script to do Timelapse videos

Make Video
ffmpeg -framerate 10 -i image%02d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4