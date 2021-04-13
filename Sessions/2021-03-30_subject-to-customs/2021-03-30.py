print(SynthDefs)

basicProg = P[5,4,0,var([1,6,-2],16)]

# atmosphere
a1 >> creep(basicProg, oct=var([3,4,5],[16,12,4]), dur=16, amp=0.25, room=0.8, mix=0.4, chop=var([0,4,0,8],[12,4]), formant=linvar([0,2],12), slide=2)
a2 >> klank(basicProg, oct=var([3,4,5],[16,12,4]), dur=8, amp=0.3, room=0.7, mix=0.2, chop=var([0,4,0,8],[12,4]), formant=linvar([0,2],12))
a3 >> swell(basicProg, oct=var([3,4,5],[16,12,4]), dur=16, amp=0.3, atk=0.25, room=0.7, mix=0.2, chop=var([0,4,0,8],[12,4]), formant=linvar([0,2],12))

a_all.stop()

# foundation / play with amp (0.02) + formant 1 and shape 2-4
k1 >> rsaw(basicProg, oct=(3,4), amp=0.125 * linvar([1,0.5],15), dur=var([2,2,1.5,4],[32,24,4,4]), formant=0, shape=0, atk=0.25, hpf=var([0,300,600,1000],16))
k2 >> filthysaw(basicProg.reverse(), amp=0.5 * linvar([0.5,1],12), dur=0.5, hpf=1000, hpr=var([0.3,0.6],[4,5,6]))

k1.amp=0.005
k1.formant=2
k1.shape=4
k1.tremolo=0.05
k1.pshift=0

k_all.stop()

b1a = P[0, 6,8,0,2, 4,2,-2, 0]
b1b = P[0, 2,6,8,4, 4,5,-2, 0]
b1 >> pbass(b1a | b1b, amp=0.4, dur=[rest(2), 0.5,0.25,1,0.25, 0.5,1.5,2, rest(2)], lpf=linvar([1500,200],32))
b2 >> bass(amp=0.4, dur=[rest(2), 0.5,0.25,1,0.25, 0.5,1.5,2, rest(2)], chop=var([0,4],[28,4])).follow(b1)

b_all.amp=0.02
b_all.formant=1
b_all.shape=4

b_all.amp=0.5
b_all.formant=0
b_all.shape=0

b_all.stop()

c1 >> nylon(basicProg, amp=0.4 * var([0,1],32), dur=P[0.25,0.5,0.125,0.125].shuffle(10), chop=var([0,2],[3,4,2]), formant=var([0,2],[28,4]))
# this needs a one direction linvar.
c2 >> faim(basicProg.reverse(), amp=0.35, dur=var([4,2,1,0.5,0.25],[16,8,4,2,2]), cut=0.5, vib=2, room=0.2, mix=0.3, lpf=5000, pshift=PWhite(-0.05,0.05), delay=PWhite(0,0.1)).sometimes('offadd', 2)

c_all.stop()

# drums
z1 >> play('<v( v  )  ><  (ooo[oo]) >', amp=0.7, dur=var([1,1,0.5],[32,26,8]), sample=15, rate=0.75, room=0.3, mix=linvar([0,1],64), lpf=0, lpr=0.7)
z2 >> play('<#!FR>', amp=0.6 * var([1,0],[1,31]), room=0.6, mix=0.2)
z3 >> play('V', amp=0.8, dur=var([4,2,1,0.5,0.25],[48,8,4,2,2]), lpf=800)
z4 >> play('-', amp=0.15 * var([1,1,0],[32,28,4]), dur=0.25, hpf=8000, echo=0.75)
z5 >> play(' r', amp=0.05, dur=1, sample=13, rate=P[1,1,2,-1,2,3].shuffle(), pan=PWhite(-1,1))

z_all.stop()

# play!
g1 >> play(P['what Is Ggoing Onon?'].shuffle(), sample=P[4,3,5,12,2].shuffle(), rate=PWhite(-2,2), dur=[5,3,6,3,2], amp=0.15)
g2 >> play(P['Ionaevnknow'].shuffle(), sample=P[9,7,6,11,22].shuffle(), rate=P[1,2,-2,1].shuffle(10), dur=[6,2,1,4,2], amp=0.05)

g_all.room=var([0,0.6],6)
g_all.mix=var([0,0.7],6)

g_all.stop()
