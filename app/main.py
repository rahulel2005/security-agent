import json
from triage import run_triage
from patcher import generate_patch
from reviewer import review_patch

def run_pipeline(finding):
    triage = run_triage(finding)

    if not triage["auto_fix"]:
        print("❌ Not eligible for auto-fix")
        return

    patch = generate_patch(finding)

    review = review_patch(finding, patch)

    if not review["approved"]:
        print("❌ Patch rejected")
        return

    print("✅ Patch ready")
    print(patch["patch"])