print(SynthDefs)

a1 >> rhpiano(var([0,4,2,1],[1,2,4,1]), amp=0.4)
a2 >> pianovel(amp=0.4)
a3 >> fmrhodes(var([0,0,1,2],8), amp=0.4, dur=PDur(5,8))
a_all.lpf=40

b1 >> varcell(5, amp=0.5)
b2 >> wbass(var([5,5,6,7],8), amp=0.4)
b_all.lpf=30

c1 >> nylon([5,2,1,2,3,0,4,4,4,3,2,6], dur=[1,0.25,0.5,2,0.25,0.5,0.5], amp=0.6 * var([1,0],26))
c2 >> faim([5,2,1,2,3,0,4,4,4,3,2,6], dur=[1,0.25,0.5,2,0.25,0.5,0.5], chop=[2,0,0,4,0])

c_all.lpf=50

o1 >> klank()
o_all.stop()

z1 >> play('x o ', amp=1)
z2 >> play('x   ', amp=1, sample=4, echo=linvar([0.25,0.6],32))
z3 >> play('-', sample=5)
z_all.stop()
