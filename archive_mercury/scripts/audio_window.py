import numpy as np, librosa, scipy.signal as ss
d=np.load("scripts/_bands.npz"); t=d["t"]; bt=d["bt"]
hop=256; sr=22050; fr=hop/sr
bass,snare,mid,hi=[d[k] for k in("bass","snare","mid","hi")]
# precise tempo: tempogram-ish via autocorrelation of onset env of full-band within 32-100s
from numpy.fft import rfft
env=bass/np.percentile(bass,99)+snare/np.percentile(snare,99)
seg=env[(t>=32)&(t<100)]; seg=seg-seg.mean()
ac=np.correlate(seg,seg,'full')[len(seg)-1:]
lags=np.arange(len(ac))*fr
for lo,hi_ in((0.38,0.46),(0.78,0.9),(1.6,1.75),(3.3,3.5),(6.6,6.8)):
    m=(lags>=lo)&(lags<=hi_); i=np.argmax(ac[m]); L=lags[m][i]; print("ac peak",lo,hi_,round(L,4),"-> bpm per beat",round(60/L*(L/0.4179),2))
# regress beats 32-100
b=bt[(bt>=32)&(bt<100)]; n=np.arange(len(b)); k,c=np.polyfit(n,b,1); print("beat regress IBI",k,"bpm",60/k,"n",len(b), "resid std",np.std(b-(k*n+c)))
# smoothed 1D envelopes at 30fps
def env30(x,t0):
    tt=t0+np.arange(240)/30
    return np.interp(tt,t,x)
sm=lambda x:ss.savgol_filter(x,9,2)
bn=bass/np.percentile(bass,99.5); sn=snare/np.percentile(snare,99.5)
res=[]
for s in np.arange(10,104-8,0.05):
    a=env30(bn,s); b_=env30(sn,s)
    e0=slice(0,8); e1=slice(232,240)
    cont=abs(a[e0].mean()-a[e1].mean())+abs(b_[e0].mean()-b_[e1].mean())
    # spectral continuity: mid/hi at ends
    m0=np.interp([s,s+0.25],t,mid/np.percentile(mid,99)).mean(); m1=np.interp([s+7.75,s+8],t,mid/np.percentile(mid,99)).mean()
    # bass peaks
    pk,_=ss.find_peaks(a,height=0.5,distance=6)
    act=a.mean()+b_.mean()
    # periodic autocorr similarity of window vs shifted by 8s? use circular cross-corr of window start/end 1s
    st=np.interp(np.arange(30)/30+s,t,bn); en=np.interp(np.arange(30)/30+s+7,t,bn)
    corr=np.corrcoef(st,en)[0,1] if st.std()>1e-6 and en.std()>1e-6 else 0
    # beat phase: offset of start to nearest beat
    ph=np.min(np.abs(bt-s)); phe=np.min(np.abs(bt-(s+8)))
    res.append((s,cont,act,len(pk),corr,ph,phe,m0,m1))
res=np.array(res)
score=res[:,2]*1.0 - 2.0*res[:,1] + 0.5*res[:,4] - 3*np.abs(res[:,7]-res[:,8]) - 2*res[:,6]
o=np.argsort(-score)[:15]
print("s cont act npk corr phS phE m0 m1 score")
for i in o: print(np.round(res[i],3), round(score[i],3))
np.save("scripts/_res.npy",res)
