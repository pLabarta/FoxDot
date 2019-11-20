SynthDef.new(\striate,
{|bus, buf, rate, sus, striate|
var osc;
osc = In.kr(bus, 1);
rate = (BufDur.kr(buf) / sus);
rate = Select.kr(rate > 1, [1, rate]);
osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate;
ReplaceOut.kr(bus, osc)}).add;