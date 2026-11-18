# KOBACH

Bangla/Banglish-সহ multilingual prompt-injection ও authorization security evaluation — tool-ব্যবহারকারী AI এজেন্টদের জন্য।

## Engineering identity (এক লাইনে)
Multilingual adversarial input-এর মুখেও tool-using AI agent-এর authorization boundary কতটা নির্ভরযোগ্য থাকে — সেটা নির্মাণ, পরীক্ষা এবং পরিমাপ করা।

এটা নতুন একটা Bangla safety classifier না, আর নতুন একটা generic red-teaming tool না। এটা দুটোর সংযোগস্থলে — ভাষাভিত্তিক আক্রমণ আর এজেন্টের permission ব্যবস্থা একসাথে টেস্ট করা।

## Stage A — এখন কী বানাচ্ছি
- [ ] Overlap map (existing work-এর সাথে কী ওভারল্যাপ করে, লিখিতভাবে)
- [ ] Dataset/license audit
- [ ] 3-4টা attack category কাজ করছে (`attacks/taxonomy.yaml`)
- [ ] Layered defense: regex pre-filter → classifier → LLM-as-judge (`defense/`)
- [ ] Evaluation harness: bypass rate, false-positive rate (আলাদা legit-query সেটে), latency (`eval/`)
- [ ] GitHub-এ README সহ public

**Stage A শেষ হওয়ার শর্ত (feeling না, fact):**
3-4টা attack category কাজ করছে + আলাদা legit-query সেটে false-positive rate মাপা হয়েছে + ফলাফল public।

## Structure
```
kobach/
├── attacks/           # attack taxonomy + generator scripts
│   └── taxonomy.yaml
├── defense/           # layered defense: regex, classifier, LLM-judge
├── eval/              # evaluation harness + metrics
├── data/
│   ├── legit_queries/ # বৈধ প্রশ্নের সেট (false-positive মাপার জন্য)
│   └── results/       # experiment run logs (run_id ভিত্তিক)
├── scripts/           # run/report scripts
└── docs/              # overlap map, hypothesis, findings
```

## Stage B+ (এখন শুরু করার দরকার নেই — reference-এর জন্য)
- NovaNotes-কে tool-using agent বানানো (`read_note`, `create_note`, `update_note`, `delete_note`, `share_note` — সব server-side enforced)
- Content-level vs policy-level defense তুলনা
- Pre-registered hypothesis: policy-level authorization বাংলা/বাংলিশ script-shift আক্রমণে content-level-এর চেয়ে কম ভাঙবে
- মূল security metric: **unauthorized action rate** (শুধু "block হলো কিনা" না)

## Drift-check
কোনো স্টেজে ~6 সপ্তাহ meaningful progress না হলে থেমে সিদ্ধান্ত নাও: continue / shrink / pause।

