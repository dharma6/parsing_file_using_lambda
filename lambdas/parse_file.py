import json
import sys
from services.dynamoService import DynamoService
from services.createCSV import CreateCSV
def parse_file_handler(event, context):
    
    try:
        event_content = json.dumps(event)
        event_dictionary = json.loads(event_content)

        #get the user id from the event
        user_id = event_dictionary['user_id']
        print(user_id)
        # Call the write file metadata 
        dbService = DynamoService()
        create_csv_file=CreateCSV()

        # delete the file meta data for the passed file_id and user_id and send the response back to the calling functionality
        # response will have all the file metadata information for that user
        response = dbService.getFileMetadataForUser(user_id)
        #create_csv_file.create_csv()

        return {
            "statusCode": 200,
            "body": response
        }
        
    except:
        print(sys.exc_info())
        return {
            "message": json.dumps("Error occured while deleting data from the table")
        }
    