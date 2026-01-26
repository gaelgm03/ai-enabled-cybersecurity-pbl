# Ethical analysis of the vulnerability scanner
The development of an automatic software vulnerability scanner involves very real risks, but the upside far outweights its potential harms. First, we will address the potential risks and malicious uses of these technologies, and then we will compare them to their benefits.

## Negative ethical aspects
- It could be used to systematically find vulnerabilities faster than they can be patched. If the technology became widely available, it could lead to a steep spike in attacks, at least in the short term.
- There is the possibility of false positives. Over-reliance on vulnerability reports can lead to unnecessary panic and/or system shutdowns, causing interruption of services to the general public. It is important not to blindly trust the scanner in order to avoid these incidents.
- In case of an incident, who assumes responsibility? The scanner is not a legal entity and cannot be held liable. Is the developer liable? Is the deployer? It is important to establish a framework that allows for determining who is responsible in case the tool misses a vulnerability, gives a false positive, or is used with malicious intent.
- If the tool is trained using proprietary or sensitive software, there could be risks of intellectual property leakage and misuse. It is necessary to implement regulations and security measures to avoid unauthorized access to sensitive information.
- The final, fully functional version could not be open-source because it would empower wrongdoers, but at the same time making it private could cause inequality in the security of systems, because those legitimate users without access to the tool would be at a disadvantage.

## Positive aspects
- The early detection of vulnerabilities can reduce the risk of data breaches and other types of attacks. This improves general security not only for companies, but also for end users, reducing the likelihood of their personal data being released or their services being interrupted.
- If developed correctly, the tool could be made available to small and medium-sized companies. This reduces inequality in protection and makes security measures available to companies that were previously unable to afford them.
- The scanner reduces human error in the analysis of software vulnerabilities. An automated scanner could go through more lines of code, in less time, and in more depth than a human could, making code review faster, cheaper, and more reliable. This does not erase the need for human intervention, because, as stated before, responsibility and supervision will always be requirements for these kinds of instruments, but it does reduce the amount of human hours necessary to keep applications safe.
- If implemented by an independent organization, it would allow for ethical and responsible disclosure of vulnerabilities, meaning that the developers of applications could be informed of the scanner’s findings and be able to patch them before they are exploited.
- History favors these kinds of instruments. Antivirus software and spam filters are both dual use technologies that are now widely accepted by society.
- Restraint from the defensive side does not prevent attackers from innovating; the tool we are talking about could very well be developed by malicious individuals, and not designing it as a defensive mechanism could leave companies — and clients — at a disadvantage.

## Conclusion
Although it has potential for misuse, there are many benefits to this technology that cannot be ignored. There are ways to reduce the risks with regulations, security measures, and responsible disclosure policies so that the tool can fulfil its purpose with minimal downsides. It is also important to control access to the instrument instead of making it public and to implement responsible disclosure procedures. This means that vulnerabilities found should not be made public until they have been patched by developers. Finally, human oversight should always be a part of the process in order to avoid malfuncion and to assign responsibility.

## References
1. Christen, M., Gordijn, B., & Loi, M. (2020). The Ethics of Cybersecurity (1st ed., Vol. 21, pp. 45–69). Springer Open. https://library.oapen.org/viewer/web/viewer.html?file=/bitstream/handle/20.500.12657/22489/1007696.pdf?sequence=1&isAllowed=y
2. Flechais, I., & Chalhoub, G. (2023). Practical Cybersecurity Ethics: Mapping CyBOK to Ethical Concerns. CyBOK. NSPW ’23, Segovia, Spain. https://www.cybok.org/media/downloads/PracticalCybersecurityEthics_MappingCyBOKtoEthicalConcerns.pdf
3. Miller, S., & Selgelid, M. J. (2007, December 1). Ethical and Philosophical Consideration of the Dual-use Dilemma in the Biological Sciences. National Library of Medicine; National Institute of Health. https://pmc.ncbi.nlm.nih.gov/articles/PMC7089176/
4. Wehing, B., & Qiushi, W. (2023). Towards More Effective Responsible Disclosure for Vulnerability Research. NDSS Symposium. Workshop on Ethics in Computer Security (EthiCS), San Diego, CA, USA. https://www.ndss-symposium.org/wp-content/uploads/2023/02/ethics2023-235691-paper.pdf
