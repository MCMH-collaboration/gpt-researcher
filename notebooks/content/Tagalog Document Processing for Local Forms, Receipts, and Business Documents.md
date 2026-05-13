# Revolutionizing Tagalog Document Processing for Local Forms, Receipts, and Business Documents in the Philippines

The digital transformation sweeping across industries globally presents both immense opportunities and unique challenges, particularly in regions with linguistically diverse and under-resourced languages. In the Philippines, the need for efficient and accurate **Tagalog Document Processing for Local Forms, Receipts, and Business Documents** is more critical than ever. While large language models (LLMs) have demonstrated remarkable capabilities for high-resource languages like English, the linguistic nuances of Filipino, including its complex morphology, syntax, and the widespread phenomenon of Taglish code-switching, often remain unexplored and underserved. This article delves into the specific hurdles faced by Philippine businesses and government agencies in managing their document workflows and introduces how advanced Intelligent Document Processing (IDP) solutions, such as DocumentLens, are poised to revolutionize this landscape, offering culturally and linguistically faithful automation.

## The Unique Landscape of Document Processing in the Philippines: Challenges and Opportunities

The Philippines is undergoing a significant digital renaissance, with government agencies modernizing permit systems and fintechs transforming loan approvals. This shift underscores the growing importance of efficient document processing. However, this transformation is not without its complexities, especially when dealing with the national language, Filipino, and its common variant, Taglish.

### Filipino as an Under-Resourced Language in NLP

Despite being the national language of the Philippines and spoken by over 80 million people, Filipino remains an under-resourced language in the realm of Natural Language Processing (NLP) ([Source: aclanthology.org/2025.acl-long.1509.pdf]). This under-representation in multilingual LLMs and NLP research leads to significant performance gaps when these generic models attempt to process Filipino text. Existing corpora for Filipino are often domain-specific, non-multilingual, and, critically, have been created by non-native speakers, leading to a pervasive "translationese bias" ([Source: aclanthology.org/2025.acl-long.1509.pdf], [Source: arxiv.org/html/2502.14911v1]). This bias means that the language data available for training models does not accurately reflect the fluency and authenticity of how native speakers use Filipino, hindering the development of robust NLP applications.

The challenge is further compounded by the unique hurdles in modeling Filipino's rich morphology and construction. Filipino, an Austronesian language, possesses complex morphological and syntactic structures that differ significantly from higher-resourced languages. These linguistic intricacies require explicit Filipino language support and instruction tuning for LLMs to truly understand, reason, and generate content in a way that is natural and accurate for native speakers ([Source: arxiv.org/html/2502.14911v1], [Source: aclanthology.org/2025.acl-long.1509.pdf]). The lack of such specialized training means that generic NLP tools often misinterpret or fail to process Filipino documents effectively, leading to errors and inefficiencies in business operations.

### The Complexity of Taglish (Code-Switching)

One of the most distinctive features of language use in the Philippines is the widespread phenomenon of Tagalog-English code-switching, commonly known as Taglish. This linguistic dance, where conversations effortlessly bounce between Filipino and English—sometimes mid-sentence, mid-thought, or even mid-syllable—is not evidence of linguistic incompetence or "broken English" ([Source: veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/]). On the contrary, Taglish is a sophisticated communication system that mirrors identity, class dynamics, humor, and emotional nuance within Filipino society ([Source: veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/]). It thrives in contexts where English carries prestige and modernity, while Filipino grounds speech in familiarity and emotional authenticity, allowing speakers to calibrate tone, distance, authority, or intimacy on the fly ([Source: veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/]).

For document processing, Taglish presents a significant "localization minefield" ([Source: veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/]). Traditional NLP techniques, largely trained on monolingual datasets, tend to perform poorly on mixed-language data ([Source: aclanthology.org/2022.lrec-1.225.pdf]). This challenge is particularly acute for tasks like sentiment analysis, where code-switching and code-mixing can degrade performance significantly, with F1-scores dropping by around 9% for LLMs across review and sentence levels ([Source: ieeexplore.ieee.org/document/11336084/]). Direct translation of Taglish often results in a loss of tone, context, and personality, stripping documents of their sociolinguistic authenticity ([Source: veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/]). Therefore, any effective **Tagalog Document Processing for Local Forms, Receipts, and Business Documents** must possess adequate knowledge of the idiosyncrasies common to Taglish code-switching ([Source: aclanthology.org/2022.lrec-1.225.pdf]).

