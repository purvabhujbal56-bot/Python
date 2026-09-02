def diagnose_flu():
    fever = input("Do you have fever? (yes/no): ")
    cough = input("Do you have cough? (yes/no): ")
    throat = input("Do you have sore throat? (yes/no): ")

    if fever.lower() == "yes" and cough.lower() == "yes" and throat.lower() == "yes":
        print("\nDiagnosis: You may have Flu.")
    else:
        print("\nDiagnosis: Flu not detected.")

diagnose_flu()