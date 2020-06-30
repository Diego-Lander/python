# Progrsm: Porgram 4
# Programmer: Diego Lander
# Date : May 15, 2020
# Version 1.0

#CONSTANTS 
IN_STATE_CREDIT_HOUR = 166.00
IN_STATE_FLAT_RATE = 1992.00
IN_STATE_PT_SERVICE_FEE = 160.00
IN_STATE_FT_SERVICE_FEE = 246.00
OUT_STATE_CREDIT_HOUR = 498.00
OUT_STATE_FLAT_RATE = 5976.00
OUT_STATE_PT_SERVICE_FEE = 480.00
OUT_STATE_FT_SERVICE_FEE = 738.00
OVERLOAD_FEE = 100.00
ACTIVITY_FEE = 20.00
MIN = 0
CREDIT_MAX = 18
MAT_FEE_MAX = 999.99
FIN_AID_MAX = 1000.00
SENTINEL = 00000000

#defining main()===========================================================
def main():
    
    semester = input('Enter current semester (Fall, Winter, Spring, Summer): ')
    
    year = input('Enter the current year: ')
    
    banner_id = int(input('Enter Banner ID, 00000000 to stop: '))
#Sentinel loop==========================================
    while banner_id != SENTINEL:
    
#get student info==========================================
        first_name, last_name = get_name()
        street, city, state_code, zip_code = get_address()
        #get credit hours, materials fee, grants and acholarship
        credit_hours = get_credit_hours()
        mat_fee = get_mat_fee()
        grants = get_grant()
        scholarship = get_scholarship()
#Financial Aid calcultations===========================
        fin_aid = grants + scholarship

#Flag set up=============================
        overload, in_state, part_time = set_flags(credit_hours, state_code)
#find base tuition, student status, and service fee===========================================
        student_status, base_tuition, service_fee = find_base_tuition(credit_hours, in_state,
part_time)
#find total fees===================================================
        fees = find_fees(mat_fee, service_fee, overload)
#Calculate total tuition===========================================
        total_tuition = base_tuition + fees - fin_aid
#Displaying Invoice==================================
        display_header(semester, year)
        display_std_info(banner_id, first_name, last_name, street, city, state_code, zip_code,)
        display_status(student_status, base_tuition)
        display_fees(mat_fee, service_fee, fees, overload)
        display_fin_aid(grants, scholarship)
        display_tuition(total_tuition)
    #get next banner id========================
        banner_ID = input('Enter banner ID, 00000000 to stop: ')

#def get_name=========================
def get_name():
    first_name = input('Enter students first name: ')
    last_name = input('Enter students last name; ')
    return (first_name, last_name)
#Get_address()====================================
def get_address():
    #get address info
    street = input('Enter street: ')
    city = input('Enter city: ')
    state_code = input('Enter state code: ')
    zip_code = input('Enter zip code: ')
    return (street, city, state_code, zip_code)
#Get_credit_hours()==========================================
def get_credit_hours():
    good_data = False
    while not good_data:
        credit_hours = int(input('Enter number of credit hours (1 to 18): '))
        good_data = MIN <= credit_hours <= CREDIT_MAX
        if not good_data:
            print('Credit hours out of range')
    return (credit_hours)
#===get_mat_fee()=======================================
def get_mat_fee():
    good_data = False
    while not good_data:
        mat_fee = int(input('Enter Material Value (0 to 999.99): '))
        good_data = MIN < mat_fee <= MAT_FEE_MAX
    if not good_data:
        print('Materials fee invalid – processing stopped')

    return (mat_fee)
#===get_grant()==============================================
def get_grant():
    good_data = False
    while not good_data:
        grants = int(input('Enter amount of student grants (0 to 1000): '))
        good_data = MIN <= grants <= FIN_AID_MAX
    if not good_data:
        print('Amount of grants invalid – processing stopped')

    return(grants)

#get_scholarship=======================================
def get_scholarship():
    good_data = False
    while not good_data:
        scholarship = int(input('Enter the amount of scholarships(0 to 1000); '))
        good_data = MIN <= scholarship <= FIN_AID_MAX
    if not good_data:
            print('Amount of scholarships invalid – processing stopped')

    return(scholarship)
            
#=====set flags====================================
def set_flags(credit_hours, state_code):
    overload = False
    in_state = False
    part_time = False
    if credit_hours > 16:
        overload = True
    if state_code.upper() == "CT":
        in_state = True
    if credit_hours < 16:
        part_time = True
    return (overload, in_state, part_time)
#===================================================
def find_base_tuition(credit_hours, in_state, part_time):
    if in_state:
        if part_time:
            return ("In-State , Part-time", credit_hours * IN_STATE_CREDIT_HOUR, IN_STATE_PT_SERVICE_FEE)
        else:
            return ("In-State , Full-time", credit_hours * IN_STATE_CREDIT_HOUR, IN_STATE_FT_SERVICE_FEE)
    else:
        if part_time:
            return ('Out-of-State, Part-Time', credit_hours * OUT_STATE_CREDIT_HOUR, OUT_STATE_PT_SERVICE_FEE)
        else:
            return ('Out-of-State, Full-Time', OUT_STATE_FLAT_RATE, OUT_STATE_FT_SERVICE_FEE)
def find_fees(mat_fee, service_fee, overload):
    if overload:
        return (mat_fee + service_fee + ACTIVITY_FEE + OVERLOAD_FEE)
    else:
        return mat_fee + service_fee + ACTIVITY_FEE
#Header display=============================================
def display_header(semester, year):
    print('===============================================')
    print('          Gateway Community College            ')
    print('              Tuition Invoice                  ')
    print(            semester, 'Semester', year           )
#displaying student info====================================
def display_std_info(banner_id, first_name, last_name, street, city, state_code, zip_code):
    print('Student Banner ID:', banner_id                  )  
    print(first_name, last_name                            )   
    print(city, state_code, zip_code                            )
#Displaying status===========================================
def display_status(student_status, base_tuition):
    print('===============================================')
    print()
    print('Student Status: '        ,student_status        )
    print()
    print('Tuition: '            '$', base_tuition         )
    print()
#Displaying fees============================================
def display_fees(mat_fee, service_fee, fees, overload):
    print('Fees: '                                         )
    print('College Service Fee'  '$', fees                 )
    print('Materials Fee'        '$', mat_fee              )
    print('Student Activity Fee' '$', ACTIVITY_FEE         )
    if overload:
        print('“Overload Fee $ ', OVERLOAD_FEE        )
    print('===============================================')
    print('Total Fees: '         '$', fees                 )
#Displaying fin_aid==========================================
def display_fin_aid(grants, scholarship):
    print('Grants: '             '$', grants               )
    print('Scholarships: '       '$', scholarship          )
#Displaying tuition===========================================
def display_tuition(total_tuition):
    print('Total Tuition Due: '  '$', total_tuition        )
        
main()
    

    



