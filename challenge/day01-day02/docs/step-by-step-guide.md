# SAP Enterprise AI Architecture Days 1 and 2

## Detailed execution guide for Srini Gummalla

You have already created your BTP trial and GitHub repository. Begin with verification and a concrete procurement use case. By the end of these two days, you will have a documented environment, an architecture charter, a procurement process map, 12 analyzed invoice cases and a small working rules baseline.

This guide continues the original 60 day workbook. Every step identifies where to work, what to do, which file to update and what completion looks like. The starter ZIP contains editable Markdown templates, synthetic JSON data, an unfinished exercise and a separate reference solution.

| Your existing setup | Value you supplied |
|---|---|
| Region | US East VA on AWS cf-us10 |
| Global account | 69b7f502trial |
| Subaccount | trial |
| Cloud Foundry org | 69b7f502trial |
| Space | dev |
| GitHub repository | srinigummalla/sap-btp-ai-architect-journey |

Your values are prefilled in the environment template. They have not been independently verified in your authenticated cockpit. The repository URL could not be inspected from this session; nothing in this guide assumes it is empty. No repository changes have been pushed for you.

## What you need open

1. Your BTP trial cockpit in a browser.
2. Your existing GitHub repository in another tab.
3. The extracted starter folder and a text editor such as VS Code.
4. Python 3.10 or newer for the Day 2 coding exercise. It uses only the standard library. You can complete Day 1 entirely in the browser.

Keep the supplied folder named challenge/day01-day02. All paths in this guide are relative to that lab folder unless a command explicitly starts from the repository root.

## Time budget

Day 1 is approximately 180 minutes. Day 2 is approximately 210 minutes. Pause between steps and record actual time. No SAP application deployment, LLM subscription or S/4HANA posting is required for these two days. The BTP trial is an environment to learn and later deploy extensions; it does not by itself establish access to S/4HANA purchasing transactions.

The lab is a proposed portfolio exercise. Its company, documents, prices, policies and performance targets are synthetic. A completed starter template is evidence of planning; independent edits, working code and explanations establish your own learning.

<!--page-->
# Day 1 Step 1 Verify your existing BTP setup

**Time:** 30 minutes. **Work in:** BTP cockpit and docs/day-01/environment.md.

1. Open https://cockpit.hanatrial.ondemand.com/trial/ and enter your trial account. Reuse the existing account.
2. Select global account 69b7f502trial and open subaccount trial. On Overview, check the region against cf-us10 and the values you supplied. Record the date you checked them.
3. Find the Cloud Foundry environment section. Record its displayed status and copy the exact API endpoint into environment.md. Region codes do not prove the precise endpoint, particularly when a region has multiple landscapes.
4. Open the org and the dev space through the cockpit navigation. Confirm the space exists. An empty Applications list is acceptable at this point.
5. Inspect space membership or role information if available. Record whether your user has Space Developer, or write NOT CHECKED if you cannot inspect it. Do not infer deployment permission from being able to view the account.
6. Inspect the account's trial status and any expiry or extension notice. Record what the cockpit shows so a later expiry does not surprise you.

The account model and cockpit navigation are described in SAP's trial tour. A subaccount belongs to a region; the global account manages its subaccounts. Cloud Foundry deployment happens in spaces within the org. [R1]

## Inspect service access without provisioning

7. At global account level, open Entitlements, then Entity Assignments where available. Select subaccount trial and inspect its assigned service plans and quota. The labels can vary with cockpit navigation; use the subaccount scope if it exposes the equivalent view. [R2]
8. Fill the service rows in environment.md: Cloud Foundry runtime, Business Application Studio, Destination, Integration Suite, HANA Cloud, AI Core, AI Launchpad, ABAP environment and Joule or Joule Studio. Record the exact plan, ABSENT or NOT CHECKED. Absence is not a Day 1 failure.
9. In subaccount trial, inspect Services, then Instances and Subscriptions. Record which subscriptions or instances already exist. A listing in the marketplace or an assigned entitlement does not establish a running instance.
10. Finish these two sentences: “I can verify that my environment has…” and “I still need separate access or confirmation for…”. Keep private screenshots locally if useful. Do not commit service keys or credentials.

**Expected result:** A filled environment inventory with observed values and explicit unknowns. You have distinguished account creation, service entitlement, service instance and application deployment. No service activation is necessary to pass this step.

**If blocked:** Check the global account versus subaccount breadcrumb first. If you cannot view a service or role, record the exact missing view and continue. Do not create a second account or change entitlements just to complete this inventory.

