import cv2
import pandas
 
csvFile = pandas.read_csv('test.csv')

# print(csvFile['Name'])
list_names = csvFile['Name']
# 425,655
for index, name in enumerate(list_names):
    template = cv2.imread('temp.jpg')
    cv2.putText(template, name, (441,699), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0),1,cv2.LINE_AA)
    cv2.imwrite(f'E:\MARWADI UNIVERSITY\CP CLUB DATA\Certificate Generator\Folder\{name}.jpg',template)
    print('Processing Certificate {}/{}'.format(index+1, len(list_names)))