sentence = 'this is a string, it is very long. so long in fact that it needs to be cut down and parts of it must be moved to lines below'
def paragraph(text):
    textLength = len(text)
    lineLength = 80
    lineStart = 0
    lineEnd = lineLength

    #subtract the rest of the text and put it on the next line
    while textLength > lineStart:
        newLine = text[lineStart:lineEnd]   
        lineStart = lineStart + lineLength 
        lineEnd = lineEnd + lineLength 
        print newLine 

paragraph(sentence)
  
        
        
        

        
