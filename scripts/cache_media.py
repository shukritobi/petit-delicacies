"""Cache merchant's public proposal media locally. Run from repository root."""
from pathlib import Path
import json, urllib.request, time
from PIL import Image, ImageOps
from io import BytesIO
root=Path("assets")
sources=json.loads((root/"media-sources.json").read_text())
success=0
for key,record in sources.items():
    if key=="hero": continue
    target=root/(key+".jpg")
    if target.exists():
        try:
            with Image.open(target) as image: image.verify()
            success+=1
            continue
        except Exception: pass
    try:
        request=urllib.request.Request(record["url"],headers={"User-Agent":"Mozilla/5.0","Referer":record["source"]})
        with urllib.request.urlopen(request,timeout=22) as response:
            data=response.read(15*1024*1024+1)
        if len(data)>15*1024*1024: raise ValueError("asset too large")
        with Image.open(BytesIO(data)) as image:
            image=ImageOps.exif_transpose(image).convert("RGB")
            if min(image.size)<300: raise ValueError("image too small")
            image.thumbnail((1600,1600))
            image.save(target,"JPEG",quality=90,optimize=True)
        success+=1
        print("OK",target)
    except Exception as error:
        print("FAILED",key,type(error).__name__,str(error))
print(f"Cached {success} images")
if success==0: raise SystemExit("No images downloaded; source URLs may be expired.")