<!--page-->
# Day 1 Step 2 Add the learning folder to GitHub

**Time:** 25 minutes. **Work in:** extracted starter kit, your editor and GitHub.

1. Extract SAP_Day_1_2_Starter_Kit.zip. Inside it, locate challenge/day01-day02. Preserve this nesting so the guide's paths work.
2. Open the lab's README.md. Locate docs/day-01, docs/day-02, data and src. The templates contain TODO fields for your own work. The reference solution is supplied separately so you can try the exercise first.
3. Keep your existing repository files. Add the new folder rather than replacing a root README or restructuring previous work. If challenge/day01-day02 already exists, compare the contents before copying over any file.

| Location inside the lab | Purpose |
|---|---|
| docs/day-01 | Environment, skills, jobs, charter, ADR and interview notes |
| docs/day-02 | Process, dictionary, manual analysis, rules and review |
| data/cases.json | The 12 synthetic input cases |
| data/expected_results.json | Answer key to open after manual analysis |
| src/student_classifier.py | Your three implementation tasks |
| src/reference_classifier.py | Complete reference for comparison |
| src/evaluate.py | Compare a classifier with the learning answer key |
| docs/progress.md | Completion and evidence ledger |

## Browser upload route

4. Open https://github.com/srinigummalla/sap-btp-ai-architect-journey and select the Code tab. Above the files, use Add file and Upload files. For an empty repository, use its initial upload link instead. [R3]
5. Drag the challenge folder from the extracted kit into the upload area. Before committing, inspect the displayed paths. They should begin with challenge/day01-day02, with no extra ZIP-name directory.
6. Use commit message “Add Day 1 and Day 2 learning starter”. Where offered, select a new branch named day-01-02-foundation and propose the changes. Review the diff before merging through the repository's normal workflow. If the empty repository creates its initial branch first, use that initial commit and create a branch for later edits.
7. Open challenge/day01-day02/README.md on GitHub and confirm it renders. Open environment.md to verify your supplied account values are present.

**Expected result:** The starter files are visible in your repository, and existing work remains intact. It is fine to upload completed Day 1 files together at the end instead of making this starter commit now.

**Browser editing:** Open a Markdown file, choose Edit, replace its TODO fields and save with a meaningful commit message. For many edits, use a local clone and upload or push the completed files together. The next page provides the optional command line route.

<!--page-->
# Day 1 Optional local Git workflow

Use this page if Git is already installed. It replaces the browser upload procedure; you do not need to perform both. Run commands in your laptop terminal or VS Code terminal. These commands do not run inside the BTP cockpit.

## Open the existing repository locally

If you have not cloned it, choose a parent working folder and run:

```text
git clone https://github.com/srinigummalla/sap-btp-ai-architect-journey.git
cd sap-btp-ai-architect-journey
git status
git switch -c day-01-02-foundation
```

If you already have a clone, open that folder and run git status. Preserve any existing uncommitted work. If the branch already exists locally, use git switch day-01-02-foundation instead of creating it again.

Copy the extracted challenge/day01-day02 folder into this repository using your file manager. Confirm that the folder is directly below the repository root. Read the diff before your first commit.

```text
git status
git add challenge/day01-day02
git diff --cached --stat
git diff --cached
git commit -m "Add Day 1 and Day 2 learning starter"
git push -u origin day-01-02-foundation
```

Use your normal GitHub authentication. If Git prompts for an identity or authentication setup you have not completed, use GitHub's browser upload route for Day 1 and resolve Git setup separately. Never put a token in the repository URL or in a committed file.

## Link the lab from your existing README

If your root README already exists, append these lines after reviewing its structure:

```markdown
## SAP AI architecture foundation

[Days 1 and 2 lab](challenge/day01-day02/README.md)

Scope: environment verification, procurement process analysis,
synthetic invoice cases and a deterministic matching baseline.
```

Do not replace an existing root README with the starter's README. If the root README is absent, you can create one with this section and your own repository description.

**Completion check:** Can you navigate from your repository to the lab README, open a template and identify what you must write yourself? If yes, move on. You do not need GitHub Actions, branch protection changes, a website or a cloud deployment today.

<!--page-->
# Day 1 Steps 3 and 4 Establish your starting point

## Step 3 Score your skills with evidence

**Time:** 20 minutes. **File:** docs/day-01/skills-baseline.md.

