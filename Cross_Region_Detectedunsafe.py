import boto3
import datetime

def moderate_image(targetkey, targetbucket):

    client=boto3.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':targetbucket,'Name':targetkey}})

    print('Detected labels for ' + targetkey)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])

def main():
    start = datetime.datetime.now()
    sourcebucket = <sourcebucket>
    sourcekey = <sourcekey>
    targetbucket= <targetbucket>
    targetkey = sourcekey

    s3=boto3.resource('s3')

    copy_source = {
        'Bucket': sourcebucket,
        'Key': sourcekey
    }
    s3.meta.client.copy(copy_source, targetbucket, targetkey)

    label_count=moderate_image(targetkey, targetbucket)
    print("Labels detected: " + str(label_count))
    end = datetime.datetime.now()
    print(end - start)

if __name__ == "__main__":
    main()
