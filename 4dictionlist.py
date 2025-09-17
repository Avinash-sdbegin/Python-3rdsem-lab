# Task 4: Nested Dictionary + Search Assistant Professor

# Nested dictionary for IIIT Ranchi's organizational structure (sample)
iiit_structure = {
    "Administration": {
        "Director": "Prof. Rajeev Srivastava",
        "Registrar": "Registrar (In-Charge)"
    },

    "Computer Science & Engineering": {
        "HoD": "Dr. Kirti Kumari",
        "Faculty": {
            "Professors": ["Prof. Rajeev Srivastava"],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Dhananjoy Bhakta",
                "Dr. Jayadeep Pati",
                "Dr. Roshan Singh",
                "Dr. Rashmi Panda",
                "Dr. Bharat Singh",
                "Dr. Priyank Khare",
                "Dr. Kirti Kumari",
                "Dr. Tarun Biswas",
                "Dr. Ranjan Kumar Behera",
                "Dr. Gaurav Sundaram",
                "Dr. Akash Srivastava"
            ]
        }
    },

    "Electronics & Communication Engineering": {
        "HoD": "Dr. Santosh Kumar Mahto",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Santosh Kumar Mahto",
                "Dr. Shashi Kant Sharma",
                "Dr. Jitendra Kumar Mishra",
                "Dr. Rajiv Kumar",
                "Dr. Priyabrat Garanayak",
                "Dr. Nishit Malviya"
            ]
        }
    },

    "Sciences": {
        "HoD": "Dr. Sandhir Kumar Singh",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Sandhir Kumar Singh",
                "Dr. Puja Ghosh",
                "Dr. Rohit Kandulna",
                "Dr. Rishikesh Dutta Tiwary",
                "Dr. Shashi Kant"   # (Mathematics)
            ]
        }
    },

    "Humanities & Management": {
        "HoD": "Dr. Sandhir Kumar Singh",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Noopur"
            ]
        }
    }
}


def find_professor_department(structure, name):
    """
    Search for an Assistant Professor in the nested dictionary.
    Return the department if found, else None.
    """
    for dept, info in structure.items():
        faculty = info.get("Faculty", {})
        aps = faculty.get("Assistant Professors", [])
        if name in aps:
            return dept
    return None


# Main program
def main():
    name = input("Enter the name of an Assistant Professor: ").strip()
    dept = find_professor_department(iiit_structure, name)

    if dept:
        print(f"✅ {name} belongs to the Department of {dept}.")
    else:
        print(f"❌ Assistant Professor named '{name}' was not found in IIIT Ranchi's structure.")


if __name__ == "__main__":
    main()