### The Pervasive "Translationese Bias" and Linguistic Hurdles

As highlighted by the Batayan benchmark, a holistic Filipino NLP benchmark designed to systematically evaluate LLMs, existing Filipino corpora suffer from a pervasive "translationese bias" ([Source: arxiv.org/html/2502.14911v1], [Source: aclanthology.org/2025.acl-long.1509.pdf]). This bias arises when data is primarily generated through translation from other languages, rather than being organically created by native speakers. The result is a corpus that, while technically in Filipino, lacks the natural flow, idiomatic expressions, and authentic linguistic structures that native speakers would use. This significantly impairs the ability of NLP models trained on such data to truly understand and generate fluent Filipino.

To counteract this, Batayan emphasizes a rigorous, native-speaker-driven annotation process to ensure fluency and authenticity to the complex morphological and syntactic structures of Filipino ([Source: arxiv.org/html/2502.14911v1], [Source: aclanthology.org/2025.acl-long.1509.pdf]). This approach is crucial for building culturally and linguistically-faithful resources in under-represented languages. Without such meticulous data curation, NLP models will continue to struggle with the unique hurdles in modeling Filipino's rich morphology and construction, leading to suboptimal performance in real-world applications.

### The Growing Need for Specialized Document Intelligence

The imperative for efficient document processing in the Philippines is driven by several high stakes:
*   **Efficiency:** Manual processes significantly slow down critical turnaround times, impacting everything from loan approvals to government services ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **Cost:** Labor-intensive workflows drive up operational expenses, making businesses less competitive ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **Compliance:** Regulatory standards demand traceability and audit readiness, especially with evolving frameworks like e-invoicing ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **Fraud Prevention:** Data integrity is non-negotiable in sectors like finance and healthcare, where accurate document processing is key to preventing fraud ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).

Philippine small and medium enterprises (SMEs) are particularly affected. While 77% are eager to adopt digital tools, only 16% currently use them, primarily due to a lack of skills, perceived complexity, and affordability ([Source: business.inquirer.net/574542/the-sme-investment-paradox-how-to-grow-while-cutting-costs-in-2026]). However, the benefits are clear: 69% of Filipino SMEs that invested in technology in 2024 reported improved profitability ([Source: business.inquirer.net/574542/the-sme-investment-paradox-how-to-grow-while-cutting-costs-in-2026]). This creates a strategic paradox: digital investment is critical, yet SMEs are under pressure to cut costs ([Source: map.org.ph/the-sme-investment-paradox-how-to-grow-wzhile-cutting-costs-in-2026/]).

Government initiatives further underscore this urgency. The Philippines' e-invoicing and e-reporting mandate, with a mandatory go-live date of January 1, 2027, for Phase 1 taxpayers, signifies a profound shift towards a digital tax ecosystem ([Source: vatupdate.com/2026/03/07/briefing-document-podcast-philippines-e-invoicing-and-e-reporting/]). While micro-enterprises are initially exempt and SMEs will be included in later phases (likely after 2027), they face upfront costs for software/hardware upgrades, IT integration, and staff training ([Source: vatupdate.com/2026/03/07/briefing-document-podcast-philippines-e-invoicing-and-e-reporting/]). This necessitates solutions that can handle specific local documents such as:
*   **BIR-related documents:** Tax forms, compliance reports.
*   **Barangay clearances:** Essential local government documents.
*   **Bank statements and loan forms:** Critical for financial institutions.
*   **Invoices and receipts:** Daily business transactions.
*   **Identity documents:** For KYC (Know Your Customer) compliance.
*   **Medical records:** For healthcare document processing.

In this environment, document intelligence is no longer optional; it is essential for resilience, compliance, and customer trust ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).

