print(SynthDefs)
Clock.reset()

a1 >> borgan(var([(0,2), (-3,-1)],[12,4]), amp=0.2, dur=4, sus=4, atk=linvar([0.1,1], 4), rel=expvar([0,1],16), lpf=3000)
a2 >> faim(P[0,1,5,4] | [0,0,0,0] | [0,1,-3,-2], amp=0.5 * var([1,0],[1.25,6.75]), dur=0.25, sus=0.5, lpf=expvar([200,5000],32), echo=0.35, echotime=linvar([0,4],32))
a3 >> chipsy(P[0,1,2,3,4,5,6,7], amp=0.5 * linvar([1,0.5],64), dur=4, room=0.2, mix=0.4, oct=6, hpf=1000, formant=2)

a2.solo(0)

b1 >> bass([0,1,-6,-4], amp=0.7, dur=8, lpf=1500)

c1 >> bell(P[0,2,3] + var([0,6,3,9],8), amp=0.2, dur=var([1,0.5,0.25],[20,8,4]), oct=6, hpf=3000, pan=(-0.5))
c2 >> pianovel(P[6,4,3,(4,6),8,9,0,0] | [0,1,2,1] | [-2,-4,3,4,(5,7),-6,0,-3,-4], amp=0.8 * var([1,0],[1,2,0.5]), dur=var([3,0.5,2,0.33],[4,2]), delay=PWhite(0,0.25), sus=6, chop=var([0,6],[28,4]))
c3 >> svoice(P[0,1,2,3].shuffle(), amp=0.5, dur=var([2,3,1],[3,5,1]), sus=4, echo=0.4, echotime=4, vib=3, tremolo=4)

c_all.solo(1)

c_all.solo(0)
x3 >> play('xdx[dxdx]', amp=0.6, sample=6, pan=(-1,1), room=1, mix=linvar([0,1],64))

z1 >> play('x   ', amp=0.2, sample=5, lpf=500)
z2 >> play('  (o{qpenbd}) ', amp=0.3, sample=4, pan=(-0.2,0.2))
x1 >> play('h', amp=0.7, dur=var([0.5,0.25],[26,6]), pan=(-0.5,0.5), hpf=3000)
x2 >> play('g', amp=0.5, dur=var([0.5,0.25],[27,5]), sample=P[0,1,2,3,4,5,6].shuffle())

x3 >> play('xdx[dxdx]', amp=0.8, sample=6, pan=(-1,1))

x4 >> play('V (XXXXXXX[oooo]) ', amp=1.3, sample=1, lpf=2000)
x5 >> play('-:h{c-:hjsk}', sample=var([0,3,2],16), chop=2, rate=PWhite(2,-2))
x6 >> play('u', dur=var([0.5,0.25],[28,4]))

x3.solo(0)
x_all.stop()
