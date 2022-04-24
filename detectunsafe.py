import boto3
import os
import os.path
from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data

def main():
    client=boto3.client('rekognition')

    rootdir ="/home/output"
    data = OrderedDict()
    sheet_1 = []
    row_1_data = [u"filename", u"lable", u"confidence", u"ParentName"]
    sheet_1.append(row_1_data)

    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            photo=os.path.join(parent,filename)

            with open(photo, 'rb') as image:
                response = client.detect_moderation_labels(Image={'Bytes': image.read()})
                print (response['ModerationLabels'])

            print('Detected labels in ' + photo)
            for label in response['ModerationLabels']:
                print (label['Name'] + ' : ' + str(label['Confidence']))
                print (label['ParentName'])

                row_2_data = [photo,label['Name'], str(label['Confidence']),label['ParentName']]
                sheet_1.append(row_2_data)
                data.update({u"Summary": sheet_1})
                save_data("detectunsafe.xls", data)

if __name__ == "__main__":
    main()
