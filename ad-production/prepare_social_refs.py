from pathlib import Path
import subprocess,json,urllib.request
R=Path(__file__).resolve().parent;out=R/'social_refs';out.mkdir(exist_ok=True)
frames=[('gym','IMG_0576.mp4',2.5),('lobby','IMG_0507(1).mp4',3),('study','IMG_0583.mp4',7)]
for label,name,t in frames:
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(R/'sources'/name),'-frames:v','1',str(out/(label+'.png'))],check=True)
clips=[('kitchen','IMG_0514.mp4',0,3),('storage','IMG_0527.mp4',6.5,5),('function','IMG_0586.mp4',2,6),('roof','IMG_0569.mp4',17,7)]
for label,name,t,d in clips:
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(R/'sources'/name),'-t',str(d),'-an','-c:v','libx264','-crf','16','-preset','fast','-movflags','+faststart',str(out/(label+'.mp4'))],check=True)
print('Prepared reference stills and clips',str(out))
