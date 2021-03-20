print(SynthDefs)


b1 >> dorgan([-2,0,3,5], amp=0.5, dur=8, sus=8, oct=3, slide=2, slidedelay=0.45, chop=var([0,linvar([1,32],16)],[56,8]))
b2 >> tremsynth(amp=0.4, echo=linvar([0.33,0.66],32), chop=var([0,2,4,6],8)).follow(b1)

b1.degree = [-2,0,3,var([5,7],32)] # main
b1.dur = 8
b1.sus = 8
b1.slide = PWhite(-0.5,2)

b1.degree = P[0,1,2,3] # rising
b1.dur = 4
b1.sus = 4
b1.slide = -1

b1.degree = P[var([7,5,7],16),5,var([4,2],16),2]

b1.dur=4

c1 >> razz(amp=1, dur=4, chop=8, room=0.4, mix=expvar([0,1],24))

d1 >> pmcrotal([var([-2,-4,-6],8),0,var([3,5,7],4),5], amp=0.25, dur=P[var([1,0.5,0.5],1),0.25,0.25,0.5] * 2, chop=P[0,0,2,4].shuffle(), lpf=expvar([5000,500],64))

d1.formant=0

x1 >> play('R', amp=0.1 * expvar([1,0],8), dur=64, sample=(8,7,9), echo=0.5, echotime=16, room=1, mix=0.5)

z1 >> play('<x o ><wld({dSsh})>', amp=0.5, sample=15, lpf=4000)
z2 >> play('-', amp=0.1, sample=4, pan=linvar([-1,1],12))

# normal params
Master().bpm=120
z_all.formant=0
c1.amp=1
Group(b2,c1,z_all).lpf=var([0,400],[64,64])
d1.hpf=0

# far away breakdown
Master().bpm=60
z_all.formant=1
c1.amp=0
Group(b2,c1,z_all).lpf=400
d1.hpf=3000
