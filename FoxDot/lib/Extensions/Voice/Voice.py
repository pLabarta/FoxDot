from __future__ import absolute_import, print_function

import os

from .Composer import compose
from .VoiceSpecificator import generateVoiceSpecification

def renderizeVoice(outputName,lyrics,notes,durations,tempo,scale,sex,foxdot_root):

	# Constants
	FILES_ROOT = os.path.realpath(foxdot_root + "/lib/Extensions/VRender/tmp/")
	LAST_MIDI = FILES_ROOT + "/last_midi_generated_by_vrender.mid"
	VOICE_XML_ORIGINAL=FILES_ROOT + "/last_voice.musicxml"
	VOICE_XML_PROCESSED=FILES_ROOT+"/last_voice.xml"

	WAVS_ROOT = os.path.realpath(foxdot_root + "/snd/_loop_/")
	LAST_VOICE_WAV = WAVS_ROOT + "/last_voice_generated.wav"

	compose(notes,durations,scale,LAST_MIDI,VOICE_XML_ORIGINAL)

	lyrics = tokenize(lyrics)

	generateVoiceSpecification(lyrics,tempo,VOICE_XML_ORIGINAL,VOICE_XML_PROCESSED)

	os.popen("LD_LIBRARY_PATH=/usr/lib /home/mathi/Desktop/MyBand/2.sound/synthesis/sinsy/RealTimeSingingSynthesis/synthesisSoftware/Sinsy-NG-0.0.1/build/sinsyNG -t "+str(tempo)+" -m es -o " + LAST_VOICE_WAV + " " + VOICE_XML_PROCESSED)

	os.system("rm -f " + WAVS_ROOT + outputName + ".wav")

	os.system("cp " + LAST_VOICE_WAV + " " + WAVS_ROOT + "/" + outputName + ".wav")

def tokenize(text):
	textSyllables = cleanText(text)
	return filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-"))

def cleanText(text):

	text.replace("\n"," ")
	text = text.lower()

	symbolsToDelete = ".,'!?" + '"'
	for symbol in symbolsToDelete:
		text = text.replace(symbol,"")

	return text
