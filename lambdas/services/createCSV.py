import csv
import boto3
class CreateCSV:

    def create_csv(self):
        s3 = boto3.client("s3")
        with open('/tmp/sample.csv','w',newline='') as f:
            theWriter = csv.writer(f)
            theWriter.writerow(['Col1','Col2','Col3'])
            for i in range(1,100):
                theWriter.writerow(['one','two','three'])
        s3.upload_file('/tmp/sample.csv',"upload-file-s3","sample.csv")
        
        
        
                