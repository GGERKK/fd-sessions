Clock.reset()

roust = var([0,2,-2,4],8)

a1 >> klank(roust,amp=0.3)
a2 >> ripple(roust, amp=0.2, dur=4, sus=4, blur=1.2, pan=(-1,1))

Group(a1,a2).degree=0

b1 >> bass([0,2,4,-4,0,2,0,-2], amp=0.3, dur=4, sus=4.2, blur=2)
b1.stop()

c1 >> fmrhodes(P[-2,2] | [-2,2] | [2,1] | 4, amp=0.2, dur=var([0.5,2],[2,2]), echo=0.75, room=1, mix=0.4, pan=-0.3)
c2 >> rlead(P[0,1,2,3] | [0,1,2,3] | [0,1,2,3] | [3,2,1,0], amp=0.6 * var([1,0],32), hpf=linvar([200,1500],16), pan=0.5)
c3 >> filthysaw([0,2,4,-2], amp=0.3, dur=16, blur=1.5, room=0.4, mix=0.2, chop=0, lpf=expvar([400,5000],128))

c3.degree=0

Group(c1,c2).stop()

c_all.stop()

print(SynthDefs)

z1 >> play("x (x[xx]xx) ", amp=0.5, sample=2, shape=0.2)
z2 >> play(' o([ o]oo)', amp=0.2)
z3 >> play('([hh]hh[hh]) h ', amp=0.3, pan=PWhite(-0.5,0.5))
z4 >> play(' (OOOOOO [ee])', dur=0.5, amp=0.3, sample=4, rate=linvar([1,2],32), pan=linvar([-0.7,0.7],32))
z5 >> play('(qw{zmkl})b', amp=0.2, dur=[0.25,0.5,0.25,0.25,0.5,0.25,1,0.5,0.25,0.25], sample=var([0,1],[2]))

Group(z2,z4).stop()
z5.stop()
z_all.stop()
