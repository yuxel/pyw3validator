# Python W3 validator

A Python wrapper for [W3 validator services API](http://validator.w3.org/docs/api.html)

# Howto Use

Install module pyw3 by
    python setup.py install

Then you can use such a code
    import pyw3
    validator = pyw3.validator() 
    try:
        results = validator.check_URI("http://yuxel.net")
        print results
    except Exception,error:
        print "Markup cannot be checked, aborted"

Check example code on examples dir

# Return values 
    {"status_text", // text of status Valid, Invalid, Aborted
     "status_code", // 0 = Invalid, 1 = Valid, -1 = Aborted
     "errors",  // num of errors found on document
     "warnings", // num of warnings found on document
     "recursion" // generally 1 check API doc for details
    }


Note: Will raise an exception if url is not checkable because of a fatal error (decoding, 404 not found, etc)
