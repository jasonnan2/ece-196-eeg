import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint,DataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
from mindwavemobile.MindwaveDataPoints import MeditationDataPoint,AttentionDataPoint
import textwrap
from mindwavemobile.MindwavePacketPayloadParser import MindwavePacketPayloadParser


if __name__ == '__main__':
	mindwaveDataPointReader = MindwaveDataPointReader()
	mindwaveDataPointReader.start()
	if (mindwaveDataPointReader.isConnected()):
		count=0
		vect=0
		counter=0
		new_count=0
		while(True):
			dataPoint = mindwaveDataPointReader.readNextDataPoint()
			#datab=data._dataValueBytes
			packet=MindwavePacketPayloadParser(dataPoint._dataValueBytes)
			packet2=MindwavePacketPayloadParser(dataPoint._dataValueBytes)
			med=MindwavePacketPayloadParser._createDataPoint(packet,0x05,packet._extractDataRowValueBytes(0x05))
			att=MindwavePacketPayloadParser._createDataPoint(packet2,0x04,packet2._extractDataRowValueBytes(0x04))
			med_str=str(med)
			att_str=str(att)
			med_value=int(med_str[18:len(med_str)])
			att_value=int(att_str[17:len(att_str)])
			counter+=1
			if (not dataPoint.__class__ is RawDataPoint):
				#print(dataPoint)
				diff=counter-new_count
#				print(med)
				if count<10 and med_value>10 and med_value<100 and diff!=1:
#					print(med)
					vect+=med_value
					count+=1
					new_count=counter
				elif count==10:
					new_count=counter
					vect/=10
					count=0
					print(vect)
					if vect<50:
						brightness=1
						vect=0
					else:
						brightness=2
						vect=0
	else:
		print((textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " ")))
