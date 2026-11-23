import os

# Resolve paths relative to this script's directory
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(_SCRIPT_DIR, 'report/NeuroSense_Project_Report.md')

sections = []

# Title Page
sections.append("""# VISVESVARAYA TECHNOLOGICAL UNIVERSITY
### “Jnana Sangama”, Belagavi - 590018, Karnataka, India

<br>

<div align="center">

## A Project Report on
# **NeuroSense: An AI-Powered Multi-Modal Clinical Decision Support Framework for Huntington’s Disease Detection and Progression Analysis**

<br>

*Submitted in partial fulfillment of the requirements for the award of the degree of*
### **BACHELOR OF ENGINEERING**
### IN
### **COMPUTER SCIENCE AND DESIGN**

<br>

**Submitted By:**

| Student Name | University Seat Number (USN) | E-mail ID |
| :--- | :--- | :--- |
| **Poorna Vilas** | 1SJ23CG035 | poornavilasrsr20@gmail.com |
| **Shivam Kumar Yadav** | 1SJ23CG051 | sy657958@gmail.com |
| **Prithvi Rao** | 1SJ23CG038 | prithvirao826@gmail.com |
| **Suraj S** | 1SJ23CG056 | surajsatish33@gmail.com |

<br>

**Carried out at:**
Project Lab, Department of Computer Science and Design
SJC Institute of Technology, Chikkaballapur - 562101

<br>

**Under the Guidance of:**
**Dr. Bharathi M**
Professor & Head of Department
Department of Computer Science and Design
SJC Institute of Technology, Chikkaballapur

<br>

**Co-guided by:**
**Mrs. Ambika S. R.**
Assistant Professor & Research Scholar
Department of Computer Science and Design
SJC Institute of Technology, Chikkaballapur

<br>

<img src="../neurosense/frontend/dist/hero-brain.png" alt="SJCIT" width="120"/>

### **DEPARTMENT OF COMPUTER SCIENCE AND DESIGN**
### **SJC INSTITUTE OF TECHNOLOGY**
**(Affiliated to Visvesvaraya Technological University, Belagavi & Approved by AICTE, New Delhi)**
**CHIKKABALLAPUR – 562101, KARNATAKA, INDIA**
### **ACADEMIC YEAR 2026–2027**

</div>

---
<div style="page-break-after: always;"></div>
""")

# Certificate Page
sections.append("""## || Jai Sri Gurudev ||
### Sri Adichunchanagiri Shikshana Trust®
## **SJC INSTITUTE OF TECHNOLOGY**
### Chikkaballapur - 562101, Karnataka, India
### **DEPARTMENT OF COMPUTER SCIENCE AND DESIGN**

<br>

<div align="center">
<img src="../neurosense/frontend/dist/hero-brain.png" alt="SJCIT Logo" width="100"/>

<br>

## **CERTIFICATE**
</div>

This is to certify that the Project Work entitled **“NeuroSense: An AI-Powered Multi-Modal Clinical Decision Support Framework for Huntington’s Disease Detection and Progression Analysis”** is a bonafide work carried out by **POORNA VILAS (1SJ23CG035)**, **SHIVAM KUMAR YADAV (1SJ23CG051)**, **PRITHVI RAO (1SJ23CG038)**, and **SURAJ S (1SJ23CG056)** in partial fulfillment for the seventh semester of Bachelor of Engineering in Computer Science and Design of Visvesvaraya Technological University, Belagavi during the academic year 2026–2027. It is certified that all corrections and suggestions indicated during internal evaluations have been incorporated into this report. The Project Report has been approved as it satisfies the academic requirements prescribed for the degree of Bachelor of Engineering.

<br><br><br>

| …………………………………… | …………………………………… | …………………………………… |
| :---: | :---: | :---: |
| **Signature of Guide** | **Signature of HOD** | **Signature of Principal** |
| **Dr. Bharathi M** | **Dr. Bharathi M** | **Dr. G. T. Raju** |
| Professor & HOD, Dept. of CSD | Professor & HOD, Dept. of CSD | Principal, SJCIT |
| SJC Institute of Technology | SJC Institute of Technology | Chikkaballapur - 562101 |

<br><br>

### **External Viva-Voce Examination:**

| Name of External Examiner | Affiliation / Institution | Signature with Date |
| :--- | :--- | :--- |
| **1.** …………………………………………………… | …………………………………………………… | ……………………………… |
| **2.** …………………………………………………… | …………………………………………………… | ……………………………… |

---
<div style="page-break-after: always;"></div>
""")

