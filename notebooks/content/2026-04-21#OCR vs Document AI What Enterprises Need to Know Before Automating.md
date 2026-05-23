# OCR vs Document AI: What Enterprises Need to Know Before Automating

In 2026, the landscape of document processing has evolved dramatically. For enterprises looking to automate their workflows, understanding the fundamental differences between traditional Optical Character Recognition (OCR) and advanced Document AI is no longer optional – it's critical. The choice between **OCR vs Document AI** dictates not just efficiency, but also accuracy, compliance, and the ability to truly transform operations. This article delves into what each technology offers, where traditional OCR falls short, and why **intelligent document processing** is becoming the default for forward-thinking organizations.

## The Foundation: What Traditional OCR Does Well

Optical Character Recognition (OCR) has been the bedrock of document digitization for decades. At its core, OCR technology converts different types of documents, such as scanned paper documents, PDFs, or images, into editable and searchable data. It's the technology that enables machines to "read" text from an image.

### Basic Text Extraction and Digitization

Traditional OCR excels at its primary function: character recognition. When presented with clean, typed documents, it can achieve high accuracy rates, often quoted between 95-98% for simple, printed text ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)). This capability was, and still is, revolutionary for converting physical archives into digital formats, making them searchable and accessible. For instance, digitizing old contracts or books to create searchable PDFs is a classic **OCR use case**.

### When OCR is Sufficient (Simple, Clean Documents)

For tasks that primarily involve converting static images of text into machine-readable text without needing to understand context, structure, or relationships, traditional OCR can be sufficient. This includes:
*   **Simple text digitization:** Converting a scanned document into a text file for basic searchability.
*   **Clean, structured forms:** If documents have a highly consistent layout and clear, typed fields, OCR can extract data points with reasonable success, often with the aid of templates or fixed rules ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88434b3a16a)).
*   **Low-stakes data capture:** Where the cost of manual review for errors is minimal or the data itself is not critical for downstream decision-making.

In these scenarios, OCR provides essential improvements in speed and accessibility, laying the groundwork for further digital processes ([source](https://celestialsys.com/blogs/beyond-ocr-financial-compliance/)).

## Beyond the Basics: Where Traditional OCR Falls Short

While foundational, traditional OCR has significant limitations that prevent it from meeting the demands of modern enterprise automation. In 2026, simply extracting text is "stopping halfway" ([source](https://ticnote.com/en/blog/ai-document-automation-tools)). The shift is from basic recognition to deep understanding ([source](https://celestialsys.com/blogs/beyond-ocr-financial-compliance/)).

### The "Error Cascade" and Hidden Inefficiencies

Most organizations might quote an OCR accuracy rate of 95-98% for simple, printed text. However, this figure is misleading in real-world production environments. A mere two percent character error rate can quickly multiply through multiple post-processing steps, leading to 15-20% information extraction errors ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)). This "error cascade" means that one in five documents often requires human intervention, with these hidden inefficiencies leading to substantial costs, compliance exposure, and slower turnaround times ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)).

Traditional OCR operates through a "fragile multi-step pipeline: OCR → Text Cleaning → NLP → Extraction," where each step introduces opportunities for new errors that compound downstream. The result is a process demanding constant oversight and frequent manual correction ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)).

### Struggling with Structure and Layout

One of the most critical **OCR limitations** is its inability to understand document structure and layout. OCR typically outputs text in reading order, losing vital information about how elements are visually organized ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).
*   **Tables and Forms:** In documents like bank statements or invoices, amounts appear in tables with rows and columns. Traditional OCR extracts all numbers but cannot discern which is a subtotal, tax, or final total without rigid templates ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)). It requires templates or heuristics, which are brittle to layout changes ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Complex Layouts:** For documents with complex layouts, such as legal contracts or insurance claims, OCR struggles to identify section headers, formatting, or the significance of signatures, as it lacks visual context ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).

### The Challenge of Context and Meaning

Traditional OCR is a character-recognition system; it does not inherently understand the meaning or context of the text it extracts. It cannot answer higher-level questions like, "Is this number a subtotal or the final payable amount?" ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)). This gap between extraction and understanding is where it fundamentally falls short ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genAI-enhances-modern-ocr-workflows-b88343b3a16a)).

