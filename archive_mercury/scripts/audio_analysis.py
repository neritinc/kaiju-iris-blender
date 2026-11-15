import sys, numpy as np, librosa, scipy.signal as ss
p=sys.argv[1]
y,sr=librosa.load(p,sr=22050,mono=True)
print("dur",len(y)/sr)
hop=256
tempo,beats=librosa.beat.beat_track(y=y,sr=sr,hop_length=hop,start_bpm=140)
bt=librosa.frames_to_time(beats,sr=sr,hop_length=hop)
print("tempo",tempo, "nbeats",len(bt)); print("beats0-12",np.round(bt[:12],3))
ibi=np.diff(bt); print("median IBI",np.median(ibi),"bpm",60/np.median(ibi))
oenv=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop)
tg=librosa.feature.tempo(onset_envelope=oenv,sr=sr,hop_length=hop,aggregate=None)
print("local tempo pcts",np.percentile(tg,[5,25,50,75,95]))
# alt tempo candidates
print("tempo cands", librosa.feature.tempo(onset_envelope=oenv,sr=sr,hop_length=hop,aggregate=None,start_bpm=70)[:3])
S=np.abs(librosa.stft(y,n_fft=2048,hop_length=hop))
f=librosa.fft_frequencies(sr=sr,n_fft=2048)
def band(lo,hi): return S[(f>=lo)&(f<hi)].sum(0)
bass=band(20,150); snare=band(2000,5000); mid=band(150,2000); hi=band(5000,11000)
t=librosa.frames_to_time(np.arange(S.shape[1]),sr=sr,hop_length=hop)
np.savez("scripts/_bands.npz",bass=bass,snare=snare,mid=mid,hi=hi,t=t,bt=bt)
# 1s RMS-ish bands overview
for s in range(0,int(t[-1]),4):
    m=(t>=s)&(t<s+4)
    print(f"{s:4d}s bass={bass[m].mean():8.1f} mid={mid[m].mean():8.1f} snare={snare[m].mean():8.1f} hi={hi[m].mean():8.1f}")