## Beyond Generic OCR: The Power of Intelligent Document Processing (IDP)

Traditional Optical Character Recognition (OCR) has been a foundational technology for converting scanned documents into editable text. However, its limitations become glaringly apparent when confronted with the complexities of Philippine documents.

### Limitations of Traditional OCR for Philippine Documents

Generic OCR solutions, while effective for simple, structured documents in high-resource languages, often fall short when dealing with the unique characteristics of documents in the Philippines. These limitations include:
*   **Lack of Contextual Awareness:** Generic OCR primarily focuses on character recognition without understanding the semantic context of the text. This means it struggles to accurately extract specific data fields from complex layouts, especially those found in local forms or receipts with varied structures.
*   **Poor Performance with Mixed Languages:** Traditional OCR is typically optimized for single-language documents. It cannot effectively handle code-switched Taglish utterances, leading to errors in recognition and data extraction when Filipino and English are intertwined within a single document or even a single sentence ([Source: aclanthology.org/2022.lrec-1.225.pdf]).
*   **Inability to Handle Linguistic Nuances:** The rich morphology and syntax of Filipino, along with regional wording variations, are often beyond the capabilities of generic OCR. It cannot account for the "translationese bias" prevalent in many existing datasets, resulting in inaccurate or unnatural interpretations.
*   **Challenges with Unstructured and Semi-structured Data:** Many local forms, receipts, and business documents are semi-structured or entirely unstructured. Generic OCR struggles to identify and categorize information from these varied formats, requiring extensive manual post-processing.
*   **Limited Support for Handwritten Text:** While some advanced OCR offers handwritten text recognition, generic solutions often fail to accurately process handwritten entries common in many Philippine forms and receipts ([Source: evolutiontech.ae/document-intelligence.html]).

These limitations lead to increased manual intervention, higher operational costs, slower processing times, and a greater risk of errors, undermining the very goal of automation.

### What is Intelligent Document Processing (IDP)?

Intelligent Document Processing (IDP) emerges as a transformative solution, moving beyond the capabilities of traditional OCR. IDP is an AI-enabled solution that automates document data extraction and structuring for various document types, including invoices, contracts, and receipts, significantly increasing efficiency while reducing manual effort and errors ([Source: precedenceresearch.com/intelligent-document-processing-market]).

At its core, IDP leverages a combination of advanced technologies:
*   **AI-powered Optical Character Recognition (OCR):** Far more sophisticated than traditional OCR, AI-OCR can handle complex layouts, varied fonts, and even handwritten text with high accuracy ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines], [Source: evolutiontech.ae/document-intelligence.html]).
*   **Natural Language Processing (NLP):** NLP enables IDP to understand the meaning and context of the text, not just recognize characters. This is crucial for handling linguistic nuances, identifying key entities, and processing mixed-language content like Taglish ([Source: precedenceresearch.com/intelligent-document-processing-market]).
*   **Machine Learning (ML):** ML algorithms allow IDP systems to learn from data, continuously improving their accuracy and adaptability over time. This includes document classification, data validation, and anomaly detection ([Source: precedenceresearch.com/intelligent-document-processing-market]).

By converging these technologies, IDP transforms unstructured and semi-structured documents into structured, actionable data, making it a foundational pillar of enterprise digital transformation ([Source: precedenceresearch.com/intelligent-document-processing-market]).

### Key Benefits of IDP for Philippine Businesses

The adoption of IDP offers compelling advantages for businesses operating in the Philippines, directly addressing the challenges outlined earlier:

