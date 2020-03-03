import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint,DataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
from mindwavemobile.MindwaveDataPoints import MeditationDataPoint,AttentionDataPoint
import textwrap

if __name__ == '__main__':
	mindwaveDataPointReader = MindwaveDataPointReader()
	mindwaveDataPointReader.start()
	if (mindwaveDataPointReader.isConnected()):
		while(True):
			dataPoint = mindwaveDataPointReader.readNextDataPoint()
			data = DataPoint()
			med = MeditationDataPoint(data)
			value=med.meditationValue
			if (not dataPoint.__class__ is RawDataPoint):
				print(value)
	else:
		print((textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " ")))