1. For each row, assign your own score: 0 means new; 1 means you recognize terms; 2 means you can explain with help; 3 means you can build or defend independently; 4 means you can adapt under a changed constraint and provide evidence.
2. In the evidence column, describe one specific example. “19 years ABAP” is background. “Diagnosed a locking issue, isolated the transaction boundary and explained the chosen fix” is evidence if it actually occurred. Keep employer details anonymous.
3. For a new AI topic, write “No hands-on evidence yet” rather than guessing proficiency.
4. Choose three strengths to carry into your profile and three gaps to prioritize. Include procurement process knowledge if that is a gap.
5. Write five sentences about one real architecture decision you influenced: problem, options, your recommendation, tradeoff and outcome. State when an outcome was not measured.

**Expected result:** A scored matrix supported by examples, not an optimistic list of technologies. You should be able to defend why you chose each score.

## Step 4 Compare five real job descriptions

**Time:** 30 minutes. **File:** docs/day-01/role-fit.md.

1. Search for the five role phrases in the template. Start with SAP BTP Solution Architect AI and SAP S/4HANA Technical Architect Clean Core. Consider location and working arrangement that fit your actual constraints.
2. Open five distinct current postings, preferably on the employer's careers site. Save the employer, exact title, URL and date checked.
3. For each posting, paraphrase three relevant requirements. Avoid copying an entire job description into a public repository.
4. Mark each requirement as supported by professional evidence, supported only by portfolio work or currently a gap. Today, do not mark planned AI work as completed.
5. Count repeated requirements across your small sample. If four postings mention Integration Suite and three mention security, record those frequencies. Treat these as findings from five postings, not the entire job market.
6. Choose the strongest near term role and explain the fit in three sentences. Keep broader Enterprise AI Architect roles in view, but inspect whether they demand production AI operations or enterprise-wide governance you cannot yet demonstrate.

**Expected result:** Five source-linked rows, a short requirement frequency list and a justified role choice. If a posting disappears, mark it unavailable and replace it. If finding suitable jobs takes longer, record the time and finish the five rows in your next session rather than inventing requirements.

<!--page-->
# Day 1 Steps 5 and 6 Define and defend the project

## Step 5 Write the project charter and first decision

**Time:** 35 minutes. **Files:** project-charter.md and architecture-decision.md in docs/day-01.

1. Read the prefilled charter aloud. Replace wording you would not use yourself. Its proposed problem is: an AP analyst must compare purchasing facts and policies to investigate invoice exceptions.
2. Keep the first slice narrow: one synthetic company code US01, material purchases, currency USD, unit EA and one PO item per case. Investigate missing receipts, price differences and invoice quantity beyond available receipts.
3. Confirm the actors: AP analyst investigates, buyer clarifies price, receiving team clarifies receipts and authorized business roles handle corrections or approvals. These are simulated roles in your case study.
4. Write three acceptance criteria in your own words. Example: “An unavailable receipt lookup produces NEEDS_DATA, never a false claim that no goods were received.” Another: “A valid partial invoice does not fail solely because the full PO is larger.”
5. Keep baseline handling time and savings as NOT MEASURED. List the information a real process owner would have to provide to measure them.
6. In ADR 001, compare standard SAP, deterministic custom matching and an LLM making the entire decision. Explain why this learning lab uses deterministic rules first and will assess standard SAP before proposing customer customization.
7. Add a drawback: the small fixture model does not cover all SAP invoice settings, tolerances, returns or accounting behavior. Identify what would make you revisit the decision.

**Expected result:** A one page charter and a decision record you can explain. You have scoped a business problem before choosing an AI framework.

## Step 6 Use AI for critique and record your introduction

**Time:** 25 minutes. **File:** docs/day-01/interview-and-review.md.

1. Write a 150 to 220 word introduction without AI. Cover your actual SAP experience, one demonstrated strength, the architecture target and what you are building to support it.
2. Paste only your synthetic charter and ADR into your AI assistant with this prompt:

```text
Act as a skeptical SAP solution architect. Review this charter
and ADR. Identify five assumptions, two unnecessary components
and three missing acceptance criteria. Do not invent available
SAP services or released APIs. Separate facts from suggestions.
```

3. Record one suggestion you accepted and one you corrected or rejected, with reasons. Do not accept added services solely because AI proposed them.
4. Record a two minute introduction privately on your phone. Listen once. Replace vague phrases with an actual decision, example or learning objective.

**Expected result:** Your own introduction, a critique log and a recording. You can say clearly which experience came from employment and which work is an independent portfolio project.

<!--page-->
# Day 1 Step 7 Complete the evidence check