*   **Enhanced Accuracy and Reduced Errors:** IDP significantly improves data extraction accuracy, minimizing human error inherent in manual processes. Solutions boast industry-leading OCR accuracy, with some claiming up to 99.8% accuracy with multi-language support ([Source: evolutiontech.ae/document-intelligence.html], [Source: precedenceresearch.com/intelligent-document-processing-market]).
*   **Increased Efficiency and Speed:** IDP automates repetitive tasks, allowing businesses to process thousands of documents in seconds with parallel processing ([Source: evolutiontech.ae/document-intelligence.html]). This dramatically speeds up workflows; for instance, some IDP platforms can cut bank-statement processing time from days to under a minute ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]). Expect up to 300x faster processing and ~70% reduction in manual effort ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **Cost Reduction:** By automating manual work, IDP reduces operational expenses. Businesses can expect to reduce expenses by up to 92% and manage resources more efficiently, allowing employees to focus on more valuable tasks ([Source: voiser.ai/ai-transcribe/filipino-philippines-speech-to-text]).
*   **Improved Compliance and Security:** IDP solutions are designed with bank-level security, encryption, and compliance frameworks (e.g., ISO-27001, GDPR) built-in, ensuring data privacy and auditability from day one ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines], [Source: evolutiontech.ae/document-intelligence.html]). This is crucial for navigating the Philippines' evolving regulatory landscape.
*   **Seamless Integration:** Cloud-native, API-first IDP platforms offer seamless integration with existing business systems such as CRMs, ERPs, and banking systems, removing barriers to digital adoption ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines], [Source: evolutiontech.ae/document-intelligence.html]).
*   **Strategic Advantage:** Automating document processing allows businesses to refocus existing resources from routine tasks to game-changing strategies, increasing competitiveness and enabling deep market intelligence ([Source: precedenceresearch.com/intelligent-document-processing-market], [Source: business.inquirer.net/574542/the-sme-investment-paradox-how-to-grow-while-cutting-costs-in-2026]).

### IDP in Action: Examples from the Philippines

The impact of IDP is already being felt in the Philippines. Mindox, for example, is a cloud-native IDP platform purpose-built for emerging markets like the Philippines ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]). It has demonstrated tangible results:
*   **Financial Institutions:** Mindox cuts bank-statement processing time from days to under a minute—50 seconds for multi-page statements, and just 5 seconds for one-page documents like barangay clearances ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **SME Loan Approvals:** Organizations like Unicapital Philippines use Mindox to improve credit analysis workflows, accelerate SME loan approvals, and ensure compliance with local data requirements ([Source: andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines]).
*   **Diverse Applications:** IDP is transforming document management across various sectors, including invoice processing, accounts payable automation, identity document verification (KYC compliance), and medical records processing ([Source: evolutiontech.ae/document-intelligence.html]).

These real-world applications underscore the transformative potential of IDP in addressing the unique document processing needs of the Philippines.

## DocumentLens: The Future of Tagalog Document Processing for Local Forms, Receipts, and Business Documents

In a market demanding specialized solutions, DocumentLens emerges as a powerful, tailored platform designed to meet the specific needs of **Tagalog Document Processing for Local Forms, Receipts, and Business Documents**. By integrating cutting-edge AI-OCR and NLP capabilities with a deep understanding of Philippine linguistic and cultural contexts, DocumentLens provides an unparalleled solution for businesses navigating the complexities of their document workflows.

### Bridging the Linguistic Gap with Advanced Tagalog OCR and NLP

DocumentLens is engineered from the ground up to address the linguistic challenges inherent in Filipino documents. Its core strength lies in its advanced **Tagalog OCR** capabilities, specifically designed to process not only pure Tagalog but also the ubiquitous Taglish code-switching with high accuracy.

*   **Addressing Morphological and Syntactic Complexities:** Unlike generic OCR, DocumentLens's underlying NLP models are trained to understand the intricate morphological and syntactic structures of Filipino. This means it can correctly interpret word conjugations, affixes, and sentence constructions that are unique to the language, ensuring that the extracted text is not just a collection of characters but meaningful linguistic units.
*   **Overcoming Translationese Bias:** DocumentLens leverages datasets that are meticulously curated through native-speaker-driven annotation processes, similar to the principles advocated by the Batayan benchmark ([Source: arxiv.org/html/2502.14911v1]). This ensures that its models are trained on culturally and linguistically-faithful resources, alleviating the pervasive translationese bias found in many existing Filipino corpora. The result is a system that processes documents with the fluency and authenticity of a native speaker.
*   **Seamless Multilingual OCR Philippines Support:** The platform offers robust **multilingual OCR Philippines** support, allowing it to seamlessly handle documents that mix Tagalog and English. It intelligently identifies language segments within a sentence or document, applying the appropriate linguistic rules for each, thereby preserving the original intent and nuance of code-switched content. This capability is crucial for accurately processing the diverse range of business communications in the Philippines, where Taglish is a standard mode of discourse.

