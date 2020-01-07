# startup.py
# ----------
# This file is loaded on startup of FoxDot. You can edit it to include any code
# you want to run at the beginning of a session. To use an alternate startup
# file use the --startup flag followed by a valid path. You can also run FoxDot
# with a --no-startup flag to not load this file.

# CHANGE AMP/DUR of Group

def changeDur(rate,group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].dur = float(group.players[i].dur)*rate
            except:
                print("ERROR")
                print(group.players[i].dur)
                print(help(group.players[i].dur))

def changeAmp(rate, group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].amp = float(group.players[i].amp)*rate
            except:
                print("ERROR")
                print(group.players[i].amp)
                print(help(group.players[i].amp))
                
# Abajo/Arriba Silence Drums

def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(0)
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())

# Modify Sample Rates/Notes

def note2index(note):
    scale = list(Scale.default)
    return scale[note]
    
def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1):
    rates = []
    for nota in list(notas):
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

def sample2notes(notas,sample="b",dur=1,oct=0,player=p1):
    rates = []
    for nota in list(notas):
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> loop(sample,dur=var(dur,4), rate=var(rates,dur),amp=1)
    
funciones_extra = 'changeDur(rate,group=d_all), changeAmp(rate, group=d_all), abajo(), arriba(), abajoarriba(intervalo), note2index(note), play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1), sample2notes(notas,sample="b",dur=1,oct=0,player=p1)'
print(f'Funciones extras cargadas: {funciones_extra}')
print('Podes usar print(funciones_extra) para volver a verlas')