**Time:** 15 minutes. **Work in:** docs/progress.md and GitHub.

1. Check that the Day 1 templates contain your own edits. A remaining TODO for an actual unknown is acceptable only when you label the unknown and next action explicitly.
2. Update the six Day 1 evidence rows in docs/progress.md as appropriate. Link the files or commits. Do not mark the student classifier complete yet.
3. Review files for credentials and confidential material. Save private audio and screenshots separately; a short text summary is enough for the public portfolio.
4. Commit your completed Day 1 work through the browser, or from the repository root:

```text
git add challenge/day01-day02/docs/day-01
git add challenge/day01-day02/docs/progress.md
git diff --cached
git commit -m "Complete Day 1 environment scope and architecture baseline"
git push
```

## Answer these questions without notes

**What have you actually completed?** An environment inventory, skills baseline, five role assessments, a project charter and an architecture decision. You have not yet built an AI agent.

**Does BTP trial mean S/4HANA is available?** No. You have an extension platform account. Access to an S/4HANA application, its business data and permitted APIs must be established separately.

**Why use your ABAP background?** It gives you experience with SAP business objects, interfaces, debugging and delivery constraints. Support the answer with one real example rather than years alone.

**Why avoid AI matching as the first implementation?** You need a repeatable reference for facts and arithmetic. Later you can evaluate whether AI adds useful explanation or routing without losing correctness.

## Day 1 is complete when

- Your BTP values are checked, and service availability has explicit statuses.
- Your lab folder is present in GitHub and previous work is preserved.
- You have scored your skills and recorded five real role assessments.
- Your charter has actors, scope, exclusions and three acceptance criteria.
- Your ADR compares credible alternatives and names a limitation.
- You can give your two minute introduction without implying production AI experience.

**Submit for review:** The repository branch or commit, the three biggest gaps, the charter, ADR 001, your introduction text and any blocked BTP checks. No passwords, tokens or service key exports are needed.

<!--page-->
# Day 2 Step 1 Understand the procurement process

**Time:** 30 minutes. **File:** docs/day-02/process-map.md.

1. Read the table below. For each row, say who owns the step, what evidence it creates and what question it answers. Then inspect the Mermaid process diagram in process-map.md; GitHub should render it when you view the Markdown file.

| Step | Business question | Typical evidence in this example |
|---|---|---|
| Purchase requisition | What do we need internally | Request for 100 units |
| Purchase order | What did we agree to buy | 100 units at USD 50 each |
| Goods receipt | What was recorded as received | Receipt of 100 units |
| Supplier invoice | What is the supplier billing | Invoice for 100 units at USD 50 |
| Invoice verification | Does the billed claim align with the relevant facts and controls | Matching result or exception |
| Exception resolution | Who must clarify or correct the difference | Buyer or receiving evidence |
| Payment | Which due items are authorized to be paid | Separate finance payment controls |

2. Trace one normal case: a buyer orders 100 units, the warehouse records 100 units, and the supplier invoices 100 units at the agreed price. Explain why the comparison finds no mismatch under our lab rules.
3. Trace one exception: 60 units are recorded as received and the supplier invoices 100. AP must investigate the remaining 40. A missing receipt record is not proof that physical delivery never happened.
4. Add a note to your process map: invoice arrival and goods receipt do not always occur in one fixed order. Actual SAP invoice behavior depends on the process, PO settings and tolerances. In particular, goods-receipt-based invoice verification relates invoice items to received deliveries. [R4]
5. Write your own six sentence process explanation below the diagram. Add one difference from a real process you have encountered, if you can do so without revealing company details.

## Keep two related workflows distinct

An invoice exception may be identified during invoice processing. A GR/IR reconciliation issue concerns the purchasing and financial records after relevant postings. They are related but not interchangeable. SAP provides standard reconciliation worklists and investigation capabilities; consider these before building a replacement. [R5, R6]

**Expected result:** You can explain the process, actors and documents without starting with tables or transaction codes. You know that a BTP trial does not let you perform S/4HANA goods receipt or invoice postings unless a separate connected application is available.

<!--page-->
# Day 2 Step 2 Trace one case through the data

**Time:** 20 minutes. **Files:** data/cases.json and docs/day-02/data-dictionary.md.

1. Open cases.json in your editor. It is an array of 12 independent scenario snapshots. C01 through C12 are not successive events for one purchase order.
2. Locate C01. Read its po, receipts, prior_invoiced_quantity and invoice objects. Identify the document keys and unit of measure. The field names are a teaching model, not a released SAP API schema.
3. Calculate the following on paper or in your notes:

