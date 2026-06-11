# Patient Management System

# 1. Read data from file
def read_patients(filename):
    patients = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                pid, name, status = line.split(",")
                patients.append([pid, name, status])
    return patients


# 2. Display all patients
def display_all(patients):
    print("\nAll Patients:")
    for p in patients:
        print(",".join(p))


# 3. Display critical patients
def display_critical(patients):
    print("\nCritical Patients:")
    for p in patients:
        if p[2] == "Critical":
            print(p[1])


# 4. Count patients by status
def count_status(patients):
    normal = stable = critical = 0

    for p in patients:
        if p[2] == "Normal":
            normal += 1
        elif p[2] == "Stable":
            stable += 1
        elif p[2] == "Critical":
            critical += 1

    print("\nPatient Count:")
    print("Normal :", normal)
    print("Stable :", stable)
    print("Critical :", critical)


# 5. Search patient by ID
def search_patient(patients, pid):
    for p in patients:
        if p[0] == pid:
            print("\nPatient Found:")
            print(",".join(p))
            return
    print("\nPatient not found")


# 6. Save critical patients to file
def save_critical(patients, filename):
    with open(filename, "w") as file:
        for p in patients:
            if p[2] == "Critical":
                file.write(",".join(p) + "\n")

    print("\nCritical Patient Report Generated Successfully.")


# ---------------- MAIN PROGRAM ----------------

patients = read_patients("patients.txt")

display_all(patients)
display_critical(patients)
count_status(patients)

search_patient(patients, "P104")

save_critical(patients, "critical_patients.txt")