For example, in invoice processing, OCR might read "T0tal Am0unt" instead of "Total Amount" or "1O00" instead of "1000." It lacks the contextual reasoning to correct these common errors automatically ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).

### Limitations with Complex Document Types (Handwriting, Tables, Noisy Scans)

Real-world documents are often messy, inconsistent, and unstructured, posing significant challenges for traditional OCR:
*   **Handwritten Content:** Due to inconsistent writing styles, handwritten documents have always been difficult for OCR engines. Traditional OCR struggles, often producing high error rates or unusable output ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Noisy/Low-Quality Scans:** Accuracy drops significantly when OCR encounters noisy, low-contrast, faded, or blurred text ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Multilingual Documents:** While some OCR tools offer multilingual support, handling diverse languages and regional formats consistently can be a hurdle without deeper understanding.
*   **Ambiguity and Variations:** Financial documents, for instance, often contain specialized terminology, industry jargon, and context-dependent language that traditional OCR struggles to process correctly. Its reliance on fixed rules and templates means it cannot adapt to variations in document content or layout, which are common due to evolving regulations or corporate practices ([source](https://www.techrxiv.org/doi/10.36227/techrxiv.172651542.23422356)).

### Inflexibility and Compliance Risks

Traditional OCR systems require manual updates and constant monitoring to adapt to new formats and regulations, making them less suitable for dynamic environments ([source](https://learn.microsoft.com/en-ca/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc)). In regulated industries, where accuracy is paramount, OCR's lack of validation mechanisms and confidence scores makes it difficult to ensure compliance. Errors can lead to severe consequences like fines or failed audits ([source](https://learn.microsoft.com/en-ca/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc)).

## The Evolution: What Document AI Brings to the Table

In 2026, **AI document processing vs traditional OCR** is not just an upgrade; it's a paradigm shift. Document AI, often encompassing Intelligent Document Processing (IDP) and Vision-Language Models (VLMs), moves beyond simple character recognition to contextual understanding, semantic reasoning, and actionable intelligence. It's about turning raw files—scans, PDFs, emails, and even meeting audio—into usable business output with less manual work ([source](https://ticnote.com/en/blog/ai-document-automation-tools)).

### From Reading to Understanding: Contextual and Semantic Reasoning

Generative AI (GenAI) is bridging the gap between OCR's extraction and true document understanding. It treats OCR output as raw input that can be corrected, interpreted, structured, and validated. By understanding language patterns and document context, GenAI can fix recognition errors, identify document structure, and infer the meaning of extracted text ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).
*   **Context-Aware Error Correction:** GenAI models understand that "Total Amount" is a standard financial term and that a monetary value like "1O00" is unlikely, automatically correcting such errors ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)). This leads to fewer manual reviews and higher straight-through processing rates.
*   **Handling Ambiguity:** Generative AI uses natural language processing (NLP) techniques to disambiguate text, recognize context-specific meanings, and adapt to different writing styles and formats, ensuring extracted information is accurate and contextually relevant ([source](https://www.techrxiv.org/doi/10.36227/techrxiv.172651542.23422356)).

### Advanced Layout Understanding and Multimodal Processing

Modern Document AI, particularly with Vision-Language Models (VLMs), processes images and language jointly. This allows it to use context to infer missing or unclear text, recover meaning even when characters are distorted, poorly scanned, or embedded in complex layouts ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Multimodal Understanding:** Documents are visual objects, not just text containers. VLMs understand layout and positioning, enabling them to answer queries like "Who signed this contract?" or "Where is the termination clause?" by interpreting visual cues alongside text ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).
*   **Robust to Noise:** VLMs can denoise and infer missing letters using context, maintaining high accuracy (e.g., ~90%+) even for historic or low-quality scans ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Handwriting Performance:** VLMs show strong performance on handwritten text, using context to interpret cursive writing, mixed content, and abbreviations, significantly outperforming traditional OCR ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).

### Structured Outputs and Workflow Integration

Document AI platforms don't just extract text; they generate structured data. They can infer table boundaries, column meanings, and relationships between fields, outputting structured data like invoice numbers, line items, and total payable amounts ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)). This structured output, often in JSON or XML, is crucial for seamless integration with ERP, CRM, and other business systems ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).

The value doesn't stop at the extracted field; workflow orchestration connects extraction outcomes to downstream system actions through native integrations and flexible APIs ([source](https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing)).

### Enhanced Accuracy and Human-in-the-Loop (HITL)

AI-driven document understanding combines machine learning, natural language processing (NLP), and computer vision to classify documents, extract data, and validate context ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)). This contextual understanding allows systems to distinguish similar data elements, detect anomalies, and apply business rules automatically, achieving extremely high accuracy rates and reducing processing costs ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)).

