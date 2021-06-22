
#For the time being, code is  messy, will make it organized once I get the time.
import boto3
from boto3.dynamodb.conditions import Key
from boto3.utils import import_module
from services.s3Service import S3Service
import traceback
import csv

class DynamoService:

    def __init__(self):
        self.bucket = "upload-file-s3"
        self.s3_file_path = "incoming-files/"
        self.s3 =  boto3.client("s3")
    
    def createTableInstance(self, tableName):

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tableName)
        return table

    def getFileMetadataForUser(self, user_id):
        s3 =  boto3.client("s3")
        
        fileMetadataTable = self.createTableInstance(tableName='dl_file_metadata')
        print("Get File metadata")
        response = fileMetadataTable.query(
            KeyConditionExpression=Key('user_id').eq(user_id)
        )
        
        print("The type of response is ",type(response))
        with open('/tmp/sample.csv','w+',newline='') as f:
            theWriter = csv.writer(f)
            theWriter.writerow(['Name','PhoneNumber','City','State','Zip'])
            for dic in response['Items']:
                print("Each item is ",dic['file_id'])
                try:
                    print("The key is ",self.s3_file_path+dic['file_id'])
                    response_obj_from_s3 = self.s3.get_object(Bucket=self.bucket,Key=self.s3_file_path+dic['file_id'])
                    content_of_object = response_obj_from_s3['Body'].read().decode('utf-8').splitlines()
                    lines = csv.reader(content_of_object)
                    print("The lines of the csv are",lines)
                    headers = next(lines)
                    print('headers: %s' %(headers))
                    print("The type of lines is"),type(lines)
    
                    for line in lines:
                        print(line)
                        print(line[0],line[1], line[2])
                        theWriter.writerow([line[0],line[1],line[2]])
                        
                except: 
                    traceback.print_exc()
                    print("Error in getting file from S3") 
        s3.upload_file('/tmp/sample.csv',"upload-file-s3",dic['file_id']+"sample.csv")
                
            

        return response['Items']