#!/usr/bin/python
# Filename: pyw3validator.py
# A Simple module to check whether a web sites markup is valid or not
# Uses http://validator.w3.org/docs/api.html

import urllib

class pyw3validator():

    # set default validator url
    def __init__(self):
        self.validator_url = "http://validator.w3.org/check?uri=%s" 

    # validator can be on localhost or another web site
    def set_validator_url(self, new_url):
        self.validator_url = new_url

    # check if given uri is valida
    def check_URI(self,uri):
        #self.validator_url = "http://validator.w3.org/check?uri=%s"
        uri = urllib.quote(uri)

        response = urllib.urlopen(self.validator_url % uri);
        info = response.info()
        response.close()

        status_text    = info["x-w3c-validator-status"] # valid, invalid, abort
        recursion = info["X-W3C-Validator-Recursion"]
        status_code = self.get_status_code(status_text)

        if status_text == "Abort":
            # will raise an error if URL is not valid or website not exists
            raise Exception("URL not valid")
        else:
            errors   = int(info["X-W3C-Validator-Errors"])
            warnings = int(info["X-W3C-Validator-Warnings"])

            return {"status_text": status_text,
                    "status_code" : status_code,
                    "errors": errors,
                    "warnings" : warnings,
                    "recursion" : recursion
            }


    # returns status_code from status_text
    def get_status_code(self, status_text):
        if status_text == "Valid":
            status_code = 1
        elif status_text == "Invalid":
            status_code = 0
        else:
            status_code = -1

        return status_code

# test
if __name__ == "__main__":    
    validator = pyw3validator()
    #validator.set_validator_url("http://validator.w3.org/docs/api.html")
    try:
        status = validator.check_URI("yuxel.net")
        print status
    except Exception,error:
        print error

