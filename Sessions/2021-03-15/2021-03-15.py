print(SynthDefs)

a1 >> blip(amp=0.5, dur=5)
a2 >> chipsy([0,1,-1,2,-2,3,-3,4], amp=0.5, dur=[1.25,1.25,1.25,1.25,5], lpf=linvar([400,4000],32))
a3 >> flute([5,5,6,4,3,3,0,6,3,2], amp=0.5 * var([0,1],[16,32]), dur=P[0.5,0.25,1,0.25,2], chop=var([5,0,3,0],[4,12,4,16]))

Group(a2,a3).stop()

b1 >> bass([5,2,0,4], amp=0.5, dur=5)
b2 >> sawbass([9,8,7,4], amp=0.6 * linvar([0,1], 16), dur=[1,1,2,3], shape=var([0,0.2,1],[16,8,8]))

b2.stop()

c1 >> organ2(P[0,0.2,0.4,0.6,0.8] | [1,1,2,1,1] | [1,1,3,2,4] | [5,5.2,5.4,5.6,5.8], amp=0.5 * linvar([0.2,1],28), dur=[0.25,1,0.5,0.25,2], cut=0.25, pshift=linvar([0,2],32))
c2 >> rlead(P[0,1,2,3] | [0,1,2,3] | [0,1,2,3] | [3,2,1,0], amp=0.6 * var([1,0],32), hpf=linvar([200,1500],16), pan=0.5)
c3 >> filthysaw([0,2,4,-2], amp=0.3, dur=16, blur=1.5, room=0.4, mix=0.2, chop=0, lpf=expvar([400,5000],128))

c1.stop()

z1 >> play('[xxxx]', amp=0.5, dur=5)
z2 >> play('[hhh]', amp=0.3, dur=5, pan=PWhite(-1,1))

x1 >> play('x o ', amp=0.5, sample=18)
x2 >> play('qp', amp=0.6 * var([0,linvar([0.2,1],8)],[8,32]), sample=[3,1], rate=0.5)

x_all.stop()
