
# Script to download files from 'url.txt' file which contains links to the data needed to be downloaded
import requests
counter = 1
with open('url.txt') as my_file:
    # go through each line in the 'url.txt' file to go through each url 
    for line in my_file:
        # remove any spaces and trailing new line characters from the link
        URL = line.strip()
        # choose the desired name of the file that will have the downloaded content from the url
        FILENAME = str(counter) + '.nc4'
        counter+= 1
        # use request library to get contents of the url
        result = requests.get(URL)
        try:
            result.raise_for_status()
            # open the the new empty file
            f = open(FILENAME,'wb')
            # copy the contents downloaded from the url and write it in the new file
            f.write(result.content)
            # close file
            f.close()
            print('contents of URL written to '+FILENAME)
        except:
            print('requests.get() returned an error code '+str(result.status_code))
