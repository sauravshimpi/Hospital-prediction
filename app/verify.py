import re
import cv2

####################################    User Authentication Function   #####################################

def name_valid(name):
    if name.isalpha() and len(name) > 2:
        return True
    else:
        return False

def password_valid(pass1):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
    pat = re.compile(reg)
	
	# searching regex				
    mat = re.search(pat, pass1)
	
	# validating conditions
    if mat:
        return True
    else:
        return False

def password_check(password1, password2):
    if password1 == password2:
        return True
    else : 
        return False

def contact_valid(number):
    Pattern = re.fullmatch("[6-9][0-9]{9}",number)
    if Pattern != None:
        return True
    else:
        return False

def authentication(first_name, last_name, pass1, pass2):
    if name_valid(first_name) == False:
        return "Invalid First Name"           
    
    elif name_valid(last_name) == False:
            return "Invalid Last Name"
    
    elif password_valid(pass1) == False:
        return "Password Should be in Proper Format. (eg. Password@1234)"
    
    elif password_check(pass1, pass2) == False:
        return "Password Not Matched"
    
    else:
        return "success"

##################################    Patient Authentication Function   ##################################

def age_valid(age):
    if int(age) <= 120 and int(age) >= 0:
        return True
    else:
        return False

def contact_valid(number):
    Pattern = re.fullmatch("[6-9][0-9]{9}",str(number))
    if Pattern != None:
        return True
    else:
        return False


def form_varification(patient_first_name,patient_last_name,patient_contact,patient_age):
    if name_valid(patient_first_name) == False:
        return "Invalid First Name"           
    elif name_valid(patient_last_name) == False:
            return "Invalid Last Name"
    elif contact_valid(patient_contact) == False:
            return "Invalid Contact Number"
    elif age_valid(patient_age) == False:
            return "Invalid Age"
    else:
        return "Success"
