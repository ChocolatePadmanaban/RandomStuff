from pydub import AudioSegment

file_name = 'breath_in_out.mp3'

endTime= 12*1000

song = AudioSegment.from_mp3(file_name)

extract = song[:endTime]

extract.export('12_sec_Trim.mp3', format='mp3')