```text
PO quantity                       = 100 EA
PO unit price                     = USD 50 per EA
Total recorded receipt quantity   = 100 EA
Previously invoiced quantity      = 0 EA
Available received quantity       = 100 - 0 = 100 EA
Current invoice quantity          = 100 EA
Current invoice unit price        = USD 50 per EA
Price difference per unit         = 50 - 50 = USD 0
Price difference amount           = 0 x 100 = USD 0
Quantity beyond available receipt = max(100 - 100, 0) = 0 EA
```

4. Write MATCH for C01 in manual-analysis.md. Add the explanation: “No mismatch under the defined teaching rules. This result does not authorize payment.”
5. Read data-dictionary.md and check these two boundaries carefully:

**Prior invoices matter.** Available received quantity is total receipts minus the quantity already invoiced before the current invoice. Comparing only current invoice quantity with the PO misses previously consumed receipt quantities.

**Unknown is not zero.** In this dataset, receipts equal to null means a lookup did not return trustworthy receipt data. An empty receipts list means a successful lookup with no receipt records. These lead to different results and different investigation owners.

6. Read the exclusions in data/README.md. We exclude tax, freight, unit conversion, currency conversion, returns, credit memos and multiple PO items. Price is per one EA. The lab aggregates receipts; it does not implement individual GR-item allocation or all SAP tolerance behavior.

**Expected result:** You can point to every input used in C01 and show the arithmetic yourself. You can explain why fresh data, complete history and explicit units will matter when a real SAP API replaces the fixtures later.

<!--page-->
# Day 2 Step 3 Analyze all 12 cases manually

**Time:** 35 minutes. **File:** docs/day-02/manual-analysis.md. Keep expected_results.json closed until you finish.

For every row, calculate total receipts, available receipts, current invoice quantity and unit price difference. Then propose an outcome, one or more flags, the first owner and the next evidence to request. All PO prices are USD and all quantities EA. C11 deliberately has an invoice currency mismatch.

| Case | PO qty at price | Receipts | Prior invoice qty | Current qty at price | Special condition |
|---|---|---|---|---|---|
| C01 | 100 at 50 | 100 | 0 | 100 at 50 | Worked example |
| C02 | 100 at 50 | 100 | 0 | 100 at 55 | Higher unit price |
| C03 | 100 at 50 | 100 | 0 | 120 at 50 | Larger billed quantity |
| C04 | 100 at 50 | None found | 0 | 100 at 50 | Successful lookup with no receipts |
| C05 | 100 at 50 | 60 | 0 | 60 at 50 | Partial delivery and invoice |
| C06 | 100 at 50 | 100 | 60 | 50 at 50 | Prior billing consumes availability |
| C07 | 100 at 50 | 100 | 0 | 100 at 49 | Lower unit price |
| C08 | 100 at 20 | 20 | 0 | 30 at 21 | Two possible differences |
| C09 | 100 at 50 | Unknown | 0 | 100 at 50 | Receipt lookup unavailable |
| C10 | 100 at 50 | 100 | 0 | 0 at 50 | Zero invoice quantity |
| C11 | 100 at 50 | 100 | 0 | 100 at 50 EUR | Different currency |
| C12 | 100 at 50 | 60 and 40 | 0 | 100 at 50 | Two receipt records |

## Work in this order

1. Finish C01 through C04. Say whether the issue belongs first with AP, the buyer or the receiving team.
2. Finish C05 and C06. Explain why one should pass our quantity rule while the other should not, even though both invoices are smaller than their POs.
3. Finish C07 and C08. Our lab flags any price difference, including a lower price. A single case may have both price and quantity flags.
4. Finish C09 through C12. Route invalid or unsupported inputs before ordinary matching. Do not invent receipt data or silently convert currencies.
5. Write down what you initially misclassified and why. Your correction is useful evidence of reasoning; do not erase the learning history.

**Expected result:** All 12 manual rows are filled. Each exception has an investigation owner and next step. You can explain C04 versus C09 and C05 versus C06 without opening the answer key.

<!--page-->
# Day 2 Step 4 Define the rules precisely

**Time:** 20 minutes. **File:** docs/day-02/decision-table.md.

These rules belong to a synthetic learning exercise. They are not SAP default tolerances, invoice blocking codes or a specification for every procurement process.

