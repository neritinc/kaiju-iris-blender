import sys,subprocess,numpy as np
F=r"C:\Users\neritinc\Music\Spotify Downloader\ffmpeg.exe"
W,H=72,128
for v in ("0836","6422","7563","9135"):
    r=subprocess.run([F,"-v","error","-i",f"referencia/IMG_{v}.MP4","-vf",f"fps=2,scale={W}:{H}","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True)
    a=np.frombuffer(r.stdout,np.uint8).reshape(-1,H,W,3).astype(float)
    px=a.reshape(-1,3); lum=px.mean(1)
    key=((px//32).astype(int)*np.array([64,8,1])).sum(1)
    cnt=np.bincount(key,minlength=512); order=np.argsort(-cnt)
    out=[]
    for k in order[:12]:
        m=key==k; c=px[m].mean(0).astype(int); out.append((round(cnt[k]/len(px)*100,1),"#%02X%02X%02X"%tuple(c)))
    # saturated accents: pixels with high chroma
    mx=px.max(1); mn=px.min(1); sat=(mx-mn)/np.maximum(mx,1); sel=(sat>0.6)&(mx>150)
    ac=[]
    if sel.sum():
        ks=key[sel]; c2=np.bincount(ks,minlength=512); 
        for k in np.argsort(-c2)[:6]:
            m=(key==k)&sel; ac.append((round(m.sum()/len(px)*100,1),"#%02X%02X%02X"%tuple(px[m].mean(0).astype(int))))
    g=a.mean(3); d=np.abs(np.diff(g,axis=0)).mean((1,2))
    print(v,"n",len(a),"mean luma %.3f"%(lum.mean()/255),"dark<26: %.1f%%"%(100*(lum<26).mean()),"bright>204: %.1f%%"%(100*(lum>204).mean()))
    print("  dominant",out); print("  saturated accents",ac)
    print("  2fps diff mean %.1f p90 %.1f  >40: %d of %d"%(d.mean(),np.percentile(d,90),(d>40).sum(),len(d)))
