"""
Streamlined Real Benchmark Dataset Ingestion.
Fetches exactly 2 gold-standard, widely recognized academic datasets:
1. StrategyQA (Segal et al. / Stanford & TAU) - Strategic Multi-Agent Decision Making
2. MMLU Professional Law (cais/mmlu / Hendrycks et al.) - High-Stakes Legal Precedent

Zero API keys required. Uses Python standard library (urllib and json).
"""

import os
import json
import urllib.request

OUTPUT_DIR = "data/real_benchmarks"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "real_decision_benchmarks.jsonl")

def fetch_strategyqa(limit: int = 100):
    url = "https://raw.githubusercontent.com/eladsegal/strategyqa/master/data/strategyqa/dev.json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    print(f"[1/2] Fetching StrategyQA ({limit} questions)...")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            episodes = []
            for idx, item in enumerate(data[:limit]):
                episodes.append({
                    "task_id": f"STRATEGYQA_{idx+1:03d}",
                    "benchmark": "StrategyQA",
                    "domain": "Strategic_Reasoning",
                    "question": item.get("question", ""),
                    "ground_truth": "Yes" if item.get("answer") is True else "No",
                    "source": "https://github.com/eladsegal/strategyqa"
                })
            print(f"      -> Ingested {len(episodes)} StrategyQA decision episodes.")
            return episodes
    except Exception as e:
        print(f"      -> Error fetching StrategyQA: {e}")
        return []

def fetch_mmlu_law(limit: int = 100):
    url = f"https://datasets-server.huggingface.co/rows?dataset=cais/mmlu&config=professional_law&split=test&offset=0&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    print(f"[2/2] Fetching MMLU Professional Law ({limit} questions)...")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            rows = data.get("rows", [])
            episodes = []
            choice_map = {0: "A", 1: "B", 2: "C", 3: "D"}
            for idx, item in enumerate(rows[:limit]):
                r = item.get("row", {})
                episodes.append({
                    "task_id": f"MMLU_LAW_{idx+1:03d}",
                    "benchmark": "MMLU_Professional_Law",
                    "domain": "Legal_Judgment",
                    "question": r.get("question", ""),
                    "choices": r.get("choices", []),
                    "ground_truth": choice_map.get(r.get("answer"), "?"),
                    "source": "https://huggingface.co/datasets/cais/mmlu"
                })
            print(f"      -> Ingested {len(episodes)} MMLU Law decision episodes.")
            return episodes
    except Exception as e:
        print(f"      -> Error fetching MMLU Law: {e}")
        return []

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Ingest ONLY the 2 premier benchmarks
    strategy_eps = fetch_strategyqa(limit=100)
    law_eps = fetch_mmlu_law(limit=100)
    
    all_episodes = strategy_eps + law_eps
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for ep in all_episodes:
            f.write(json.dumps(ep) + "\n")
            
    print("\n" + "=" * 65)
    print(f"READY: Ingested exactly 2 benchmark datasets ({len(all_episodes)} total questions).")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"  • StrategyQA:            {len(strategy_eps)} questions")
    print(f"  • MMLU Professional Law: {len(law_eps)} questions")
    print("=" * 65)

if __name__ == "__main__":
    main()
