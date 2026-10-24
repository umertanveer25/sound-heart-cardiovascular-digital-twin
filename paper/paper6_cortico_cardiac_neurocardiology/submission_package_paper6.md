# Journal Submission Package: Paper 6

**Manuscript Title:** Cortico-Cardiac Neurocardiology: Directional Vagal Afference and Cerebral Hemodynamics Induced by Contemplative Prayer and 0.10 Hz Acoustic Entrainment  
**Authors:** Muhammad Umer Tanveer (Corresponding Author, ORCID: [0009-0004-9462-8178](https://orcid.org/0009-0004-9462-8178)) & Consortium Co-Investigators  
**Target Journal:** *IEEE Transactions on Affective Computing* (Impact Factor: 11.2)  
**Alternative Target:** *NeuroImage* (Impact Factor: 5.7) / *Frontiers in Human Neuroscience*  

---

## 1. Formal Cover Letter to the Editor-in-Chief

To:  
**Editor-in-Chief**  
*IEEE Transactions on Affective Computing*  

**Dear Editor-in-Chief,**

We are pleased to submit our original research article entitled **"Cortico-Cardiac Neurocardiology: Directional Vagal Afference and Cerebral Hemodynamics Induced by Contemplative Prayer and 0.10 Hz Acoustic Entrainment"** for consideration as a regular paper in *IEEE Transactions on Affective Computing*.

For over a century, cardiovascular neuroscience has treated the heart primarily as an efferent peripheral responder to central nervous system commands. While theoretical models of neurovisceral integration have proposed bidirectional feedback, quantitative proof of whether the heart acts as an active information-theoretic driver of cortical electrophysiology has remained elusive due to reliance on linear correlation metrics and uncoupled single-modality setups.

In this investigation, we establish a standardized multimodal neurocardiac benchmark adhering to the 14-channel AMIGOS electrode topography coupled with synchronized dual-lead electrocardiography (ECG) and transcranial Doppler ultrasound across 40 human subjects ($N = 160$ multimodal epochs). We rigorously evaluate four behavioral regimes: Contemplative Prayer (*Salah*), Harmonic Recitation (*Qur'an*), Sedentary Video Exposure (*TV Screen*), and Transient High-Tempo Stimulation (*Pop Song*).

**Key Discoveries and Contributions:**
1. **Mathematical Proof of Directional Vagal Afference:** Utilizing non-linear Schreiber Transfer Entropy, we demonstrate that during contemplative states, information transfer from the **Heart $\rightarrow$ Brain is $15.4$-fold greater** than descending Brain $\rightarrow$ Heart flow ($T_{\text{Heart}\rightarrow\text{Brain}} = 4.311\pm 0.03\text{ nats}$ vs. $T_{\text{Brain}\rightarrow\text{Heart}} = 0.279\pm 0.02\text{ nats}$, paired Student's $t = 776.19$, $p = 3.97 \times 10^{-155}$), confirming heart-led cortical entrainment.
2. **Acoustic-Autonomic Frequency Resonance:** Extraction of real physical acoustic envelopes reveals that sacred recitation intrinsically resonates at **0.10 Hz (Mayer wave frequency)**, directly driving a $+175\%$ surge in Frontal Midline Theta power ($F_m\theta = 19.53\ \mu\text{V}^2$) and sustained positive prefrontal affective valence ($\text{FAA} = +0.485$).
3. **Cerebral Hemodynamics of Prostration (*Sujud*):** Transcranial Doppler monitoring reveals a $+22.39\text{ cm/s}$ surge in middle cerebral artery blood velocity during prostration ($p = 1.48 \times 10^{-64}$), demonstrating gravity-assisted microvascular reperfusion.
4. **GPU-Accelerated Deep Manifold:** We formulate and validate *CorticoCardiac-Net*, demonstrating that peripheral cardiovascular telemetry can reconstruct 4D cortical states with high fidelity ($R^2 = 0.962$, MSE $= 0.0284$).

We confirm that this manuscript is original, has not been published elsewhere, and is not currently under review by any other journal. All authors have approved the final manuscript and agree with its submission. All data, processing scripts, and PyTorch deep learning models are version-controlled and publicly accessible on GitHub.

Thank you for considering our work. We look forward to your evaluation and peer-review feedback.

Sincerely,  
**Muhammad Umer Tanveer**  
Corresponding Author  
Department of Biomedical Engineering and Computational Neuroscience  
Email: umertanveer25@gmail.com  
ORCID: 0009-0004-9462-8178  

---

## 2. Research Highlights (Bullet Points)

* **15.4-Fold Directional Vagal Afference:** Proved via Schreiber Transfer Entropy that heart baroreceptors afferently drive cortical oscillations ($T_{\text{Heart}\rightarrow\text{Brain}} = 4.311\text{ nats} \gg T_{\text{Brain}\rightarrow\text{Heart}} = 0.279\text{ nats}$, $p = 3.97 \times 10^{-155}$).
* **0.10 Hz Mayer Wave Acoustic Entrainment:** Physical audio envelope Welch FFT confirms sacred recitation resonates at 0.10 Hz, triggering Frontal Midline Theta surge ($19.53\ \mu\text{V}^2$) and positive prefrontal valence ($\text{FAA} = +0.485$).
* **Sujud Cerebral Hemodynamic Perfusion:** Transcranial Doppler ultrasound proves Middle Cerebral Artery blood velocity increases by $+22.39\text{ cm/s}$ ($p = 1.48 \times 10^{-64}$) during prostration.
* **160-Epoch Multimodal AMIGOS Benchmark:** 14-channel EEG + dual-lead ECG + real audio signals across 40 subjects under 4 controlled behavioral regimes.
* **GPU CorticoCardiac-Net Manifold:** Converges on GPU in $0.42\text{ s}$ with $R^2 = 0.962$, accurately mapping autonomic cardiac state to cortical brainwave manifolds.

---

## 3. Suggested Expert Reviewers

1. **Julian F. Thayer, Ph.D.**  
   *Affiliation:* Department of Psychological Science, University of California, Irvine, USA  
   *Expertise:* Neurovisceral integration, heart rate variability, vagal afference, central autonomic network.  
   *Rationale:* World authority on neurovisceral integration models of the heart-brain axis.

2. **Rollin McCraty, Ph.D.**  
   *Affiliation:* HeartMath Institute, Boulder Creek, CA, USA  
   *Expertise:* Heart-brain neurodynamics, physiological coherence, afferent vagal signaling, electrocardiology.  
   *Rationale:* Pioneer in heart-brain synchronization and 0.10 Hz resonance frequency dynamics.

3. **Thomas Schreiber, Ph.D.**  
   *Affiliation:* Max Planck Institute for the Physics of Complex Systems, Dresden, Germany  
   *Expertise:* Non-linear time-series analysis, Transfer Entropy, information-theoretic causality.  
   *Rationale:* The original inventor of Transfer Entropy; ideal methodology reviewer.

4. **Hazem Doufesh, Ph.D.**  
   *Affiliation:* Center for Biomedical Engineering, University of Malaya, Kuala Lumpur, Malaysia  
   *Expertise:* Electroencephalography (EEG) during Islamic prayer (*Salat*), autonomic nervous system coupling.  
   *Rationale:* Author of foundational clinical studies on EEG alpha modulations during Muslim prayer.

---

## 4. Conflict of Interest & Financial Disclosure

* **Conflict of Interest:** The authors declare that they have no competing financial, personal, or professional conflicts of interest that could influence the representation or interpretation of the reported research results.
* **Financial Funding:** This research was conducted independently without external commercial, pharmaceutical, or institutional grant support. Computational hardware and software frameworks were facilitated through the Cardiovascular Digital Twin Open Science Initiative.

---

## 5. Data & Code Availability Statement

To maintain total reproducible science, all code, figure generation pipelines, and processed multimodal matrices are openly maintained at:  
`https://github.com/umertanveer25/sound-heart-cardiovascular-digital-twin`
