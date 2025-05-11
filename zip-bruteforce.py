from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extraction(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except: 
        return False
        
def main():
    print("Bruteforcing... ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'r') as f:
            # Iterate through password entries in rockyou.txt 
            for p in f: 
                # Attempt to extract the zip file using each password
                if attempt_extraction(zf, p):
                    # Handle successful and unsuccessful attempts
                    print("Password has been found")
                    return p
                    exit(0)
            print("Password not found in file")

if __name__ == "__main__":
    main()
