# OCR Accuracy in the Real World: Character Accuracy Is Not Business Accuracy

In the quest for digital transformation, Optical Character Recognition (OCR) has long been hailed as a foundational technology, promising to liberate businesses from the shackles of paper-based processes. From digitizing historical archives to automating invoice processing, OCR's ability to convert scanned images into searchable, editable text has been a game-changer ([Source: ISG](https://isg-one.com/articles/the-evolution-of-intelligent-document-processing), [Source: Affinda](https://www.affinda.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/)). However, a critical misunderstanding often clouds the true value of OCR: the assumption that high character recognition rates automatically translate into usable business data. This article delves into why **OCR Accuracy in the Real World: Character Accuracy Is Not Business Accuracy**, and how modern Document AI solutions are bridging this crucial gap.

## The Evolution of OCR: From Telegraph Code to AI Intelligence

The journey of OCR began over a century ago. In 1914, Emanuel Goldberg developed a machine to read characters and convert them into telegraph code, laying the groundwork for automated text processing ([Source: PairSoft](https://www.pairsoft.com/blog/revolutionizing-text-processing-the-history-and-future-of-ocr-technology/), [Source: Wikipedia](https://en.wikipedia.org/wiki/Optical_character_recognition), [Source: Incode](https://www.incode.com/blog/the-history-of-optical-character-recognition-ocr)). His later "Statistical Machine" in the 1920s and 30s, acquired by IBM, aimed at searching microfilm archives using optical code recognition ([Source: PairSoft](https://www.pairsoft.com/blog/revolutionizing-text-processing-the-history-and-future-of-ocr-technology/), [Source: Wikipedia](https://en.wikipedia.org/wiki/Optical_character_recognition), [Source: RPATech](https://www.rpatech.ai/blogs/ocr-technology/), [Source: OneAdvanced](https://www.oneadvanced.com/resources/optical-character-recognition-ocr-technology-a-brief-history/)).

Significant breakthroughs continued, notably with Ray Kurzweil's omni-font OCR system in 1974, which could recognize text in virtually any font, revolutionizing accessibility for the blind and opening up broader applications ([Source: Incode](https://www.incode.com/blog/the-history-of-optical-character-recognition-ocr), [Source: PairSoft](https://www.pairsoft.com/blog/revolutionizing-text-processing-the-history-and-future-of-ocr-technology/), [Source: RPATech](https://www.rpatech.ai/blogs/ocr-technology/), [Source: Wikipedia](https://en.wikipedia.org/wiki/Optical_character_recognition), [Source: ISG](https://isg-one.com/articles/the-evolution-of-intelligent-document-processing)). By the 1980s and 90s, OCR became widespread for digitizing documents in libraries and offices, with programs like OmniPage making OCR accessible on personal computers ([Source: Incode](https://www.incode.com/blog/the-history-of-optical-character-recognition-ocr), [Source: Veryfi](https://www.veryfi.com/ocr-api-platform/history-of-ocr/)).

Today, OCR is a foundational technology, integrated into mobile apps and enterprise automation platforms, supporting multiple languages and real-time image capture ([Source: AWS](https://aws.amazon.com/what-is/ocr/)). However, its evolution has also highlighted its inherent limitations when it comes to extracting truly *actionable* business intelligence.

## Measuring OCR: The Metrics That Matter (and Don't)

When discussing OCR accuracy, several metrics are commonly cited:

*   **Character Error Rate (CER):** This measures the percentage of incorrect characters (insertions, deletions, substitutions) compared to the total number of characters in the reference text. For standard documents, a CER below 2% is considered a good benchmark ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).
*   **Word Error Rate (WER):** Similar to CER but at the word level, WER is calculated as the number of incorrect words compared to the total number of words. This metric is particularly relevant when extracted text feeds into NLP pipelines or search indexes ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy), [Source: Retica.ai](https://retica.ai/en/blog/ocr-accuracy-guide-how-to-ensure-accuracy-and-improve-results/)).

While these metrics provide a quantitative measure of how well an OCR engine recognizes individual characters and words, they often fall short in reflecting real-world business utility. A document can achieve an impressive 99% CER, meaning only 1% of characters are wrong, yet still be completely unusable for automated business processes.

## The Critical Disconnect: Character Accuracy vs. Field-Level Accuracy

Here's where the core problem lies: **OCR Accuracy in the Real World: Character Accuracy Is Not Business Accuracy**. Businesses don't just need text; they need *data*. They need specific pieces of information extracted correctly and placed into the right fields within their systems. This is where **Field-Level (Semantic) Accuracy** becomes the paramount metric.

Field-level accuracy measures whether a specific extracted field—such as an invoice total, an expiry date, or a policy number—is completely correct, irrespective of the accuracy of the surrounding text ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)). A system might correctly transcribe every word on an invoice, achieving a low CER, but if it misidentifies the "Invoice Number" as the "Purchase Order Number" or extracts the "Subtotal" instead of the "Grand Total," the entire extraction is a failure from a business perspective. That's an error that costs money and requires manual intervention ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).

For financial fields and identity documents, the 2026 benchmark for field-level accuracy is a demanding 99.9%. This high threshold is necessary to enable straight-through processing (STP), where documents move through workflows without any human review ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).

