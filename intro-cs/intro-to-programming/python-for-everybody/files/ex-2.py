try:
    file_name  = input("Enter file name: ")
    file_handle = open(file_name)

    count = 0
    total_spam_confidence = 0

    for line in file_handle:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            slice_index = line.find(':') + 1
            spam_confidence = line[slice_index:].rstrip()
            total_spam_confidence = total_spam_confidence + float(spam_confidence)
        
    print(f"Average spam confidence: {str(total_spam_confidence / count)}")
except:
    quit()