By focusing on these specific linguistic challenges, DocumentLens ensures that businesses can automate the processing of their Tagalog and Taglish documents without sacrificing accuracy or contextual understanding.

### Pre-trained for Philippine Document Intelligence

A key differentiator for DocumentLens is its specialized training on a vast array of regional document types, making it a true **Philippine document AI** solution. This pre-training allows it to possess an inherent contextual understanding of local forms, receipts, invoices, and government-related documents.

*   **Contextual Understanding of Regional Wording and Layouts:** DocumentLens is not just a generic OCR; it's an intelligent system that understands the typical layouts, terminology, and data fields specific to Philippine documents. This includes:
    *   **BIR Forms OCR:** It is pre-trained to recognize and accurately extract data from various Bureau of Internal Revenue (BIR) forms, which are critical for tax compliance and financial reporting in the Philippines. This significantly reduces the manual effort and potential for errors associated with processing these complex government documents.
    *   **Barangay Clearances and Local Government Forms:** The platform is equipped to handle official documents issued by local government units, understanding their specific structures and data requirements.
    *   **Loan Applications and Financial Documents:** For the financial sector, DocumentLens can process diverse loan forms, bank statements, and other financial records, extracting key information for credit analysis and approval workflows.
    *   **Commercial Invoices and Official Receipts:** It accurately captures line items, totals, dates, and other critical information from commercial invoices and official receipts, streamlining accounts payable and reconciliation processes.
    *   **Identity Documents and KYC Forms:** DocumentLens facilitates faster and more accurate identity verification by extracting data from various IDs and KYC forms, crucial for compliance in banking and other regulated industries.
*   **Adaptability to Local Nuances:** The system's pre-training extends to understanding regional variations in terminology and common abbreviations, ensuring that it can interpret documents from different parts of the archipelago with high fidelity. This deep local knowledge makes DocumentLens exceptionally reliable for Philippine document workflows.

This specialized intelligence means that DocumentLens can be deployed rapidly and effectively, requiring minimal customization for common Philippine document types, thereby accelerating the return on investment for businesses.

### Structured Data Extraction with Layout Preservation

Beyond simply recognizing text, DocumentLens excels at transforming unstructured and semi-structured documents into highly organized, actionable data while maintaining crucial traceability.

*   **Accurate Extraction of Key Fields:** DocumentLens utilizes advanced AI and ML algorithms to identify and extract specific data fields from even the most complex documents. Whether it's a customer's name and address from a utility bill, line item details from an invoice, or specific declarations from a government form, the system precisely isolates and categorizes this information. This capability is vital for automating data entry into ERP, CRM, and other business systems.
*   **Preservation of Original Document Layout:** For auditability and compliance, it's often critical to not only extract data but also to understand its original context within the document. DocumentLens preserves the layout and source traceability of the processed documents. This means that users can easily cross-reference extracted data with its original location on the document, providing a clear audit trail and enhancing trust in the automated process. This feature is particularly valuable in regulated industries where data integrity and verification are paramount.
*   **Ensuring Data Integrity for Compliance and Decision-Making:** By providing structured, validated data with full traceability, DocumentLens helps businesses meet stringent regulatory compliance requirements. The high accuracy of extraction minimizes errors that could lead to non-compliance or flawed business decisions, empowering organizations with reliable information for strategic planning and operational efficiency.

### Empowering Philippine Businesses with DocumentLens

DocumentLens is more than just a tool; it's a strategic enabler for Philippine businesses seeking to thrive in the digital age. By addressing the specific challenges of **Tagalog Document Processing for Local Forms, Receipts, and Business Documents**, it delivers tangible benefits across various sectors:

