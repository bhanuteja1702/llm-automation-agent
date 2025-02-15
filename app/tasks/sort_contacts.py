import json

def sort_contacts(input_file: str, output_file: str):
    with open(input_file, "r") as infile:
        contacts = json.load(infile)
    
    sorted_contacts = sorted(contacts, key=lambda contact: (contact["last_name"], contact["first_name"]))
    
    with open(output_file, "w") as outfile:
        json.dump(sorted_contacts, outfile, indent=2)