# Declaration Page
sections.append("""## **DECLARATION**

<br>

We, **POORNA VILAS (1SJ23CG035)**, **SHIVAM KUMAR YADAV (1SJ23CG051)**, **PRITHVI RAO (1SJ23CG038)**, and **SURAJ S (1SJ23CG056)**, students of Seventh Semester B.E. in Computer Science and Design at SJC Institute of Technology, Chikkaballapur, hereby declare that the dissertation work entitled **“NeuroSense: An AI-Powered Multi-Modal Clinical Decision Support Framework for Huntington’s Disease Detection and Progression Analysis”** has been independently carried out by us at the Project Laboratory, Department of Computer Science and Design, SJC Institute of Technology, under the supervision and guidance of **Dr. Bharathi M**, Professor & Head of the Department, Department of Computer Science and Design, SJC Institute of Technology, and co-guided by **Mrs. Ambika S. R.**, Assistant Professor, Department of Computer Science and Design.

This report is submitted in partial fulfillment of the requirements for the award of the degree of **Bachelor of Engineering in Computer Science and Design** of Visvesvaraya Technological University, Belagavi, during the academic year 2026–2027.

We further solemnly declare that this report has not been submitted previously, in part or full, to this or any other university or institution for the award of any degree, diploma, associateship, or other academic titles.

<br><br>

**Place:** Chikkaballapur  
**Date:** 27th October 2026  

<br>

**Signatures of Candidates:**

1. **POORNA VILAS** (1SJ23CG035) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _______________________  
2. **SHIVAM KUMAR YADAV** (1SJ23CG051) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _______________________  
3. **PRITHVI RAO** (1SJ23CG038) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _______________________  
4. **SURAJ S** (1SJ23CG056) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _______________________  

---
<div style="page-break-after: always;"></div>
""")

# Abstract Page
sections.append("""## **ABSTRACT**

Huntington’s Disease (HD) is a fatal, autosomal-dominant neurodegenerative disorder caused by an unstable cytosine-adenine-guanine (CAG) trinucleotide repeat expansion within the huntingtin (*HTT*) gene on chromosome 4. The progressive motor, cognitive, and psychiatric decline in HD is driven by the selective loss of medium spiny projection neurons in the corpus striatum (caudate nucleus and putamen), eventually spreading through frontostriatal and cortical networks. In standard clinical practice, diagnosis is confirmed only after manifest chorea or involuntary motor signs appear, by which point irreversible brain atrophy has already accumulated. Existing machine learning diagnostic pipelines remain fundamentally single-modal—relying exclusively on structural magnetic resonance imaging (MRI), discrete genetic repeats, or subjective clinical rating scales (such as the Unified Huntington's Disease Rating Scale - UHDRS). These unimodal pipelines provide a fragmented view of disease pathology, exhibit high vulnerability to noise, and offer zero cross-modal explainability to attending neurologists.

To overcome these clinical barriers, this project presents **NeuroSense**, an intelligent, end-to-end multi-modal artificial intelligence clinical decision support framework. NeuroSense unifies 3D volumetric structural MRI (T1-weighted), genetic biomarkers (CAG repeat length), and longitudinal clinical-motor scores (Total Motor Score, Total Functional Capacity, Symbol Digit Modalities Test) into a cohesive predictive representation. The imaging stream utilizes a 3D ResNet-50 backbone initialized with Med3D transfer learning weights to extract 256-dimensional spatial representations of subcortical atrophy. Concurrently, a Bidirectional Long Short-Term Memory (Bi-LSTM) network captures temporal disease dynamics from longitudinal clinical visits. These disparate modalities are harmonized using an 8-head pre-layer normalization cross-attention transformer fusion block, where imaging features serve as queries while clinical and genetic embeddings provide contextual keys and values.

The system performs multi-task inference, simultaneously predicting three-class disease staging (Pre-manifest HD, Early Manifest HD, Advanced HD) and forecasting continuous 12- and 24-month motor progression trajectories. To establish clinical transparency and safety, NeuroSense implements dual explainability: 3D Grad-CAM++ generates volumetric saliency heatmaps highlighting targeted striatal atrophy in MRI scans, while TreeSHAP produces patient-specific waterfall attribution plots for genetic and clinical features. The complete system is deployed as an enterprise-grade clinical platform comprising a high-throughput asynchronous FastAPI backend and a modern React 19 web application featuring real-time WebGL/Three.js interactive 3D brain visualization, a digital cognitive testing battery, and an LLM-powered clinical query assistant.

Rigorous empirical evaluation on the PREDICT-HD cohort (n ≈ 1,000 subjects over 6+ years) and the OpenNeuro HD benchmark demonstrates that NeuroSense achieves an area under the receiver operating characteristic curve (AUC-ROC) of **0.902 ± 0.014**, a macro F1-score of **0.865**, and a progression forecasting mean absolute error (MAE) of **2.82 months**, outperforming single-modality baselines by over 8.8% in discriminative capability. Dual explainability demonstrates greater than 88% spatial overlap with expert anatomical striatum masks, while end-to-end inference latency is sustained under **18.4 seconds** on standard GPU hardware. NeuroSense represents a clinically viable, transparent, and scalable AI platform for early detection, therapeutic stratification, and proactive management of neurodegenerative disorders.

---
<div style="page-break-after: always;"></div>
""")

