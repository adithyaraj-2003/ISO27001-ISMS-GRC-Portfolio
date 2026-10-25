# 🛡️ ISO/IEC 27001:2022 ISMS & GRC Engineering Portfolio — NexusCloud SaaS Ltd.

 📌 Project Overview
This repository contains an end-to-end *Information Security Management System (ISMS)* implementation case study for *NexusCloud SaaS Ltd.*, a cloud-native B2B SaaS platform hosted on AWS. 

Designed from a practitioner's perspective, this project fulfills the core requirements of **ISO/IEC 27001:2022 Clauses 6.1.2 (Risk Assessment)** and **6.1.3 (Risk Treatment & Statement of Applicability)**, while bridging governance requirements with automated technical evidence mapped to **SOC 2 (TSC)** and **NIST CSF 2.0**.

---

 📂 Repository Deliverables

1. `NexusCloud_ISO27001_Risk_Register.xlsx`
   * **Scope:** 15 core cloud, application, endpoint, and operational assets (`AST-01` to `AST-15`).
   * **Methodology:** Quantitative **5×5 Likelihood × Impact** risk scoring matrix (Max Score: 25).
   * **Contents:** Asset identification, threat/vulnerability modeling, inherent risk scoring, formal risk treatment decisions (*Mitigate, Transfer, Avoid, Accept*), ISO 27001:2022 Annex A control mappings, and post-mitigation residual risk scores.

2. **`NexusCloud_Statement_of_Applicability_SoA.xlsx`**
   * **Scope:** 31 controls across all four **ISO/IEC 27001:2022 Annex A** themes:
     * **Organizational (`A.5`)** | **People (`A.6`)** | **Physical (`A.7`)** | **Technological (`A.8`)**
   * **Auditor Traceability:** Links every control directly back to specific asset IDs in the Risk Register, documents clear inclusion/exclusion justifications (including AWS Shared Responsibility Model exclusions for physical data centers under `A.7.5` and `A.7.11`), and specifies concrete audit evidence artifacts.

---

## ⚙️ Bridging GRC with Technical Automation (Compliance-as-Code)

Rather than relying solely on manual administrative checks, this ISMS integrates technical security engineering artifacts as continuous audit evidence:

| Technical Artifact | ISO 27001:2022 | SOC 2 Criteria | NIST CSF 2.0 | Audit Objective & Evidence Generated |
| :--- | :--- | :--- | :--- | :--- |
| **Python Access Reconciliation Script** | `Annex A.5.18`<br>`Annex A.8.2` | `CC6.2`<br>`CC6.3` | `PR.AA-05` | Automates user access reviews by comparing active Linux/IAM accounts against authoritative HR records to detect and revoke orphaned accounts. |
| **AWS Wazuh SIEM & Zeek Log Integration** | `Annex A.8.15`<br>`Annex A.8.16` | `CC7.2`<br>`CC7.3` | `DE.CM-01`<br>`DE.AE-02` | Centralizes network and host telemetry into tamper-evident logs with real-time detection rules for unauthorized access and anomalous traffic. |

---

## 📊 Risk Scoring Matrix Summary (Clause 6.1.2)
* **High Risk (15–25):** Immediate treatment required via technical/organizational controls before audit sign-off.
* **Medium Risk (9–14):** Active monitoring and scheduled mitigation required.
* **Low Risk (1–8):** Acceptable residual risk level (Management sign-off).
