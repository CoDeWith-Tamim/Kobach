# Overlap Map

এই document-এ existing tool/paper-এর সাথে KOBACH কোথায় মেলে, কোথায় আলাদা — সেটা honestly লিখে রাখা হবে। Stage A শেষ হওয়ার আগে এটা পূরণ করতে হবে।

| Existing work | কী করে | KOBACH-এর সাথে পার্থক্য |
|---|---|---|
| BanglaSafe / BanglaShield / SurakshaEval | বাংলা safety classifier/benchmark | ওরা content safety মাপে, KOBACH agent authorization + injection একসাথে মাপে |
| Garak | Generic LLM red-teaming (English-centric) | Bangla/Banglish script-shift axis নেই |
| PromptFoo / Rebuff | Prompt injection detection tool | Agent authorization boundary টেস্ট করে না |
| CaMeL / FIDES / Progent | Policy-level (capability-based) agent security | Bangla/Banglish multilingual angle নেই |

## খোলা প্রশ্ন (Stage A-তে উত্তর দিতে হবে)
- [ ] এই চারটার মধ্যে কেউ কি Bangla/Banglish + authorization একসাথে করেছে? (arXiv/Scholar সার্চ)
- [ ] Dataset license — কোনো existing dataset ব্যবহার করলে তার লাইসেন্স কী অনুমতি দেয়
