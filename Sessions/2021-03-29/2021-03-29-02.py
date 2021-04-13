# Snoop meets Ye

Clock.clear()
Clock.reset()

print(SynthDefs)

Scale.default = Scale.minorPentatonic

a1a = P[7,6,5,3,5,6,7,13]
a1b = P[0,0,0,0,0,0,0,0]
a1 >> marimba(a1a | a1b, amp=1 * var([1,0], [16,8]), dur=var([1,0.25],[8,8])).every(6, "offadd",2)

a1.stop()

a2 >> drone(amp=0.3, dur=32, slide=1)
a2.stop()

b1 >> dafbass(amp=0.6, dur=[0.5,0.5,1,1], pshift=expvar([0,1],32))
b1.stop()

c1 >> blip([0,8,7,6,7,6,5,6,5,4,3,4], amp=1.5 * var([0,1,0],[16,48,64]), dur=[2,2,0.5,0.5,1,0.5,0.5,1,0.5,0.5,0.5,0.5], cut=0.125, shape=0.5, hpf=4000)

c_all.stop()

c2 >> moogpluck2([-2], amp=0.7, dur=P[4,2,6].shuffle(), blur=4, slide=PWhite(0,-1), shape=1.5, formant=4, chop=0, oct=4)
c3 >> moogpluck([0], amp=0.7, dur=P[4,2,6].shuffle(), blur=4, slide=PWhite(0,-1), shape=1.5, formant=4, chop=0, oct=4)
c3.stop()
c2 >> moogpluck2([0,-2,0,8], amp=0.7 * var([1,0],64), dur=[0.25,0.5,0.25,var([2,3,6,7],[4,3,6,16])], blur=1, slide=0, shape=1, formant=0, chop=var([0,4],[12,4]), oct=5)

d1 >> play('c', amp=0.3, dur=P[4,26,43].shuffle(), sample=P[3,5,4,7,12].shuffle(), room=0.2, mix=0.3, rate=P[2,-2].shuffle())
d1.stop()

z1 >> play('<x o ><{[:::][::::]}>', amp=0.4, dur=1, sample=18, rate=expvar([1,2],32), lpf=linvar([200,5000],64))
z2 >> play('j [jj] j', amp=0.2)
z3 >> play('[dd] dd ', amp=0.4, hpf=linvar([200,2000],16))
z4 >> play(' h h [hh]', amp=0.2)
z5 >> play('V   ', dur=0.25, amp=0.8)

z_all.stop()
