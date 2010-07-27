import csv # to parse alexa's list
from pyw3 import validator


class markup_check_for_alexa():
    def __init__(self):
        self.valid_count = 0
        self.invalid_count = 0
        self.aborted_count = 0
        
        self.validator = validator()

        self.alexa_csv = csv.reader(open('top-1m.csv'), delimiter=',')

    def check_each_site(self):
        for row in self.alexa_csv:
            uri = row[1].strip()
            try:
                validation_result = self.validator.check_URI(uri)
                if validation_result["status_code"] == 0:
                    self.invalid_count = self.invalid_count + 1
                elif validation_result["status_code"] == 1:
                    self.valid_count = self.valid_count + 1

                print validation_result["status_code"],"| Markup for '"+uri+"' is ", validation_result["status_text"].upper()

            except Exception,error:
                print "- | Markup for '"+uri+" is not checkable, aborted"
                self.aborted_count = self.aborted_count + 1

    def print_results(self):
        print " ------ Total results ------ "
        print "Total web sites checked = ", (self.invalid_count + self.valid_count + self.aborted_count)
        print "Valid web sites = " , self.valid_count
        print "Invalid web sites = " , self.invalid_count
        print "Aborted web sites = " , self.aborted_count       
        

markup_checker = markup_check_for_alexa()
markup_checker.check_each_site()
