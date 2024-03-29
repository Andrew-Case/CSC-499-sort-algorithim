def main():
    
    order = ''
    #ask for ascending or descending order
    while order != 'a' and order != 'd':
        order = input("Please enter a for ascending order or d for descending order. ")
    
    #open file, read and record lines
    nameFile = open('Sort Me.txt', 'r', encoding='utf-8')
    nameFileLines = nameFile.readlines()
    
    #open clean file or make if doesn't exist, write
    cleanFile = open('Clean File.txt', 'w+', encoding='utf-8')
        
    #for every name in the file write to clean file without spaces
    for name in nameFileLines:
        cleanFile.write("%s" % name.replace(' ', ''))
        
    #open clean file, read
    cleanFile = open('Clean File.txt', 'r', encoding='utf-8')
    
    #record lines and then sort them
    cleanFileLines = cleanFile.readlines()
    if order == 'a':
        cleanFileLines.sort()
    else:
        cleanFileLines.sort(reverse = True)
    #open alphabetical file or creat if doesn't exist, write
    alphabeticalFile = open('Alphabetical File.txt', 'w+', encoding='utf-8')
    
    #write the sorted names into the file
    for name in cleanFileLines:
        alphabeticalFile.write(name)
        
    #open file, read
    alphabeticalFile = open('Alphabetical File.txt', 'r', encoding='utf-8')
    
    #record lines then sort by length
    alphabeticalFileLines = alphabeticalFile.readlines()
    alphabeticalFileLines.sort(key=len)
    
    #open file or create if doesn't exist, write
    sortedFile = open('Output.txt', 'w+', encoding='utf-8')
    
    #write sorted list to file
    for name in alphabeticalFileLines:
        sortedFile.write(name)
main()
