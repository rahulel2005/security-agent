import json
from triage import run_triage
from patcher import generate_patch
from reviewer import review_patch

def run_pipeline():
    print("🚀 Starting AI Security Agent...")

    try:
        with open("findings.json", "r", encoding="utf-8") as f:
            semgrep_output = json.load(f)
    except Exception as e:
        print("❌ Error reading findings.json:", e)
        return

    results = semgrep_output.get("results", [])

    print(f"🔍 Total findings: {len(results)}")

    if not results:
        print("✅ No vulnerabilities found.")
        return

    # Process first finding (for now)
    finding = results[0]

    print("\n📌 Processing finding:")
    print(json.dumps(finding, indent=2))

    # Step 1: Triage
    triage = run_triage(finding)
    print("\n🧠 Triage result:")
    print(triage)

    if not triage.get("auto_fix"):
        print("❌ Not eligible for auto-fix")
        return

    # Step 2: Generate patch
    patch = generate_patch(finding)
    print("\n🛠️ Patch generated:")
    print(patch)

    # Step 3: Review
    review = review_patch(finding, patch)
    print("\n🔍 Review result:")
    print(review)

    if not review.get("approved"):
        print("❌ Patch rejected")
        return

    print("\n✅ Patch approved and ready for PR 🚀")

if __name__ == "__main__":
    run_pipeline()