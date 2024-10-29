import json

document_sections = [
    {
    "id": "Case_1",
    "title": "Cardiac_surgery_conference",
    "content": "DOB: Age: 11 days; Hosp Type: Inpatient (CICU)"
},
{
    "id": "Case_1_History",
    "title": "History",
    "content": "An 11-day-old female, born at 38 weeks gestation via uncomplicated NSVD, with a brief NICU stay for hypoglycemia in the setting of LGA. She had been at home feeding well until the past 2 hours when she was noted to have gasping and color change in the face with feeds. Started becoming tired and taking less formula in the past 24 hours. No decrease in wet diapers, no other color change outside of feeds. No noted tachypnea, respiratory distress, sweating, or syncope. CXR showed cardiomegaly; EKG showed RVH. Echo in NICU demonstrated long segment coarctation, borderline small left-sided structures, and severely decreased biventricular function. Started on PGE and transferred to CICU."
},
{
    "id": "Case_1_Prior_Procedure",
    "title": "Prior_Procedure",
    "content": "None"
},
{
    "id": "Case_1_Other_Diagnoses",
    "title": "Other_Diagnoses",
    "content": "None"
},
{
    "id": "Case_1_Medications",
    "title": "Meds",
    "content": "PGE @ 0.05 mcg/kg/min, ampicillin, ceftazidime"
},
{
    "id": "Case_1_Allergies",
    "title": "Allergies",
    "content": "NKDA"
},
{
    "id": "Case_1_Vitals",
    "title": "Vitals",
    "content": "Weight: 4.5 kg (97th percentile); Height: 56 cm (99th percentile)"
},
{
    "id": "Case_1_Physical_Exam",
    "title": "Exam",
    "content": "General: alert and crying; HEENT: no conjunctival injection; Resp: LCTA b/l, no wheeze, mild WOB, no crackles; CV: normal S1 S2, no murmur, non-displaced PMI, normal coloration of extremities, femoral pulses 1+ bilaterally; Abd: soft, non-distended, no hepatomegaly; MSK: no peripheral edema; Skin: no rash, warm and well-perfused, no cyanosis; Neuro: alert, no focal deficits"
},
{
    "id": "Case_1_EKG",
    "title": "EKG",
    "content": "Date: 1/9/23; Normal sinus rhythm; Right atrial enlargement; Biventricular hypertrophy; Nonspecific ST and T wave abnormality"
},
{
    "id": "Case_1_Echo",
    "title": "Echo_Data",
    "content": "Study Date: 1/8/23; Findings before Alprostadil; Borderline small mitral valve annulus; Mildly hypoplastic left ventricle; Borderline aortic valve, bicuspid; Long segment coarctation of the aorta; Patent ductus arteriosus, small and restrictive, right to left shunt; Severely decreased biventricular function; Small secundum atrial septal defect, left to right shunt; Mildly dilated right ventricle; Mild tricuspid valve regurgitation; Trivial mitral valve regurgitation"
},
{
    "id": "Case_1_Cath_Data",
    "title": "Cath_data",
    "content": "None"
},
{
    "id": "Case_1_CT_MRI_Data",
    "title": "CT_MRI_data",
    "content": "None"
},
{
    "id": "Case_1_Pending_Tests",
    "title": "Pending_Tests",
    "content": "None"
},
{
    "id": "Case_1_Access_Issues",
    "title": "Access_Issues",
    "content": "None"
},
{
    "id": "Case_1_Non_Cardiac_Abnormalities",
    "title": "Non_Cardiac_Abnormalities",
    "content": "None"
},
{
    "id": "Case_1_PreOp_Risk_Factors",
    "title": "PreOp_Risk_Factors",
    "content": "None"
},
{
    "id": "Case_1_Echo_BSA",
    "title": "Echo",
    "content": "BSA(Haycock): 0.27 m2; Clinical History: Long segment CoA, borderline small left-sided structures, bicuspid aortic valve; Requested Information: Assess isthmus, PDA size, function, left-sided size"
},
{
    "id": "Case_1_Echo_Summary",
    "title": "Interpretation_Summary",
    "content": "Coarctation of aorta, juxtaductal; Elongated distal arch; Bicommissural aortic valve, right/left fusion, thickened leaflets; Borderline mitral valve annulus, shortened chordae; Normal left ventricle structure and size; Small PDA, narrowing to 2.5 mm at aortic end; Mild to moderate peak descending aorta gradient, peak velocity 3 m/s; Normal aortic and mitral valve velocity; Mild mitral valve insufficiency; Patent foramen ovale, small left to right shunt"
},
{
    "id": "Case_1_Attestation",
    "title": "Attending_Attestation",
    "content": "Attending saw, examined, and evaluated the patient. Verified and agreed with the findings and care plan."
},
{
    "id": "Case_1_Problem_List",
    "title": "Problem_List_Past_Medical_History",
    "content": "Ongoing: No qualifying data; Historical: No qualifying data; Birth History: Full term, NSVD; Brief NICU stay for hypoglycemia in setting of LGA"
},
{
    "id": "Case_1_Lab_Results",
    "title": "Lab_Results",
    "content": "WBC Count: 10.16 K/mcL; Hemoglobin: 16.9 gm/dL; Hematocrit: 49.2 %; Platelet Count: 454 K/mcL; MCV: 107.4 fL; RDW: 15.9 %; Sodium: 140 mmol/L; Potassium: 4.8 mmol/L; Chloride: 104 mmol/L; CO2: 24 mmol/L; Anion Gap: 17 mmol/L; BUN: 10 mg/dL; Creatinine: 0.27 mg/dL; Glucose: 134 mg/dL; Calcium: 10 mg/dL; Magnesium: 2.1 mg/dL; Phosphorus: 5.8 mg/dL; Total Protein: 5.3 gm/dL; Albumin: 3 gm/dL; Bilirubin, Total: 3.1 mg/dL; AST: 116 unit/L; ALT: 203 unit/L; ALK: 177 unit/L"
},
{
    "id": "Case_1_ECG",
    "title": "ECG",
    "content": "Study Date/Time: 01/09/2023 03:51; Vent. Rate: 164 BPM; Atrial Rate: 164 BPM; P-R Int: 112 ms; QRS Dur: 066 ms; QT Int: 275 ms; QTc Int: 455 ms; Normal sinus rhythm; Right atrial enlargement; Biventricular hypertrophy; Nonspecific ST and T wave abnormality"
}
]

with open('patient_data.jsonl', 'w') as f:
    for idx, section in enumerate(document_sections):
        # Construct each JSON object
        json_obj = {
            "id": f"sample_patient_data_{idx + 1}",  # Unique ID for each section
            "title": section["title"],
            "content": section["content"]
        }
        # Write JSON object to file as a line
        f.write(json.dumps(json_obj) + "\n")

print("Data has been written to patient_data.jsonl in JSONL format.")
