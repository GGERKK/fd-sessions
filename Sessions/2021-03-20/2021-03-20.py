print(SynthDefs)

Scale.default = Scale.harmonicMinor

a1a = P[0,-2,3,2]
a1b = P[1,2,1,2]
a1c = P[0,2,5,4]
a1 >> keys(a1a | a1b | a1c | a1b, amp=0.7 * var([0,1,0],4), dur=1).every(12, 'offadd', 2)

a2a = P[0,0,0,0,var([0,7,4,13],16),0]
a2b = P[0,5,4,3,4,0]
a2c = P[5,4,3,2,1,0]
a2dur1 = P[0.5,0.25,0.25,0.5,0.5, rest(6)]
a2dur2 = P[0.5,0.5,0.25,0.25,0.5, rest(6)]
a2 >> pianovel(a2a | a2b | a2a | a2c, amp=0.7 *  linvar([1,0.2],64), dur=Pvar([a2dur1,a2dur2],[24,8]), sus=PWhite(2,0.25))

a3 >> hoover([0,5,4,2,3,4,5,6,7,7,8,9,12,3,4,13], amp=0.1 * linvar([0,1],64), cut=1, chop=var([0,4,6,8],[12,4,8,8]))

a_all.stop()

b1 >> harp(amp=0.7 * linvar([0,1],64), dur=var([4,8],8), oct=var([4,(4,3,2)],8), lpf=1500, echo=var([0,3],8), echotime=8).follow(a1)
b2 >> faim(a1a | a1b | a1c | a1b, amp=0.05, dur=8, oct=(4,5,6), chop=var([0,32],[24,8]), lpf=linvar([1000,5000],32), shape=linvar([0.1,0.6],42))

b_all.stop()

c1 >> gong([0,0,0,var([0,7,4,13])], amp=0.6 * linvar([0.3,1],43)).every(6, 'stutter', 4)

c_all.stop()

z1 >> play(' h', amp=0.4, dur=2, hpf=linvar([100,8000],16))
z2 >> play('(-------{be})', amp=0.1)
z3 >> play('x (ooo[llll])( i r l)', amp=0.3, dur=0.5)
z4 >> play('(VVVVVVV[vvv]) ', amp=0.6)

z_all.stop()