Crucially, "touchless" automation doesn't mean zero humans. It means standard cases finish end-to-end without edits, while exceptions route to review. Document AI platforms include confidence scores, validation rules, sampling, and human-in-the-loop (HITL) review queues with clear audit logs to manage exceptions and ensure accuracy and compliance ([source](https://ticnote.com/en/blog/ai-document-automation-tools)).

### Agentic Processing: Beyond Extraction to Action

A defining transition in 2026 is the move from "extract this field" to "understand this document and act on it" ([source](https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing)). Agentic document processing doesn't just pull data points; it reads context, cross-references related documents, flags anomalies, and routes decisions with a level of judgment that rules-based systems cannot replicate ([source](https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing)).

For example, an accounts payable team might see manual invoice review drop from 40% to 4%, not just because of improved extraction, but because the system understands vendor history, contract terms, and approval thresholds well enough to handle edge cases ([source](https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing)). This represents a shift from process automation to intelligent autonomy, where systems learn, adapt, and make judgment calls ([source](https://www.acldigital.com/blogs/top-6-enterprise-architecture-trends-shaping-2026-and-beyond)).

### Real-Time Decisioning and Scalability

Batch processing is a "2020 problem." By 2026, business operations demand document intelligence that operates at the speed of the transaction ([source](https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing)). Modern Document AI platforms support real-time ingestion and dynamic schema recognition, enabling documents to trigger workflows instantly. This allows enterprises to move from batch processing to real-time operational responsiveness, prioritizing time-sensitive documents like claims or compliance notices ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)).

Cloud-native and scalable architectures are becoming the default, supporting elastic processing capacity to handle seasonal spikes or unexpected volume surges without infrastructure bottlenecks ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)).

## Choosing Your Path: When OCR is Enough vs. When Document AI is Essential

The decision between OCR and Document AI hinges on the complexity of your documents, the criticality of the data, and the desired level of automation.

### Simple Digitization vs. Intelligent Automation

