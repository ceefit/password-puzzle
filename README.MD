### Running Backend with auto-reload

```bash
gunicorn application:application -b :8080 --worker-class aiohttp.GunicornWebWorker --workers=1 --reload --access-logfile - 

```

### Generating Favicons from SVG, the hard way:
```bash
inkscape --export-png=favicon.png --export-dpi=200 --export-background-opacity=0 --without-gui logo.svg

favicon_sizes=(32 57 76 96 120 128 144 152 167 180 192 195 196 228)	

for favicon_size in "${favicon_sizes[@]}"     
do
   convert favicon.png -resize "${favicon_size}x${favicon_size}" "favicon-${favicon_size}".png  
done
```