1. Read the rule table in the starter file. Verify that input routing happens before matching: invoice quantity must be positive, currencies must match, and receipt data must be available.
2. Calculate available receipts as the sum of receipt quantities minus prior invoiced quantity.
3. When total receipts are zero, flag MISSING_GR. In that case, do not also add the redundant quantity-excess flag.
4. Otherwise, when current invoice quantity exceeds available receipts, flag QUANTITY_EXCEEDS_AVAILABLE_GR.
5. Independently compare the invoice unit price with the PO unit price. Any difference produces PRICE_VARIANCE under our zero-tolerance teaching policy.
6. Preserve multiple flags. If no flags remain, return MATCH. If matching flags exist, return EXCEPTION. Missing receipt evidence produces NEEDS_DATA. Invalid quantity or mismatched currency produces MANUAL_REVIEW.

## Two examples to defend

**C05:** The PO is for 100, the recorded receipt is 60, and the current invoice is for 60. Available receipts are 60. The current invoice is covered under this aggregate model, even though the PO is not fully delivered. Requiring the invoice to equal the full ordered quantity would create a false exception.

**C06:** The receipt total is 100 and earlier invoices already cover 60. Only 40 remain available. A new invoice for 50 exceeds availability by 10. Comparing 50 only with the total receipt of 100 would miss the issue.

**C08:** Available receipts are 20 and the new invoice is for 30. The quantity excess is 10. The price difference is USD 1 per EA, giving a USD 30 price difference over the 30 invoiced units. Keep the two quantities conceptually separate; do not combine quantity units and currency amounts.

## Assign the next action

A price difference usually needs buyer and AP clarification in this lab. A missing receipt or quantity discrepancy needs receiving evidence and AP invoice history. A failed receipt lookup needs integration investigation before business classification. None of these flags is permission to change a PO, record a receipt, release an invoice or make a payment.

**Expected result:** Your decision table is unambiguous enough for another developer to implement, and its assumptions are clearly labeled. Write one case where a real customer's SAP configuration could legitimately behave differently.

<!--page-->
# Day 2 Step 5 Implement the matching baseline

**Time:** 45 minutes including the first evaluation. **Work in:** local editor and terminal.

1. Open a terminal in challenge/day01-day02. In VS Code, open this folder and use Terminal, then New Terminal. In a file manager, open a terminal at the folder if your operating system offers that action.
2. Check your Python command. On Windows try py --version or python --version. On macOS or Linux try python3 --version. Use whichever command reports your installed Python 3 version; replace python in the examples below with that command. [R7]
3. If no Python 3 interpreter is installed, use the official Python installation instructions for your operating system. Continue the manual work while resolving setup. Mark the coding step pending until it actually runs.
4. Open src/student_classifier.py. The input routing is already supplied. Read it and explain why currency mismatch and unknown receipts exit before arithmetic.
5. Complete TODO 1: convert each receipt quantity to Decimal, sum from Decimal("0"), and subtract Decimal(case["prior_invoiced_quantity"]). Replace both None assignments and remove the corresponding unfinished check once implemented.
6. Complete TODO 2: add MISSING_GR when total_received is zero. Use an elif branch for QUANTITY_EXCEEDS_AVAILABLE_GR when invoice_qty is greater than available_received. Remove the NotImplementedError for this task.
7. Complete TODO 3 with a separate if statement comparing invoice and PO unit prices as Decimal. Append PRICE_VARIANCE when they differ. Keep the existing return statement.

## Syntax hints for an ABAP developer

```python
from decimal import Decimal

quantity = Decimal("60")
prior = Decimal("20")
available = quantity - prior
flags = []
if available < Decimal("50"):
    flags.append("QUANTITY_EXCEEDS_AVAILABLE_GR")
```

Python dictionaries provide named fields, lists hold the receipt records and indentation defines blocks. Use Decimal for the provided decimal strings. Avoid float conversions for the unit price comparison in this exercise. No class hierarchy, web server or package installation is required.

8. Save the file and run python src/evaluate.py. If it stops with Exercise unfinished, complete the indicated TODO. If it runs but reports failures, use the next page to isolate the rule error.

**Expected result:** Your own implementation produces the intended outputs. Read the reference solution only after making an attempt. Record what you copied or changed so the portfolio accurately shows your contribution.

<!--page-->
# Day 2 Check your output and diagnose mistakes

Run the student implementation from the lab folder:

```text
python src/evaluate.py
```

Successful completion ends with STUDENT: 12/12 learning cases passed. Every preceding row should show PASS. These are visible teaching cases, not an unseen benchmark or proof of production SAP behavior.

