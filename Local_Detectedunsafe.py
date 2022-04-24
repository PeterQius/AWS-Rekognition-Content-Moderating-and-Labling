import boto3
import datetime

def moderate_image(photo, bucket):

    client=boto3.client('rekognition')
    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])

def main():
    start = datetime.datetime.now()
    photo = <fimename>
    bucket = <bucketname>
    label_count = moderate_image(photo, bucket)
    print("Labels detected: " + str(label_count))
    end = datetime.datetime.now()
    print(end - start)

if __name__ == "__main__":
    main()
