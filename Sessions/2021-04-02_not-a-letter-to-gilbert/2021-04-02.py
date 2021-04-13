# Not the letter to Gilbert

print(SynthDefs)

#foundation... hmmm... how to begin... right now it's just a fade-in in audacity :/ not good enough.
a1 >> bchaos(amp=0.3, dur=var([16,8],64), vib=3, slide=var([0,2],128))

a_all.stop()

#texture
p1 >> bphase([var([0,2,0,4],8),2], amp=0.2, vib=2, shape=linvar([0,0.3],64))
p2 >> pmcrotal(amp=0.2 * var([0,1],32), lpf=500)
p3 >> cluster(amp=0.4 * linvar([1,0.2],24), dur=var([0.125,0.5],[6,2]), pshift=var([0,2,0,4],8))

p_all.stop()

#melodies?
m1 >> pianovel(var([(0,3,5),(2,4,6),(5,7)],[4,4,8]), amp=0.7 * var([1,0],128), vib=4, hpf=200, lpf=5000, room=0.2, mix=0.3).sometimes('offadd', 2)
# the piano is the chillest/most pleasant part... save it for the outro?
m2 >> gbell(amp=0.5, dur=PDur(3,8), pan=linvar([-0.6,0.6],35), hpf=var([0,5000],128), room=0.6, mix=0.3)

m3 >> faim([0,5,-3,5,4,3,var([0,4,5,3],8)], amp=0.5 * var([0.05,1],128), dur=[1,1,1,0.5,0.25,0.25,4], formant=var([2,0],128), room=0.6, mix=var([0,0.2],128), pan=var([0.4,0],128)).sometimes('offadd', 2)
# ^^^ this is almost good... it needs a little more confidence and character
m4 >> drone(P[0,1,2,4], amp=0.7 * var([0,1],128), shape=0.3).every(6, 'reverse')
m5 >> filthysaw(var([0,-2,-4,5],32), amp=0.6 * var([0.3,1],128))

Group(m4,m5).stop()

m_all.stop()

#microphone!
r4 >> soundin(amp=4, amplify=1, room=0.6, mix=linvar([0,1],16), lpf=linvar([400,5000],24), chop=16, pan=linvar([-1,1],16), vib=2)
r4 >> soundin(amp=4, amplify=1, room=0.6, mix=linvar([0,0.3],16), lpf=0, chop=0, pan=linvar([-1,1],16), vib=2)

r4.stop()

#drums
z1 >> play('<x (o[oo]o[ooo]) >', amp=0.8, dur=2, sample=15, room=0.2, mix=0.4, lpf=3500)
z2 >> play('Q', amp=0.7, dur=128, sample=15, rate=var([1,-1],128), delay=var([128,124],128), room=1, mix=linvar([0,1],4)) # this is the weird warp engine sound - stop VERY early!
z3 >> play('<V (o[ooo]o[oooo]) ><h[hhh]h>', amp=0.6 * var([0,1],128), dur=1, sample=12, room=0.4, mix=0.2)
z4 >> play('Q', amp=0.4 * var([0.5,1],128), dur=var([1,0.5],128), lpf=linvar([400,5000],64)) # constant synth hit
z5 >> play('P', amp=0.3 * var([0.3,1],128), dur=var([0.5,0.25],64), sample=13)

Group(z6,z5,z4).stop()

z_all.stop()

#randoooo
x1 >> play('paLinD3r(om)e', amp=0.3, sample=P[0,2,6,1].shuffle(), dur=P[6,3,8].shuffle(10), rate=P[-1,1,2,-2].shuffle(10), room=0.6, mix=0.6)

x_all.stop()

# next we need bass!
b1 >> jbass([0,4,2,var([4,7,-2,0],8), 0], amp=0.6 * var([0.5,1],128), dur=[0.25,0.5,1,0.25, rest(2)])

b_all.stop()






## delay test.. does var
t1 >> blip([7,0,0,0], amp=0.5, dur=2, chop=8)
t2 >> play('Q', amp=0.4, dur=16, sample=15, rate=var([1,-1],16), delay=var([16,12],16), room=1, mix=linvar([0,1],4))
t3 >> sine(var([4,2],16), amp=0.6, dur=[4,rest(12)], delay=0, pan=1)

t_all.stop()
