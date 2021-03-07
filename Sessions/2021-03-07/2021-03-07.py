print(SynthDefs)

a1 >> bell([0,1,2,4,3,3,3,-2], amp=0.4 * var([1,0],[0.5,1,0.5]), dur=P[0.25,0.5,1,2,4].shuffle(), echo=0.25, echotime=3, hpf=2000, delay=(0,PWhite(0,0.5)))

a2 >> pianovel(P[(0,2,4),(4,5,2),(5,8,4),(-2,3,1)].shuffle(), amp=0.5, dur=2, vib=0.2, oct=3)
a3 >> pianovel(P[0,2,3] + P[0,2,4,6].shuffle(), amp=0.7 * var([1,0],[3,2,0.5,1,0.5]), dur=0.5, lpf=expvar([500,2000],25))
a4 >> pianovel(P[6,3,2,1,1,1,1,8,9] | [0,2,-1], amp=0.6 * linvar([1,0.2],64), lpf=expvar([500,2000],42), dur=P[0.5,0.66,1,2].shuffle())

Group(a2,a3,a4).formant=1
Group(a2,a3,a4).chop=3
Group(a2,a3,a4).dur=1

a_all.stop()

a4.solo(0)

b1 >> moogpluck([4,3,2,-4,1,3,2,-2], amp=0.7, dur=4)
b2 >> faim(dur=0.125, lpf=500).follow(b1)
b3 >> gong(dur=12).follow(b1)

b_all.stop()

z1 >> play('X(kskhkb)', amp=0.7, dur=0.5, sample=[0,1,2])
z2 >> play('xo', amp=0.8, dur=0.25, lpf=1000)
x3 >> play('-', amp=0.6 * var([1,0,1],[16,12,4]), dur=var([0.5,0.25,0.125],[24,4,4]), lpf=4000)
x4 >> play('x [xx]O    ', amp=0.8, dur=var([0.25,0.5],16), lpf=linvar([500,2500],32))

z_all.stop()
x_all.stop()