| Case | Expected result | Expected flags |
|---|---|---|
| C01 | MATCH | None |
| C02 | EXCEPTION | PRICE_VARIANCE |
| C03 | EXCEPTION | QUANTITY_EXCEEDS_AVAILABLE_GR |
| C04 | EXCEPTION | MISSING_GR |
| C05 | MATCH | None |
| C06 | EXCEPTION | QUANTITY_EXCEEDS_AVAILABLE_GR |
| C07 | EXCEPTION | PRICE_VARIANCE |
| C08 | EXCEPTION | PRICE_VARIANCE and QUANTITY_EXCEEDS_AVAILABLE_GR |
| C09 | NEEDS_DATA | RECEIPT_DATA_UNAVAILABLE |
| C10 | MANUAL_REVIEW | INVALID_INVOICE_QUANTITY |
| C11 | MANUAL_REVIEW | CURRENCY_MISMATCH |
| C12 | MATCH | None |

**C05 fails:** You may be comparing the invoice with the full PO instead of available receipts. **C06 passes incorrectly:** You probably forgot prior invoicing. **C07 passes incorrectly:** You checked only an upward price difference. **C08 has one flag:** You probably made price comparison an elif of quantity comparison. **C09 becomes MISSING_GR:** You treated null as an empty list. **C12 fails:** Check that you summed both receipts.

If you need the reference, run python src/evaluate.py --reference. It has been checked against these 12 cases. Reading it does not replace explaining the logic yourself. The default student file is intentionally incomplete and should report that until you finish it.

## Make one independent change

Temporarily change C05 invoice quantity from 60 to 70. Predict that the result becomes a quantity exception of 10 units before running it. The old answer key will now report one failed comparison; that is expected because you changed the input. Capture the observation, then restore the original quantity to 60. Do not alter the answer key simply to make incorrect logic pass.

**Evidence to keep:** The student run summary, the rule you corrected, the changed-case prediction and the restored final result. Put a short text record in questions-and-completion.md; you do not need to publish terminal screenshots.

<!--page-->
# Day 2 Steps 6 and 7 Explain the architecture

## Step 6 Decide where AI belongs

**Time:** 20 minutes. **File:** docs/day-02/standard-versus-ai.md.

1. Read the responsibility table in the starter. Keep SAP posting and payment controls in the standard business system. The fixture data and rule code are only a learning baseline.
2. Read the SAP lesson on invoice verification and scan the reconciliation app capabilities in the references. Write two capabilities a real customer may already have. Verify edition, configuration and entitlement before claiming availability. [R4, R5]
3. Write 150 words answering: “What value would the AI layer add beyond a standard worklist and deterministic matching?” A defensible example is assembling evidence, retrieving an approved policy and drafting a cited explanation for the AP analyst.
4. Explain why an LLM should not invent missing receipts, calculate the reference quantities or decide payment authorization.
5. Use the AI prompt in questions-and-completion.md to challenge your manual cases. Record one correction or a reasoned rejection. Keep the original manual work so you can explain the revision.

**Expected result:** You can justify AI with a specific user need, and identify two tasks better handled by standard SAP or deterministic code.

## Step 7 Practice process and architecture questions

**Time:** 25 minutes. **File:** docs/day-02/questions-and-completion.md.

1. Answer all five interview questions in your own words. Record a three minute walkthrough: 45 seconds on the process, 60 seconds on C05 and C06, 45 seconds on missing evidence and 30 seconds on the future AI boundary.
2. Check your answer against these points: PO is agreed purchasing intent; a receipt is a recorded goods movement; an invoice is a supplier claim; verification and payment are distinct responsibilities. Real behavior depends on the configured process.
3. For the partial invoice question, explain that C05 covers a received partial quantity. For missing data, contrast C04's known empty receipt set with C09's unknown result.
4. For the AI question, explain that the deterministic baseline makes arithmetic and rule outcomes independently checkable. For the MATCH question, say it finds no difference within this model and does not approve payment.
5. Review the five MM or FI discovery questions in the starter. Add one based on your own uncertainty. You may discuss them with an appropriate colleague through your normal channels, but a simulated AI role play is not a completed functional expert review.

**Expected result:** A spoken explanation you can deliver without reading code, plus questions that show you understand the limits of your current process knowledge.

<!--page-->
# Day 2 Step 8 Publish evidence and close the two days

**Time:** 15 minutes. **Work in:** docs/progress.md and your GitHub branch.

