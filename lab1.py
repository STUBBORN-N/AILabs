# =====================================================================
# STEP 1: KNOWLEDGE BASE (KB)
# Declarative facts and decision rules representing university grading policy.
# =====================================================================

UNIVERSITY_KB = {
    "system_name": "BSCS Academic Performance & Grading Expert System",
    "passing_marks": 50,
    "rules": [
        {
            "id": "RULE_01",
            "conditions": {"attendance_percentage": 74},  # Below 75%
            "condition_type": "attendance_below",
            "grade": "F",
            "status": "Debarred",
            "action": "Ineligible to sit for final exam due to short attendance."
        },
        {
            "id": "RULE_02",
            "conditions": {"marks_min": 85, "marks_max": 100},
            "condition_type": "marks_range",
            "grade": "A",
            "status": "Passed with Distinction",
            "action": "Recommended for Merit Scholarship."
        },
        {
            "id": "RULE_03",
            "conditions": {"marks_min": 75, "marks_max": 84},
            "condition_type": "marks_range",
            "grade": "B",
            "status": "Passed",
            "action": "Good standing. Maintain momentum."
        },
        {
            "id": "RULE_04",
            "conditions": {"marks_min": 60, "marks_max": 74},
            "condition_type": "marks_range",
            "grade": "C",
            "status": "Passed",
            "action": "Satisfactory performance. Focus on weak subject areas."
        },
        {
            "id": "RULE_05",
            "conditions": {"marks_min": 50, "marks_max": 59},
            "condition_type": "marks_range",
            "grade": "D",
            "status": "Conditional Pass",
            "action": "Warning: Near failure threshold. Academic counseling advised."
        },
        {
            "id": "RULE_06",
            "conditions": {"marks_min": 0, "marks_max": 49},
            "condition_type": "marks_range",
            "grade": "F",
            "status": "Failed",
            "action": "Must repeat the course in the upcoming semester."
        },
        {
            "id": "RULE_07",
            "condition": {"cgpa" :3.70 },
            "disciplinary_warnings ": 0,
            "Status": "Graduated with Magna Cum Laude Honors",

        }
    ]
} 


print(f"Loaded: {UNIVERSITY_KB['system_name']}")


