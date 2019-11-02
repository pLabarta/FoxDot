from __future__ import absolute_import, print_function

from ...SCLang import SynthDef
from ... import Clock, Scale, Root
from ...Settings import FOXDOT_ROOT
import threading, os

class VoiceSynthDef(SynthDef):

    def __init__(self):
        SynthDef.__init__(self, "voice")
        self.add()

    def __call__(self, notes, pos=0, sample=0, **kwargs):

        if "lyrics" in kwargs:
            lyrics = kwargs['lyrics']
        else:
            lyrics = "oo "

        if "dur" in kwargs:
            durations = ",".join(map(str,kwargs['dur']))
        else:
            durations = 1

        if 'file' in kwargs:
            filename = kwargs['file']
        else:
            filename = 'v1'

        if "sex" in kwargs:
            sex = kwargs["sex"]
        else:
            sex = "female"

        if "octave" in kwargs:
            octave = kwargs["octave"]
        else:
            octave = 6

        if "lang" in kwargs:
            language = kwargs["lang"]
        else:
            language = "es"

        scale = ",".join(map(str,Scale.default.semitones))
        tempo = int(Clock.bpm)

        notes = ",".join(map(str,notes))

        dst_path = FOXDOT_ROOT + '/snd/_loop_/' + filename + '.wav'

        root = Root.default

        path = "/media/mathi/Personal/MyBand/2.sound/synthesis/sinsy/RealTimeSingingSynthesis_dl"

        if "model" in kwargs:
            command = f"python {path}/main.py notes={notes} octave={octave} root={root} dur={durations} lang={language} file={dst_path} tempo={tempo} scale={scale} lyrics=\"{lyrics}\" model={model}"
        else:
            command = f"python {path}/main.py notes={notes} octave={octave} root={root} dur={durations} lang={language} file={dst_path} tempo={tempo} scale={scale} lyrics=\"{lyrics}\""

        print("Ejecutando esto:",command)
        threading.Thread(target = lambda : os.system(command)).start()


voice = VoiceSynthDef()
