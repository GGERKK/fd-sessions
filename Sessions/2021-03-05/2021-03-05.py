print(SynthDefs)

a1 >> borgan(var([(0,2), (-3,-1)],[12,4]), amp=0.3, dur=4, sus=4, atk=linvar([0.1,1], 4), rel=expvar([0,1],16))
a2 >> faim(amp=0.4 * var([1,0],[1.25,6.75]), dur=0.25, sus=linvar([0.25,1],3), lpf=expvar([200,5000],32), room=1, mix=0.3, echo=0.35, echotime=linvar([0,4],32))
a3 >> chipsy(P[0,1,2,3,4,5,6,7].shuffle(), amp=0.5 * linvar([1,0.5],64), dur=16, shape=linvar([0.1,2],64), room=0.2, mix=0.4, lpf=1000)

b1 >> bass([0,1,-6,-4], dur=8)

c1 >> xylo(P[0,1,2] + var([0,2,4,6],8), amp=0.6, dur=0.33, oct=6, hpf=3000, pan=(-0.5))
c2 >> pianovel(P[6,4,3,6,8,9].shuffle(4), dur=var([1,0.5,2],[4,2,4,2]), sus=4).every(12, 'offadd', 2)
c3 >> svoice(P[0,1,2,3].shuffle(), dur=var([2,3,1],[3,5,1]), sus=4, echo=0.4, echotime=4, vib=3, tremolo=4)

c_all.solo(0)

z1 >> play('x   ', amp=0.2, sample=5, lpf=500)
z2 >> play('  (o{qpenbd}) ', amp=0.3, sample=4, pan=(-0.2,0.2))
x1 >> play('h', amp=0.7, dur=var([0.5,0.25],[26,6]), pan=(-0.5,0.5), hpf=3000)
x2 >> play('g', amp=0.5, dur=var([0.5,0.25],[27,5]), sample=P[0,1,2,3,4,5,6].shuffle())
x3 >> play('xdx[dxdx]', amp=0.7, sample=6, pan=(-1,1))
x4 >> play('V (XXXXXXX[OOOO]) ', amp=0.8)
x5 >> play('-:h{c-:hjsk}', sample=var([0,3,2],16), chop=2, rate=PWhite(2,-2))
x6 >> play('u', dur=var([0.5,0.25],[28,4]))

x_all.stop()