1. Restore the original case data after your independent mutation exercise. Rerun the student evaluator and record the actual result.
2. Complete questions-and-completion.md with manual analysis status, implementation result, whether you used the reference, one correction and your spoken explanation status.
3. Update docs/progress.md. Separate “starter provided”, “edited by me”, “implemented by me” and “verified by me” where relevant.
4. Commit the specific Day 2 paths from the repository root, or upload the reviewed files through GitHub:

```text
git add challenge/day01-day02/docs/day-02
git add challenge/day01-day02/docs/progress.md
git add challenge/day01-day02/src/student_classifier.py
git diff --cached
git commit -m "Complete Day 2 procurement process and matching baseline"
git push
```

5. Open the updated branch on GitHub. Confirm the process diagram renders, the manual analysis is filled and the student classifier contains your implementation. Keep a pull request if you want to review the work before merging to your default branch. Follow any existing repository rules.

## Day 2 is complete when

- You can explain the procurement process and ownership in ordinary language.
- Your 12 manual analyses are filled, including the reason for every exception.
- Your decision table states its synthetic tolerances and data assumptions.
- The student classifier passes the 12 original learning cases.
- You predicted and observed a changed-case result independently.
- You can defend C05 versus C06 and C04 versus C09 without AI.
- Your architecture note identifies standard SAP, deterministic rules and the proposed AI responsibilities.
- Your work and implementation status are recorded in GitHub.

If Python setup remains blocked, the process and manual analysis can still be complete. Record the coding gap explicitly; do not claim a working prototype until the evaluator runs.

## Send this for the next coaching review

Share the branch or commit URL, your charter, manual-analysis.md, student_classifier.py, the evaluation summary and answers to these two questions: “Why does C06 fail?” and “What does BTP trial still not provide for this project?” Include the exact error text if a step is blocked.

Your next step in the 60 day plan will use this process and baseline to evaluate S/4HANA extension boundaries. You will have concrete requirements to apply to Clean Core, RAP, released APIs and BTP rather than choosing those technologies in the abstract.

<!--page-->
# References and practical troubleshooting

These official sources were checked while preparing the guide. Product interfaces can change; record what your account actually shows. Use the sources to verify the specific concept, then return to the exercise.

**R1 SAP BTP trial tour.** Account model, scopes and cockpit navigation. https://developers.sap.com/tutorials/cp-trial-quick-onboarding

**R2 SAP BTP trial entitlements.** Inspect assigned service plans and quotas. https://developers.sap.com/tutorials/cp-trial-entitlements.html

**R3 GitHub adding files.** Browser uploads and Git-based file additions. https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

**R4 SAP invoice verification types.** PO-based and GR-based concepts; read the GR allocation discussion. https://learning.sap.com/courses/invoice-verification-in-sap-s-4hana/using-different-types-of-invoice-verification

**R5 SAP Fiori apps for GR/IR reconciliation.** Standard investigation and worklist capabilities. https://learning.sap.com/courses/invoice-verification-in-sap-s-4hana/using-fiori-apps-for-gr-ir-reconciliation

**R6 SAP GR/IR account maintenance.** Relationship between goods receipt and invoice receipt records. https://learning.sap.com/courses/exploring-foundations-of-logistics-invoice-verification-in-sap-s-4hana-cloud-private-edition/explaining-gr-ir-account-maintenance-in-logistics-invoice-verification

**R7 Python interpreter.** Selecting and invoking an installed Python interpreter. https://docs.python.org/3/tutorial/interpreter.html

## If a step does not behave as expected

**I cannot see a BTP menu:** Verify the breadcrumb and scope. Record the missing view; do not assume the service is unavailable just because a menu is hidden.

**There is no S/4HANA system:** Use the JSON fixtures. BTP, ABAP environment and an S/4HANA application are distinct capabilities. No S/4HANA connection is required for this lab.

**I cannot open the GitHub repository:** Sign in with the account that owns it and check the exact URL. A failed external fetch does not prove that your repository is missing or private.

**Python is not recognized:** Try the interpreter commands listed in Step 5. If none exists, install from official Python guidance for your operating system or use an already approved development environment. Do not install AI packages for this exercise.

**The script cannot find files:** Keep data and src under the same challenge/day01-day02 folder. Use the interpreter with the script path, not pasted Python code in a shell.

**The script says Exercise unfinished:** This is intentional in the starter. Finish the three TODOs. **A comparison fails:** Use the case-specific diagnostics and correct your rule. Do not modify expected results to hide a mismatch.