| Feature               | Traditional OCR                                     | Document AI (IDP/VLM)                                |
| :-------------------- | :-------------------------------------------------- | :--------------------------------------------------- |
| **Core Capability**   | Character recognition, text digitization            | Document understanding, contextual interpretation    |
| **Input Coverage**    | Scanned PDFs, clean images                          | Scanned PDFs, native PDFs, images, email, audio/video ([source](https://ticnote.com/en/blog/ai-document-automation-tools)) |
| **Document Types**    | Clean, structured forms, printed text               | Structured forms, narrative work, complex layouts, handwriting ([source](https://ticnote.com/en/blog/ai-document-automation-tools)) |
| **Output**            | Raw text, searchable PDFs                           | Extracted fields, JSON, workflow triggers, finished deliverables ([source](https://ticnote.com/en/blog/ai-document-automation-tools)) |
| **Accuracy (Complex)**| 40-60% on complex forms/tables ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)) | 65-75% on complex forms/tables, 85-95% on handwriting ([source](https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex)) |
| **Contextual Understanding** | Limited, rule-based                                 | High, semantic reasoning, layout-sensitive ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)) |
| **Error Correction**  | Manual review, post-processing                      | Context-aware, automated correction ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)) |
| **Integration**       | Basic text export                                   | Deep integration with ERP, CRM, RPA, cloud stacks ([source](https://ticnote.com/en/blog/ai-document-automation-tools)) |
| **Adaptability**      | Static, template-dependent                          | Dynamic, learns from data, adapts to new formats ([source](https://www.techrxiv.org/doi/10.36227/techrxiv.172651542.23422356)) |
| **Cost**              | Lower processing cost, higher manual review cost    | Higher compute/inference cost, significantly lower manual review cost ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)) |

**When OCR is Enough:** If your primary need is to convert clean, typed documents into searchable text, and the data is not highly complex or critical for automated decision-making, traditional OCR can still serve a purpose. It's suitable for bulk digitization where human review can easily catch errors.

**When Document AI is Essential:** For most enterprise operations in 2026, Document AI is no longer a luxury but a necessity. If your bottleneck is deliverables from conversations or extracting structured data at scale, Document AI is the clear choice ([source](https://ticnote.com/en/blog/ai-document-automation-tools)). It's required when:
*   You deal with complex, varied, or unstructured documents (invoices, contracts, claims, handwritten notes).
*   Accuracy, compliance, and auditability are critical (e.g., financial services, healthcare, legal).
*   You need to automate end-to-end workflows, not just data capture.
*   Real-time decision-making and scalability are crucial.
*   You need to extract meaning and context, not just characters.

### The Cost-Benefit Analysis

While traditional OCR is significantly cheaper and faster for basic tasks, the "total cost to operate" for Document AI includes setup time, template/training effort, monitoring, and exception handling. However, the savings from reduced manual review, faster processing, improved compliance, and the ability to automate complex decisions often far outweigh the higher upfront and operational costs of Document AI ([source](https://ticnote.com/en/blog/ai-document-automation-tools)). Draft generation alone can look fast—until QA eats the savings ([source](https://ticnote.com/en/blog/ai-document-automation-tools)).

### Strategic Advantage in 2026

In 2026, AI document automation isn't just OCR. The best stack either extracts fields into your systems or turns meetings plus mixed files into finished work outputs—or both ([source](https://ticnote.com/en/blog/ai-document-automation-tools)). Enterprises that invest in intelligent automation today are building the foundation needed to scale tomorrow. Competitive advantage will belong to those that transform documents into actionable intelligence, automate decision workflows, scale processing capacity without adding headcount, strengthen compliance, and enable real-time operational insight ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)).

## Introducing DocumentLens: Bridging the Gap for Enterprise Needs

For enterprises navigating the complexities of modern document automation, a solution like DocumentLens represents the cutting edge of **intelligent document processing**. It's designed to move businesses beyond the limitations of traditional OCR, delivering usable, structured data rather than just raw text.

### Layout Analysis and VLM-Powered Understanding

DocumentLens goes beyond simple character recognition by leveraging advanced Vision-Language Models (VLMs). This allows it to perform comprehensive layout analysis, understanding the visual structure of documents in addition to the text content. Unlike traditional OCR, which struggles with complex layouts, DocumentLens can interpret the spatial relationships between elements, recognizing sections, paragraphs, and the overall design intent of a document. This VLM-powered understanding enables it to infer meaning and context even from poorly scanned or visually challenging documents, maintaining high accuracy where conventional OCR would fail ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).

### Comprehensive Extraction: Fields, Tables, Stamps, Figures

DocumentLens is engineered for comprehensive data extraction across a wide array of document types. It can:
*   **Extract specific fields:** Identifying and pulling out key-value pairs regardless of their position on the page.
*   **Process complex tables:** Naturally extracting structured data from tables, understanding rows, columns, and their semantic relationships without rigid templates ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).
*   **Recognize stamps and figures:** Identifying and classifying non-textual elements like company stamps, signatures, or embedded figures, which often carry critical information in business documents.
*   **Handle diverse inputs:** From scanned PDFs and native PDFs to images and even email attachments, DocumentLens ensures broad input coverage ([source](https://ticnote.com/en/blog/ai-document-automation-tools)).

This capability is vital for industries like finance, insurance, and legal, where every piece of information, textual or visual, contributes to compliance and decision-making.

### Structured Outputs for Seamless Enterprise Workflows

The true power of DocumentLens lies in its ability to transform raw document content into highly structured, machine-readable outputs. It produces data in formats like JSON, CSV, and XML, which are immediately consumable by enterprise systems. This means:
*   **Direct integration:** Extracted data can seamlessly feed into ERP, CRM, RPA platforms (like UiPath/Automation Anywhere), and cloud stacks (AWS/Azure/GCP) ([source](https://ticnote.com/en/blog/ai-document-automation-tools)).
*   **Workflow triggers:** The structured output can trigger downstream processes, automating actions based on extracted information, moving beyond mere data capture to intelligent orchestration ([source](https://www.ibml.com/blog/trends-in-document-automation-for-2026/)).
*   **Enhanced analytics:** Clean, structured data enables reliable downstream analytics and reporting, providing deeper insights for business intelligence ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).

### Multilingual and Regional Document Support

Recognizing the global nature of modern business, DocumentLens is designed with robust multilingual capabilities. It supports a wide range of languages, including complex Southeast Asian languages, and is adaptable to various regional document formats and conventions. This ensures that enterprises operating across different geographies can standardize their document processing, reducing the need for localized, disparate solutions. Its ability to handle diverse writing styles and formats, including mixed handwritten and printed content, makes it highly versatile for global operations ([source](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).

### DocumentLens: Your Next Step for Usable Data

DocumentLens is positioned as the right step for businesses that need more than just text. It’s for organizations ready to transform their documents into actionable intelligence, automate decision workflows, and ensure compliance with confidence. By providing high-accuracy, context-rich, and structured data, DocumentLens empowers enterprises to truly automate document-heavy processes, cutting rework and context switching, and enabling faster, more informed decisions. It's an embodiment of the shift from simply "reading" documents to genuinely "understanding" them ([source](https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a)).

## Conclusion

The debate of **OCR vs Document AI: What Enterprises Need to Know Before Automating** clearly leans towards the latter for any organization seeking meaningful automation in 2026. While traditional OCR remains a useful tool for basic text digitization, its limitations in understanding context, structure, and complex document types make it insufficient for modern enterprise demands. The future of document automation is intelligent, context-aware, and action-oriented.

Document AI, powered by advancements like Vision-Language Models and generative AI, offers a transformative approach. It enables businesses to move from simply extracting text to truly understanding documents, automating complex workflows, ensuring compliance, and driving real-time decision-making. For enterprises aiming to gain a strategic advantage, solutions like DocumentLens, which leverage these advanced capabilities to deliver usable, structured data from diverse and complex documents, are not just an upgrade—they are an essential investment in a future-ready digital infrastructure. Don't stop halfway; embrace the full potential of **intelligent document processing** to unlock unprecedented efficiency and insight.

## References

*   https://ticnote.com/en/blog/ai-document-automation-tools
*   https://aimultiple.com/ocr-technology
*   https://bizcon.dk/future-of-enterprise-architecture/
*   https://www.acldigital.com/blogs/top-6-enterprise-architecture-trends-shaping-2026-and-beyond
*   https://bizzdesign.com/blog/enterprise-transformation-shifts-will-define-2026
*   https://artificio.ai/blog/document-ai-trends-2026-from-ocr-to-agentic-processing
*   https://www.firstsource.com/insights/blogs/reading-understanding-how-ai-visual-processing-outperforms-traditional-ocr-complex
*   https://devoxsoftware.com/blog/intelligent-document-processing-vs-traditional-ocr-what-enterprises-need-in-2026/
*   https://intuitionlabs.ai/pdfs/pharma-document-ai-ocr-accuracy-a-benchmark-analysis.pdf
*   https://intuitionlabs.ai/articles/pharma-document-ai-ocr-benchmarks
*   https://www.ibml.com/blog/trends-in-document-automation-for-2026/
*   https://www.ziaconsulting.com/blog/enterprise-tech-trends/
*   https://www.techrxiv.org/doi/10.36227/techrxiv.172651542.23422356
*   https://celestialsys.com/blogs/beyond-ocr-financial-compliance/
*   https://pnwacfe.org/Blog/13406876
*   https://www.tredence.com/blog/visual-language-models
*   https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/
*   https://packagex.io/blog/vision-language-model
*   https://www.firstsource.com/insights/whitepapers/document-processing-with-vlm
*   https://medium.com/@tpps.sai.kailash.bc/from-ocr-to-document-intelligence-how-genai-enhances-modern-ocr-workflows-b88343b3a16a
*   https://learn.microsoft.com/en-ca/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc
*   https://gleematic.com/why-document-processing-with-ocr-is-no-longer-enough/