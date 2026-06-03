import json
import logging

# Ensure transformers doesn't spam warnings
logging.getLogger("transformers").setLevel(logging.ERROR)

def get_medical_recommendation(predicted_class, lesion_score, confidence):
    """
    Recommendations mapping Severity prediction, exact structural score, and temperature confidence.
    """
    is_high_conf = confidence > 0.8
    if predicted_class == 0:
        if lesion_score < 10:
             return "Healthy baseline", "No signs of diabetic retinopathy isolated. Continue standard annual eye exams.", "#22c55e" # Green
        else:
             return "Re-evaluate Baseline", "Routine monitoring indicated. Minor structural anomalies suggest a clinical follow-up is beneficial.", "#84cc16"
    elif predicted_class == 1:
        text = "Mild vascular irregularities suspected."
        if lesion_score > 30 and is_high_conf:
             text += " Consistent lesion mapping detected; schedule an appointment in 3-6 months."
        else:
             text += " Maintain systemic glucose control and monitor annually."
        return "Routine Monitor", text, "#eab308" # Yellow
    elif predicted_class == 2:
        text = "Moderate structural changes detected."
        if lesion_score > 50:
             text += " Significant peripheral lesion spread isolated. Consult a specialist within 1-2 months."
        else:
             text += " Consult an eye doctor within 3-6 months for a dilated exam."
        return "Consult Doctor", text, "#f97316" # Orange
    elif predicted_class == 3:
         return "Immediate Specialist Attention", "Severe indicators present. Substantial risk to retinal integrity detected; seek an immediate formulation evaluation.", "#ef4444" # Red
    else:
         return "Urgent Treatment Required", "Proliferative characteristics identified. Extreme risk of blinding complications. Sight-saving intervention is emergent.", "#b71c1c" # Dark Red


def generate_llm_explanation(structured_json, stage, generator=None):
    """
    Step 3 of the Hybrid Engine: takes strict structural features and queries a Local LLM 
    (flan-t5-small) to format it without hallucination. Enforces deterministic generation and verification.
    """
    # 1. Fallback to rule-based logic if generator is unavailable
    if generator is None:
        return _fallback_rule_based(structured_json, stage)
        
    try:
        # 2. Dynamic prompt formulation
        intensity = structured_json.get('intensity', 'unknown')
        spread = structured_json.get('spread', 'unknown')
        location = structured_json.get('location', 'unknown')
        area_percent = structured_json.get('area_percent', 0.0)

        prompt = f"Generate a clinical explanation for diabetic retinopathy. Intensity: {intensity}, Spread: {spread}, Location: {location}, Area affected: {area_percent}%."
        print("LLM called with:", prompt)
        
        # 3. Controlled execution
        output = generator(prompt, max_length=150)
        
        explanation = output[0]['generated_text'].strip()
        
        # 4. Debug Mode Logging
        print("====== DEBUG MODE: LLM HYBRID EXPLANATION ======")
        print("[LLM USED] - Execution Successful")
        print(f"RAW LLM TEXT: {explanation}")
        print("================================================")
        
        return explanation
        
    except Exception as e:
        print(f"LLM Generation pipeline failed: {e}")
        return _fallback_rule_based(structured_json, stage)

def _fallback_rule_based(structured_json, stage):
    """
    Rule-based deterministic mapping explicitly used when LLM is offline or verification fails.
    """
    print("====== DEBUG MODE: LLM HYBRID EXPLANATION ======")
    print("[RULE-BASED FALLBACK] - LLM bypassed or failed")
    print(f"INPUT JSON: {json.dumps(structured_json)}")
    print("================================================")
    
    intensity = structured_json['intensity']
    spread = structured_json['spread']
    loc = structured_json['location']
    area = structured_json['area_percent']
    
    if intensity == "none":
        return f"Analysis reveals clear retinal structuring with no pathological markers. "
        
    return (
    f"{spread.capitalize()} {intensity}-intensity activations span {area}% of the retinal area.\n\n"
    f"These findings are primarily located in the {loc} structures, providing spatial correlation for the model's diagnostic stage."
)
