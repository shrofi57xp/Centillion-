import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

q = queue.Queue()

model = Model("model/vosk-model-small-en-us-0.15")

def listen():

    rec = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=lambda indata,frames,time,status:q.put(bytes(indata))
    ):

        while True:

            data = q.get()

            if rec.AcceptWaveform(data):

                text = rec.Result()

                if "centillion" in text.lower():

                    return True