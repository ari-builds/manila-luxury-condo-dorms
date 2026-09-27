import pathlib,subprocess,json
from PIL import Image,ImageDraw
r=pathlib.Path(__file__).resolve().parent;q=r/'qc';q.mkdir(exist_ok=True)
for n in [1,2,3]:
 p=r/'generated'/f'part{n}.mp4'; info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(p)]));dur=float(info['format']['duration']); print(n,dur,next((s['width'],s['height']) for s in info['streams'] if s['codec_type']=='video'))
 times=[i*.5 for i in range(int(dur*2))]
 sheet=Image.new('RGB',(6*240,((len(times)+5)//6)*452),'#12161b');d=ImageDraw.Draw(sheet)
 for i,t in enumerate(times):
  f=q/f'p{n}_{t:04.1f}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(p),'-frames:v','1','-q:v','2',str(f)],check=True)
  im=Image.open(f);im.thumbnail((236,420));x=i%6*240;y=i//6*452;sheet.paste(im,(x,y+28));d.text((x+5,y+8),f'Part {n} {t:.1f}s',fill='white')
 sheet.save(q/f'part{n}_sheet.jpg',quality=93)
