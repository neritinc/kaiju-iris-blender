import numpy as np, scipy.signal as ss
d=np.load("scripts/_bands.npz"); t=d["t"]
bass,snare=d["bass"],d["snare"]; fr=t[1]-t[0]
IBI=60/143.58
def follow(x,att,rel):
    y=np.zeros_like(x); v=0
    for i,s in enumerate(x):
        k=att if s>v else rel
        a=1-np.exp(-fr/k); v+=a*(s-v); y[i]=v
    return y
bf=follow(bass,0.005,0.18); sf=follow(snare,0.002,0.08)
# onset-based grid fit in 33-79 (drop 2 + breakdown) using bass onsets
on=np.maximum(0,np.diff(bass,prepend=0)); on/=np.percentile(on,99)
best=None
for ph in np.arange(0,IBI,0.002):
    g=np.arange(33+ph,60,IBI); v=np.interp(g,t,on).mean()
    if best is None or v>best[0]: best=(v,ph)
anchor=33+best[1]; print("grid anchor (beat) s",anchor,"score",best[0])
# check grid at other drop (80-100) with same IBI: drift
for lo in (80,):
    bestb=None
    for ph in np.arange(0,IBI,0.002):
        g=np.arange(lo+ph,100,IBI); v=np.interp(g,t,on).mean()
        if bestb is None or v>bestb[0]: bestb=(v,ph)
    n=(lo+bestb[1]-anchor)/IBI; print("drop3 phase vs grid: beats offset",n-round(n))
def sample(x,s): return np.interp(s+np.arange(240)/30,t,x)
def report(s):
    b=sample(bf,s); sn=sample(sf,s)
    pb=np.percentile(bf[(t>=33)&(t<60)],99.5); ps=np.percentile(sf[(t>=33)&(t<60)],99.5)
    print(f"\n=== window start {s:.3f}s  end {s+8:.3f}s ; beats in window {8/IBI:.3f}")
    print(" v1,v240 bass raw/peak", b[0]/b.max(), b[-1]/b.max(), " snare", sn[0]/sn.max(), sn[-1]/sn.max(), " |diff|b,s",abs(b[0]-b[-1])/b.max(),abs(sn[0]-sn[-1])/sn.max())
    # kick = bass peaks on raw band (fast), snare peaks
    rb=sample(bass,s); rs=sample(snare,s)
    pk,_=ss.find_peaks(ss.savgol_filter(rb,5,2),height=0.45*rb.max(),distance=7)
    ps_,_=ss.find_peaks(ss.savgol_filter(rs,5,2),height=0.5*rs.max(),distance=7)
    print(" bass peaks (t_in_window s, abs s, frame1based, rel amp):")
    print("  ",[(round(i/30,3),round(s+i/30,3),i+1,round(rb[i]/rb.max(),2)) for i in pk])
    print(" snare peaks:")
    print("  ",[(round(i/30,3),round(s+i/30,3),i+1,round(rs[i]/rs.max(),2)) for i in ps_])
    print(" baked-env maxima (peak for normalization): bass",b.max(),"snare",sn.max(), "(units: STFT magnitude sums, not Blender units)")
    # beats in window
    g=anchor+np.arange(-200,400)*IBI; g=g[(g>=s)&(g<s+8)]
    print(" grid beats frames:",[round((x-s)*30+1,1) for x in g])
start_beat_n=round((38.85-anchor)/IBI); 
for k in (start_beat_n-1,start_beat_n,start_beat_n+1):
    report(anchor+k*IBI)
report(anchor+round((33-anchor)/IBI)*IBI)