### Why Traditional OCR Fails at Business Accuracy: The Problem of Context Blindness

Traditional OCR systems are fundamentally "context blind" ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)). They excel at converting pixels into text at fixed positions but lack the ability to interpret meaning or understand relationships between pieces of information. For example, an OCR engine might see a sequence of digits. It cannot inherently tell if that number represents a "Total," a "Quantity," or a "Date" – it only knows the coordinates where that number appears ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

Consider an invoice: it contains multiple numeric fields—an invoice number, a purchase order number, a tax ID, a customer account reference, and various line item quantities and prices. To a human, these distinctions are intuitive, interpreted based on surrounding words, layout, and visual hierarchy. To a machine, however, they are merely sequences of digits unless context is applied ([Source: LlamaIndex - OCR for Invoices](https://www.llamaindex.ai/blog/ocr-for-invoices)).

This context blindness creates "silent errors" ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)). A field mapped to the wrong coordinate extracts the wrong value, and the system might still mark it as a successful extraction because the *characters* were recognized correctly. For intelligent document processing workflows that depend on extraction accuracy, this is a serious operational risk ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

### The Limitations of Template-Based OCR

Many early and even current OCR solutions rely on templates. Template-based OCR systems operate by matching documents to a pre-configured layout map, extracting data based on exact field coordinates ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)). While effective for highly standardized documents, this approach quickly breaks down in the real world:

*   **New Document Formats:** A new vendor invoice or a slightly revised form will have no matching template, halting processing until a new one is manually built and tested ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).
*   **Layout Changes:** Even minor changes in document layout can render existing templates obsolete, requiring constant maintenance ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).
*   **Scalability Issues:** The operational cost of template-based OCR grows with each new supplier or document type, as each requires dedicated template creation and maintenance ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).
*   **Context Blindness:** As discussed, even with a perfect template, the system is still reading positions, not meanings, making it vulnerable to silent extraction errors ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

These rigid structures, maintenance overheads, poor variability handling, and context blindness result in systems that are expensive to run and fragile under real operating conditions ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

## The Shift to Intelligent Document Processing (IDP) and AI

Recognizing these limitations, the field has evolved beyond traditional OCR to **Intelligent Document Processing (IDP)**. IDP is designed to deal with the influx of data in a more intelligent way, extracting important information and managing it efficiently ([Source: ISG](https://isg-one.com/articles/the-evolution-of-intelligent-document-processing)). It builds on OCR by integrating advanced AI models that significantly improve both accuracy and functionality ([Source: Addepto](https://addepto.com/blog/from-ocr-to-intelligent-document-processing-how-ai-is-transforming-document-management/)).

IDP systems are designed to understand documents in a way that is much closer to how humans interpret them. This means recognizing not just what is written, but also what it means, how different elements relate to each other, and what actions should be taken based on that information ([Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/)).

Key technologies enabling this shift include:

*   **Deep Learning:** Models like Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) enhance the system's ability to recognize text even in challenging conditions and capture long-range dependencies within a document ([Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/), [Source: AJBConsulting](https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/)).
*   **Natural Language Processing (NLP):** NLP plays a central role in enabling machines to understand human language within documents. It allows systems to identify key entities (names, dates, financial values), detect relationships between them, and convert unstructured text into structured data. NLP can also uncover deeper insights by identifying topics, categorizing documents, or analyzing sentiment ([Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/), [Source: AJBConsulting](https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/)).
*   **Computer Vision:** While NLP focuses on text, Computer Vision interprets the visual aspects of documents. This includes analyzing layout, identifying structural elements (headers, tables), and understanding spatial relationships between components. This visual context is crucial, especially where meaning is tied to structure ([Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/), [Source: Klearstack](https://klearstack.com/blogs/template-based-ocr), [Source: LlamaIndex - OCR for Invoices](https://www.llamaindex.ai/blog/ocr-for-invoices)).

This integration allows IDP to handle semi-structured, unstructured, and handwritten documents, significantly reducing the need for manual intervention and transforming documents from static records into dynamic sources of business intelligence ([Source: ISG](https://isg-one.com/articles/the-evolution-of-intelligent-document-processing), [Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/)).

### Templateless OCR: The AI-Powered Advantage

A key advancement within IDP is **templateless OCR**. Unlike its template-based predecessor, templateless OCR is an AI-powered document extraction system that identifies fields based on context and labels, not fixed coordinates ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)). This means:

*   It can process any document format automatically, including formats it has never seen before, without prior template setup ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).
*   The system does not break when document layouts change.
*   Machine learning models improve extraction accuracy over time without manual reconfiguration ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).
*   It inherently handles handwritten text, unstructured layouts, and multi-format documents ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

Templateless OCR achieves this flexibility through the combined power of computer vision, deep learning, and natural language processing, allowing the system to process any document format accurately without a fixed template ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr)).

