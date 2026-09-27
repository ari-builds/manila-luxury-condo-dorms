import pathlib,subprocess,json
R=pathlib.Path(__file__).resolve().parent;G=R/'generated';O=R/'output';O.mkdir(exist_ok=True)
clips=[G/f'part{i}.mp4' for i in range(1,4)]
infos=[json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)])) for p in clips]
vids=[next(s for s in inf['streams'] if s['codec_type']=='video') for inf in infos]
assert len({(v['width'],v['height']) for v in vids})==1
w,h=vids[0]['width'],vids[0]['height']; assert (w,h)==(1080,1920)
# Lobby occupies frames 48 through 90 inclusive. Remove it completely.
segments=[(0,0,48),(0,91,240),(1,0,192),(2,0,240)]
fps=24;total=sum(e-s for _,s,e in segments)/fps
cmd=['ffmpeg','-v','error','-y']
for p in clips:cmd+=['-i',str(p)]
cmd+=['-i',str(G/'music.wav')]
f=[]
for j,(i,s,e) in enumerate(segments):
 f.append(f'[{i}:v]trim=start_frame={s}:end_frame={e},setpts=PTS-STARTPTS,setsar=1[v{j}]')
 f.append(f'[{i}:a]atrim=start={s/fps}:end={e/fps},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,apad,atrim=duration={(e-s)/fps}[a{j}]')
f.append(''.join(f'[v{j}][a{j}]' for j in range(len(segments)))+'concat=n=4:v=1:a=1[vcat][acat]')
f+=[f"[vcat]ass='{O/'titles.ass'}'[vout]",f'[acat]volume=0.14,afade=t=in:d=0.2,afade=t=out:st={total-.9}:d=0.9[amb]',f'[3:a]atempo={28/total},atrim=duration={total},asetpts=PTS-STARTPTS,aresample=48000,loudnorm=I=-18:TP=-2:LRA=7,afade=t=in:d=0.3,afade=t=out:st={total-1.2}:d=1.2[music]','[amb][music]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.85[aout]']
out=O/'Manila_Luxury_Condo_Dorms.mp4'
cmd+=['-filter_complex',';'.join(f),'-map','[vout]','-map','[aout]','-t',str(total),'-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','256k','-ar','48000','-movflags','+faststart',str(out)]
subprocess.run(cmd,check=True)
print(json.dumps({'file':str(out),'width':w,'height':h,'duration':total,'frames':int(total*fps),'size_mb':out.stat().st_size/1e6},indent=2))
