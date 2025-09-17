from school_name import claim_unreserved_code_school_name

def test_invalid_name_no_pytest():
    
    # Implement the equivalent of this test logic but DO NOT import or otherwise access pytest:
    try:
        result = claim_unreserved_code_school_name("Ada Developers Academy")
    except ValueError as error:
        print(f"{error}")