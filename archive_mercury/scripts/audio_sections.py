import numpy as np, scipy.signal as ss
d=np.load("scripts/_bands.npz"); t=d["t"]
bass,snare,mid,hi=[d[k] for k in("bass","snare","mid","hi")]
fr=t[1]-t[0]
b1=np.array([bass[(t>=s)&(t<s+0.5)].mean() for s in np.arange(0,134,0.5)])
print("bass 0.5s (x=index/2 s):")
for i in range(0,len(b1)):
    if 8<=i/2<=110: print(f"{i/2:5.1f}:{b1[i]:6.0f}",end=" | " if i%8!=7 else "\n")
# grid phase: onsets of bass in 32-60
IBI=60/143.58
env=bass/np.percentile(bass,99)
tt=np.arange(32,60,0.005); e=np.interp(tt,t,env)
best=None
for ph in np.arange(0,IBI,0.005):
    g=np.arange(32+ph,60,IBI); v=np.interp(g,t,env).mean()
    if best is None or v>best[0]: best=(v,ph)
print("best beat-phase offset",best, "grid anchor", 32+best[1])