# Acknowledgement Page
sections.append("""## **ACKNOWLEDGEMENT**

With profound reverential pranam, we express our heartfelt gratitude and humble salutations at the lotus feet of His Holiness Paramapoojya Jagadguru Byravaikya Padmabhushana **Sri Sri Sri Dr. Balagangadharanatha Maha Swamiji**, His Holiness Paramapoojya Jagadguru **Sri Sri Sri Dr. Nirmalanandanatha Maha Swamiji**, and **Sri Sri Mangalanatha Swamiji**, Sri Adichunchanagiri Mahasamsthana Math, for their divine presence, perpetual guidance, and boundless blessings.

First and foremost, we wish to express our deep sense of gratitude to our esteemed institution, **SJC Institute of Technology (SJCIT)**, Chikkaballapur, for providing an exemplary academic ecosystem, state-of-the-art computational infrastructure, and the opportunity to carry out this Major Project work.

We extend our sincere and profound gratitude to **Dr. G. T. Raju**, Principal, SJC Institute of Technology, for his visionary leadership, continuous encouragement, and for providing the necessary facilities and support to make this endeavor successful.

We extend our special in-depth, heartfelt, and sincere gratitude to our esteemed Head of the Department and Project Guide, **Dr. Bharathi M**, Professor & Head of Department, Department of Computer Science and Design, for her insightful technical advice, patient mentorship, constructive criticism, and steadfast encouragement throughout the planning and implementation of this research work.

We convey our immense pleasure and deep gratitude to our Project Coordinator and Co-Guide, **Mrs. Ambika S. R.**, Assistant Professor & Research Scholar, Department of Computer Science and Design, for her meticulous guidance, continuous assistance, and valuable suggestions during all stages of development.

We also express our warm thanks to all teaching and technical staff members of the Department of Computer Science and Design, SJCIT, for their cooperation and constant support.

Finally, we express our warmest love and gratitude to our beloved parents and family members for their unconditional sacrifices, moral encouragement, and enduring support, and to our dear friends and classmates who stood by us and assisted in the successful completion of this project report.

<br><br>

**POORNA VILAS (1SJ23CG035)**  
**SHIVAM KUMAR YADAV (1SJ23CG051)**  
**PRITHVI RAO (1SJ23CG038)**  
**SURAJ S (1SJ23CG056)**  

---
<div style="page-break-after: always;"></div>
""")

with open(md_path, 'w') as f:
    f.write('\n'.join(sections))

print("Wrote preliminaries successfully.")
