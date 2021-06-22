import csv
class CsvWriter:
    def __init__(self):
        with open('sample.csv','w',newline='') as f:
            theWriter = csv.writer(f)
            theWriter.writerow(['Col1','Col2','Col3'])
            for i in range(1,100):
                theWriter.writerow(['one','two','three'])
                