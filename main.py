from neuropy3.neuropy3 import MindWave

mw = MindWave(address='C4:64:E3:E6:F0:A7', autostart=False, verbose=3)

mw.set_callback('eeg', lambda eeg: print(eeg))

mw.set_callback('attention', lambda att: print(att))

mw.set_callback('meditation', lambda med: print(med))

mw.start()

mw.unset_callback('eeg')

mw.stop()