import boto3
import requests
import datetime

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])

def main():
    start = datetime.datetime.now()
    res = requests.get('URL.jpg', timeout=15)
    filename = <imagename>

    with open(filename, "wb") as f:
        f.write(res.content)

    photo=filename
    print(type(photo))

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))
    end = datetime.datetime.now()
    print(end - start)

if __name__ == "__main__":
    main()