*   **Streamlined Workflows:** From finance and human resources to logistics and government services, DocumentLens automates document-intensive processes, eliminating manual bottlenecks and accelerating operational rhythms. This includes invoice processing automation, employee onboarding, and public records management ([Source: hyland.com/en/resources/articles/idp-use-cases]).
*   **Accelerated Processes:** Critical business functions like loan approvals, KYC verification, and contract reviews are significantly sped up, leading to faster customer service and improved market responsiveness.
*   **Reduced Manual Effort and Human Error:** By automating data extraction and validation, DocumentLens drastically cuts down on manual data entry, reducing labor costs and minimizing the potential for human errors that can be costly and time-consuming to rectify.
*   **Actionable Insights from Locked Data:** Previously trapped in unstructured documents, valuable data can now be extracted, structured, and analyzed, providing businesses with deeper insights into their operations, customers, and market trends. This supports data-driven decision-making and fosters innovation.
*   **Digital Competitiveness in Southeast Asia Document AI:** By adopting DocumentLens, Philippine businesses position themselves at the forefront of **Southeast Asia document AI**. This not only enhances their local competitiveness but also prepares them for broader regional and global integration, leveraging advanced technology to overcome linguistic and operational barriers.

In essence, DocumentLens offers a comprehensive, intelligent, and locally-attuned solution that empowers Philippine enterprises to unlock the full potential of their document-driven processes, driving efficiency, compliance, and growth.

## Conclusion: Embracing Specialized Tagalog Document Processing for a Digital Future

The journey towards comprehensive digital transformation in the Philippines hinges significantly on the ability to efficiently and accurately process the vast volumes of local documents. Generic NLP and OCR solutions, while powerful in other contexts, consistently fall short when confronted with the unique linguistic complexities of Filipino, the pervasive nature of Taglish code-switching, and the specific formats of local forms, receipts, and business documents. The "translationese bias" and the intricate morphological and syntactic structures of Filipino demand a specialized approach—one that is culturally and linguistically faithful.

The rise of Intelligent Document Processing (IDP) marks a pivotal shift, moving beyond simple character recognition to contextual understanding and structured data extraction. Solutions like DocumentLens are at the forefront of this revolution, offering a purpose-built platform for **Tagalog Document Processing for Local Forms, Receipts, and Business Documents**. By providing advanced **Tagalog OCR** capabilities, comprehensive **multilingual OCR Philippines** support, and pre-training on diverse **Philippine document AI** including **BIR forms OCR**, DocumentLens directly addresses the critical needs of the market. It ensures high accuracy, preserves document integrity, and seamlessly integrates into existing workflows, transforming operational bottlenecks into strategic advantages.

For Philippine businesses, embracing such specialized IDP solutions is no longer a luxury but a necessity. It is the key to unlocking efficiency, ensuring compliance, reducing costs, and ultimately, securing a competitive edge in the rapidly digitizing economy of **Southeast Asia document AI**. The future of document processing in the Philippines is intelligent, localized, and powered by solutions that truly understand the language and its context.

---

## References

*   https://arxiv.org/html/2502.14911v1
*   https://aclanthology.org/2025.acl-long.1509.pdf
*   https://aclanthology.org/2022.lrec-1.225.pdf
*   https://ieeexplore.ieee.org/document/11336084/
*   https://veqta.com/the-code-switching-paradox-why-taglish-isnt-broken-english-but-a-localization-minefield/
*   https://andsolutions.net/blog/document-processing-trends-and-innovations-in-philippines
*   https://map.org.ph/the-sme-investment-paradox-how-to-grow-wzhile-cutting-costs-in-2026/
*   https://business.inquirer.net/574542/the-sme-investment-paradox-how-to-grow-while-cutting-costs-in-2026
*   https://vatupdate.com/2026/03/07/briefing-document-podcast-philippines-e-invoicing-and-e-reporting/
*   https://precedenceresearch.com/intelligent-document-processing-market
*   https://evolutiontech.ae/document-intelligence.html
*   https://voiser.ai/ai-transcribe/filipino-philippines-speech-to-text
*   https://hyland.com/en/resources/articles/idp-use-cases