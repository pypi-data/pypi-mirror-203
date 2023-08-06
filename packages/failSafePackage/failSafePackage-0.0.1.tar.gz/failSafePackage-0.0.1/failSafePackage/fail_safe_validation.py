import numpy as np
import re

class fail_safe_cls():

    def __init__(self):
        pass

    def fail_safe_validation_function(product_charge):
        '''
        doc_string:
        param product_charge: str,float,int >return type:float

        This function is made for fail-safe validation of product_charge from product metrics
        and room_revenue of location metrics.
        function takes only 1 arg for which the fail-safe condtion is applied.
        the data type of the argument can string, int and float.
        the return value is in the form of float only.
        '''
        try:
            product_charge = str(product_charge)
            # replace any string with blank except 0-9,hyphon and dot. Ex USD12!@00 => 1200
            response = re.sub(r"[^0-9-\.]", '', product_charge)
            # replace more than one dot(from left to right) with blank, except the rightmost dot. Ex 12.34.43 => 1234.43
            response1 = re.sub(r'\.(?![^.]*$)', '', response)
            # replace more than one hyphen with blank, except the starting Hyphen. Ex -123-2 => -1232
            response2 = (lambda x: "".join([x[0], x[1:].replace("-", "")]) if (
                    len(x) > 1 and bool(re.search(r'\d', x))) else x.replace(".", '').replace("-", ''))(response1)
            # round to 2 decimal
            output = round(float(response2), 2)
            return output
        except:
            return np.nan