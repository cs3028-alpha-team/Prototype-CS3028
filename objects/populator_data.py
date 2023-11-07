from faker import Faker
import random
fake = Faker()
suffixes = [ "Internship", "Placement", "Opportunity" ]
medical_jobs = [ "Registered Nurse", "Physician", "Medical Laboratory Technician", "Pharmacist", "Medical Assistant", "Surgeon", "Radiologic Technologist", "Physical Therapist", "Dental Hygienist", "Emergency Medical Technician (EMT)" ]

populator_data = {
    "student_data" : {
        "fullname" : [ fake.name() for _ in range(100) ],
        "degree" : [ "Doctor of Medicine (M.D.)", "Doctor of Osteopathic Medicine (D.O.)", "Doctor of Dental Medicine (D.M.D.)", "Doctor of Dental Surgery (D.D.S.)", "Doctor of Veterinary Medicine (D.V.M.)", "Doctor of Pharmacy (Pharm.D.)", "Doctor of Nursing Practice (D.N.P.)", "Doctor of Physical Therapy (D.P.T.)", "Doctor of Optometry (O.D.)", "Doctor of Podiatric Medicine (D.P.M.)", "Doctor of Chiropractic (D.C.)", "Master of Public Health (M.P.H.)", "Master of Health Administration (M.H.A.)", "Bachelor of Science in Nursing (B.S.N.)", "Bachelor of Science in Biomedical Science (B.S.)" ],
        "experience" : [ "surgery", "dentistry", "nursing", "nutrition", "physiotherapy", "immunology" ]
    },
    "internship_data" : {
        "title" : [ f"{position} {random.choice(suffixes)}" for position in medical_jobs ], 
        "company" : [ "MediCare Innovations", "HealthPro Solutions", "LifeScience Labs", "MediTech Systems", "BioHealth Therapeutics", "MediNet Pharmaceuticals", "HealthCare Dynamics", "BioTech Innovators", "PharmaLink Solutions", "MediConnect Services" ], 
        "field" : [ "surgery", "dentistry", "nursing", "nutrition", "physiotherapy", "immunology" ]
    }
}