## The Next Frontier: Vision Language Models (VLMs) and Generative AI

The most recent evolutionary stage in document processing involves the integration of **Large Language Models (LLMs)** and **Vision Language Models (VLMs)** into IDP workflows. This is not merely an incremental improvement but a fundamental transformation ([Source: Artificio.ai](https://artificio.ai/blog/IDP-using-large-language-models)).

LLMs bring a fundamentally different capability: **contextual understanding** ([Source: Artificio.ai](https://artificio.ai/blog/IDP-using-large-language-models)). They process text in ways that approximate human reading comprehension, grasping not just the presence of key terms but their meaning within the broader narrative. This enables:

*   **Recognition of Conceptual Equivalence:** LLMs can identify relevant information even when expressed in different terms (e.g., "potential future obligations" and "contingent liabilities" mean the same thing) ([Source: Artificio.ai](https://artificio.ai/blog/IDP-using-large-language-models)).
*   **Multi-Document Analysis and Cross-Referencing:** LLMs excel at maintaining context across multiple documents, synthesizing information and identifying contradictions or discrepancies between related sources ([Source: Artificio.ai](https://artificio.ai/blog/IDP-using-large-language-models)).
*   **Natural Language Queries and Insight Generation:** These systems can respond to natural language queries, understand document context, and generate insights that connect information across multiple sources, moving beyond predefined extraction tasks ([Source: Artificio.ai](https://artificio.ai/blog/IDP-using-large-language-models)).

**Generative AI** further reshapes IDP by:

*   Elevating document pre-processing tasks like noise removal and resolution enhancement ([Source: Zinnov](https://zinnov.com/automation/why-generative-ai-in-intelligent-document-processing-has-been-a-game-changer-blog/)).
*   Improving document classification through synthetic labeled data.
*   Enabling data extraction with natural language prompts.
*   Facilitating rigorous validation with diminished manual oversight and even auto-populating missing data ([Source: Zinnov](https://zinnov.com/automation/why-generative-ai-in-intelligent-document-processing-has-been-a-game-changer-blog/)).

### VLMs: The Best of Both Worlds?

Vision Language Models (VLMs) combine the visual understanding of computer vision with the linguistic prowess of LLMs. They don't just see text; they use semantic reasoning to interpret it ([Source: Graahand](https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce)). This provides several advantages over traditional OCR:

*   **Superior Handwriting Recognition:** VLMs deliver highly reliable extraction from handwritten forms where traditional engines struggle ([Source: F22Labs](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/), [Source: Graahand](https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce)).
*   **Contextual Awareness:** They provide "lossless comprehension," understanding the relationship between a label and its value even in complex layouts ([Source: Graahand](https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce)).
*   **Zero-Shot Capability:** Top-tier VLMs can achieve high accuracy on new document types out-of-the-box, unlike traditional engines that require extensive fine-tuning ([Source: Graahand](https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce)).
*   **Robustness:** VLMs are more robust against complex backgrounds, low-contrast text, and can denoise and infer missing letters using context ([Source: F22Labs](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/)).

However, VLMs are not without their weaknesses. They are computationally expensive and can be slower than traditional OCR for bulk processing. More critically, VLMs can "hallucinate"—inventing text that doesn't exist, misreading specific numbers, or generating plausible but incorrect structural assumptions, which is unacceptable for critical financial or legal documents ([Source: Dev.to](https://dev.to/kesimo/ocr-vs-vlm-why-you-need-both-and-how-hybrid-approaches-win-5bo4)).

This is why the future of document understanding often lies in **hybrid systems**, where OCR handles fast bulk extraction for clean documents, while VLMs are routed for complex cases, validation, or semantic understanding, especially when OCR confidence is low ([Source: F22Labs](https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/), [Source: Graahand](https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce), [Source: Dev.to](https://dev.to/kesimo/ocr-vs-vlm-why-you-need-both-and-how-hybrid-approaches-win-5bo4)).

## DocumentLens: Achieving Business Accuracy with Document AI

In this evolving landscape, businesses demand solutions that move beyond mere character recognition to deliver **business accuracy**. This is where advanced Document AI systems like DocumentLens come into play, designed from the ground up to address the limitations of traditional OCR and template-based systems.

DocumentLens is a business-accuracy-focused document AI system that understands documents as structured entities, not just flat text. It leverages the power of templateless OCR, advanced computer vision, deep learning, and natural language processing to deliver reliable, actionable data.

Here’s how DocumentLens ensures business accuracy:

*   **Structured Field Extraction and Semantic Correctness:** DocumentLens focuses on extracting specific data fields with semantic understanding. It doesn't just recognize characters; it interprets the meaning of the data within its context. For an invoice, it understands that a number next to "Invoice No." is the primary billing identifier, while a similar pattern next to "PO" is a procurement reference ([Source: LlamaIndex - OCR for Invoices](https://www.llamaindex.ai/blog/ocr-for-invoices)). This ensures that the extracted data is not only accurate at the character level but also semantically correct for its intended business purpose.
*   **Preserves Layout and Document Hierarchy:** Unlike systems that flatten documents into raw text, DocumentLens uses advanced computer vision and layout analysis to understand the visual structure of a document. It detects tables, columns, headers, logos, and spatial relationships between elements, building a structural map without any predefined field coordinates ([Source: Klearstack](https://klearstack.com/blogs/template-based-ocr), [Source: LlamaIndex - OCR for Invoices](https://www.llamaindex.ai/blog/ocr-for-invoices)). This preservation of hierarchy is crucial for correctly interpreting complex documents and ensuring data integrity.
*   **Grounds Values to Their Original Locations for Verification:** DocumentLens provides a transparent audit trail by grounding extracted values to their original locations within the document image. This visual verification allows users to quickly confirm the accuracy of extracted data, building trust in the automation process and facilitating human-in-the-loop validation for low-confidence extractions.
*   **Uses Confidence and Schema-Aligned Outputs to Improve Downstream Reliability:** DocumentLens provides confidence scores for each extracted field, allowing businesses to set thresholds for automation versus human review. Its outputs are schema-aligned, meaning the extracted data is automatically mapped to predefined structures, ready for direct integration into ERP, CRM, or other business systems. This reduces the need for manual validation and interpretation, moving companies from reactive document handling to proactive, insight-driven workflows ([Source: Addepto](https://addepto.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/)).

By focusing on these capabilities, DocumentLens ensures that businesses receive usable, validated data, not just a high character recognition rate. It transforms documents from static records into dynamic sources of business intelligence, enabling true straight-through processing.

## Practical Steps to Enhance Document AI Accuracy

While DocumentLens and similar advanced systems handle much of the complexity, businesses can still implement best practices to maximize their document processing accuracy:

### 1. Robust Pre-Processing

The quality of the input image significantly impacts OCR performance. Even the best OCR engines struggle with flawed inputs ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).

*   **High-Resolution Scans:** Standardize scanning settings to at least 300 DPI, ideally 300-600 DPI, for high-stakes text extraction. This is one of the cheapest and most impactful accuracy improvements ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy), [Source: Retica.ai](https://retica.ai/en/blog/ocr-accuracy-guide-how-to-ensure-accuracy-and-improve-results/)).
*   **Image Enhancement:** Apply techniques like noise reduction (Gaussian blurring, median filtering), contrast adjustment, and binarization (converting to high-contrast black and white) to give the OCR engine the clearest possible signal ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy), [Source: AJBConsulting](https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/), [Source: LlamaIndex - Image Preprocessing](https://www.llamaindex.ai/glossary/what-is-image-preprocessing)).
*   **Deskewing and Orientation Correction:** Automatically detect and correct skewed or rotated pages. Even a 5-degree tilt can significantly increase word error rates ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy), [Source: AJBConsulting](https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/)).

Modern solutions like DocumentLens often incorporate these pre-processing steps automatically using layout-aware computer vision, ensuring optimal input quality without manual configuration ([Source: LlamaIndex - OCR for Invoices](https://www.llamaindex.ai/blog/ocr-for-invoices)).

### 2. Leveraging Language Models for Post-OCR Correction

Even with excellent pre-processing, raw OCR output can contain misrecognitions. This is where LLM post-OCR correction becomes invaluable. By passing raw OCR output through a language model with a targeted correction prompt, the model can fix clear misrecognitions without rewriting or paraphrasing the original text ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)). The key is prompt specificity, guiding the LLM to *only* correct OCR errors while preserving original formatting.

### 3. Continuous Training and Custom Dictionaries

For domain-specific documents (e.g., medical records, legal documents), creating custom dictionaries containing industry-specific terms can significantly enhance accuracy. Training OCR models with domain-specific data also improves their performance on that particular type of document ([Source: AJBConsulting](https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/), [Source: Retica.ai](https://retica.ai/en/blog/ocr-accuracy-guide-how-to-ensure-accuracy-and-improve-results/)). Advanced AI-based solutions like DocumentLens continuously learn and improve over time, adapting to new fonts, formats, and languages without requiring ongoing manual model maintenance.

### 4. Robust Validation and Ground Truth

To truly measure and improve business accuracy, a robust validation framework is essential:

*   **Ground Truth Sets:** Create a sample of documents that have been manually verified to be 100% correct. This ground truth set should reflect your actual document distribution, not just the cleanest examples ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).
*   **Automated Comparison and Cost-of-Error Framework:** Use automated tools to compare OCR output against your ground truth, calculating CER, WER, and crucially, field-level discrepancies. Frame these errors in terms of their actual cost to your operation to prioritize improvements ([Source: LlamaIndex](https://www.llamaindex.ai/blog/ocr-accuracy)).

## Conclusion: Beyond Character Recognition to Business Intelligence

The journey of OCR has been one of continuous innovation, from early mechanical readers to today's sophisticated AI-powered systems. However, a fundamental truth remains: **OCR Accuracy in the Real World: Character Accuracy Is Not Business Accuracy**. Businesses don't need perfect character recognition if the extracted data is contextually incorrect or misplaced. They need reliable, structured, and validated data that can seamlessly integrate into their workflows and drive strategic decision-making.

The shift from traditional OCR to Intelligent Document Processing, templateless OCR, and the integration of Large Language Models and Vision Language Models marks a pivotal moment. Solutions like DocumentLens exemplify this new era, focusing on semantic correctness, layout preservation, and verifiable data grounding. By embracing these advanced Document AI systems, organizations can move beyond the misleading simplicity of character accuracy benchmarks and achieve true **AI document extraction accuracy** that delivers tangible business value. The future of document processing is not just about seeing text, but about understanding its meaning and transforming it into actionable intelligence.

## References

*   https://www.incode.com/blog/the-history-of-optical-character-recognition-ocr
*   https://www.pairsoft.com/blog/revolutionizing-text-processing-the-history-and-future-of-ocr-technology/
*   https://en.wikipedia.org/wiki/Optical_character_recognition
*   https://www.rpatech.ai/blogs/ocr-technology/
*   https://www.oneadvanced.com/resources/optical-character-recognition-ocr-technology-a-brief-history/
*   https://addepto.com/blog/from-ocr-to-intelligent-document-processing-how-ai-is-transforming-document-management/
*   https://klearstack.com/blogs/template-based-ocr
*   https://zinnov.com/automation/why-generative-ai-in-intelligent-document-processing-has-been-a-game-changer-blog/
*   https://artificio.ai/blog/IDP-using-large-language-models
*   https://isg-one.com/articles/the-evolution-of-intelligent-document-processing
*   https://aws.amazon.com/what-is/ocr/
*   https://www.affinda.com/blog/from-ocr-to-ai-the-evolution-of-ocr-technology/
*   https://www.veryfi.com/ocr-api-platform/history-of-ocr/
*   https://www.llamaindex.ai/blog/ocr-accuracy
*   https://www.llamaindex.ai/glossary/what-is-image-preprocessing
*   https://artificio.ai/blog/unlocking-hidden-data-the-role-of-ocr-in-analyzing-unstructured-documents
*   https://www.llamaindex.ai/blog/ocr-for-invoices
*   https://www.tratta.io/blog/ocr-invoice-processing
*   https://www.rillion.com/learn-ap/ocr-invoice-processing/
*   https://www.f22labs.com/blogs/ocr-vs-vlm-vision-language-models-key-comparison/
*   https://graahand.medium.com/beyond-recognition-why-vision-language-models-are-the-future-of-document-intelligence-7af24aa785ce
*   https://dev.to/kesimo/ocr-vs-vlm-why-you-need-both-and-how-hybrid-approaches-win-5bo4
*   https://ajbconsulting.us/enhancing-ocr-accuracy-best-practices-and-techniques/
*   https://retica.ai/en/blog/ocr-accuracy-guide-how-to-ensure-accuracy-and-improve-results/