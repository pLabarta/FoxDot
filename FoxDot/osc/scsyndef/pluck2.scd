SynthDef.new(\pluck2,
{|vib=0, rate=0, sus=1, fmod=0, bus=0, amp=1, freq=0, blur=1, beat_dur=1, pan=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
