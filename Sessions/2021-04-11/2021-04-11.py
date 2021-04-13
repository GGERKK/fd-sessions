print(SynthDefs)

a1 >> rhpiano()
a1a = P[0,1,2]
a1.pitch= a1a + var([0,2],8)
a1.amp=0.3 * var([1,0.2],4)
a1.vib=2
a1.oct=6
a1.hpf=4000
a1.hpr=0.1
a1.dur=0.25
a1.cut=0.125
a1.pan=0.8
a1.sometimes('stretch', 2)

a1.solo()
a1.stop()

#------------------------------------------------------------------------------

b1 >> sinepad()
b1a = P[P*(2,5,7,2),P*(7,5,9,-2),1,0]
b1b = P[1,P*(5,6,3,5,2),P*(0,3,4),P*(P*(0,-1,-2,-3,-3,-3,-2),8)]
b1.pitch= b1a.loop(7) | b1b
b1.amp=0.7 * var([0,1],128)
b1.dur=2
b1.pan=(-0.3)
b1.vib=12

b1.stop()

#------------------------------------------------------------------------------

# kinda the main melody
c1 >> fmrhodes()
c1a = P[1,2,P^[2,3,0.5],P^[4,3,2,1/3]]
c1b = P[2,3,5,P^[2,3,1/4]].offadd(var([2,4],2))
c1ab = c1a.loop(3) | c1b
c1c = P[1,2,P^[2,3,2,1/3],P^[4,3,2,1,1/4]]
c1.pitch= c1ab | c1c.loop(4)
c1.amp=0.4 * var([1,0],128)
c1.pan=linvar([-1,1],32)
c1.lpf=var([0,300],128)
c1.cut=var([0,0.25],[12,4])

c1.stop()

#------------------------------------------------------------------------------

d1 >> benoit(var([0,5,4,2],16), oct=4)
d1.amp=0.4 * var([1,0],[4]) # change this over time to bring it in

d1.stop()

#------------------------------------------------------------------------------

e1 >> harp()
e1a = P[0,5,1,P*(2,5,4)]
e1b = P[7,4,5,P*(0,2,2)]
e1c = P[4,P*(2,1,0,-1,-2,-3),-2,P*(8,4,2)]
e_1 = e1a | e1b | e1a | e1c
e1.pitch= e_1 | P[P*(5,4,3,2)].loop(4)
e1.amp=1 * var([1,0],[8]) # change this over time to bring it in
e1.dur=var([4,2],64)
e1.pan=PWhite(-1,1)
e1.room=0.5
e1.mix=linvar([0,0.5],16)
e1.lpf=sinvar([1000,5000],32)
e1.sometimes('offadd',2)

e1.stop()

#------------------------------------------------------------------------------

f1 >> fuzz()
f1.amp=0.4 * linvar([0,1],128)
f1.dur=[2,rest(0.5)]

f1.stop()

#------------------------------------------------------------------------------

x1 >> play('(v[v   v v]v[   v v]) (f[f f ]ffff[ff]) ', sample=2)
x2 >> play('ppp[pp]', sample=P[0,1,2,3,4,5].shuffle(), dur=PDur(3,8))
x_all.lpf=var([0,900],64)

x_all.stop()

#------------------------------------------------------------------------------

z1 >> play('{jei}{cwh}', amp=0.2, sample=P[3,5,6,12,0,1].shuffle(), dur=P[4,3,6,5,1].shuffle(), room=0.6, mix=PWhite(0,0.5), delay=PWhite(0,0.5), rate=P[2,1,-2,-1].shuffle())

z1.stop()
