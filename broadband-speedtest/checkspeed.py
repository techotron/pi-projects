import pyspeedtest

i = 0
testLoop = 100

while i < testLoop:

    st = pyspeedtest.SpeedTest(host='www.speedtest.net')
    resultDownload = pyspeedtest.pretty_speed(st.download())

    print('Download: %s') % (resultDownload)

    i += 1


