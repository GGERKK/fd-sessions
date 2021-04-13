print(SynthDefs)

Clock.bpm=linvar([96,110],32)

Scale.default=Scale.minor

a1 >> pianovel()
a1a = P[3,3,P*(4,3,var([2,5,-2,1],8),3),0]
a1b = P[P*(4,7,3),0,-2,0]
a1.pitch= a1a.loop(3) | a1b
a1.amp=0.8 * var([1,0],[6,2])
a1.vib=12
a1.hpf=230
a1.lpf=2510
a1.delay=PWhite(0,0.12)
a1.sometimes('layer', 2)
a1.sometimes('offadd', 2)
a1.solo(0)

a1.stop()

#------------------------------------------------------------------------------

b1 >> benoit()
b1_susdur = 8
b1.pitch=P[3,5,1,P*(0,4,2,2,0)]
b1.amp=0.6
b1.dur=b1_susdur
b1.sus=var([b1_susdur,b1_susdur/4],[24,8])
b1.vib=2
b1.lpf=503
b1.hpf=18
b1.solo(0)

b1.stop()

#------------------------------------------------------------------------------

c1 >> klank()
c1.amp=0.6
c1.vib=4
c1.slide=2
c1.oct=4
c1.shape=0.5

c1.stop()

#------------------------------------------------------------------------------

d1 >> play('for')
d2 >> play('your')
d3 >> play('eyes')
d4 >> play('only')
d_all.sample=33
d_all.amp=0.4
d_all.formant=var([2,0],32)
d_all.dur=PDur(3,8)
d_all.room=0.5
d_all.mix=var([0,linvar([0.8,0],16)],16)
d_all.lpf=var([0,linvar([400,6000],64)],64)

d_all.stop()

#------------------------------------------------------------------------------

e1 >> bell()
e1a = P[P*(7,6,2,-2),0]
e1b = P[P*(4,3,1),6]
e1.pitch= e1a.loop(2) | P[0,0] | e1b | P[7,0].loop(3)
e1.amp=0.45
e1.hpf=121
e1.lpf=5000
e1.echo=var([0,0.28],[4,1])
e1.delay=PWhite(0,0.12)
e1.rarely('reverse')
e1.solo(0)

e1.stop()

#------------------------------------------------------------------------------

z1 >> play('  (yy{[yy][  yy]}y) ', hpf=481, lpf=3500)
z2 >> play('(vvv[vv]) ', sample=2, hpf=121, lpf=481)
z3 >> play('s', sample=3, hpf=2500, lpf=11000)
z_all.amp=1
z_all.room=0.8
z_all.mix=var([0,linvar([0.8,0],16)],16)

z_all.stop()
