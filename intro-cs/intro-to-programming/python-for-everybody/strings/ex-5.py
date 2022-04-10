str = 'X-DSPAM-Confidence:0.8475'

start = str.find(':')

print(float(str[start + 1: ]))

