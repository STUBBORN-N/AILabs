# =====================================================================
# STEP 2: INFERENCE ENGINE
# Evaluates student records against rules stored in the Knowledge Base.
# =====================================================================

def evaluate_student(student_record, kb):
    """
    Evaluates student marks and attendance against university rules.
    Returns computed grade, academic status, and recommended action.
    """
    print(f"\n--- EVALUATING STUDENT: {student_record['student_name']} (ID: {student_record['student_id']}) ---")
    
    # Check rule 1: Attendance constraint first
    if student_record["attendance"] < 75:
        attendance_rule = next(r for r in kb["rules"] if r["condition_type"] == "attendance_below")
        return {
            "rule_id": attendance_rule["id"],
            "grade": attendance_rule["grade"],
            "status": attendance_rule["status"],
            "action": attendance_rule["action"]
        }
    
    # Check grade spectrum rules
    marks = student_record["total_marks"]
    for rule in kb["rules"]:
        if rule["condition_type"] == "marks_range":
            print(f"Evaluating Rule {rule['id']}: {rule['conditions']['marks_min']} <= {marks} <= {rule['conditions']['marks_max']}")
            if rule["conditions"]["marks_min"] <= marks <= rule["conditions"]["marks_max"]:
                return {
                    "rule_id": rule["id"],
                    "grade": rule["grade"],
                    "status": rule["status"],
                    "action": rule["action"]
                }
                
    return {
        "rule_id": "UNKNOWN",
        "grade": "N/A",
        "status": "Invalid Score Entry",
        "action": "Verify submitted marks with the exam department."
    }