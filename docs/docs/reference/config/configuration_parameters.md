---
sidebar_label: Configuration Parameters
title: Configuration Parameters
---

The `BaseConfig` dictionary controls the behavior of the GPT Researcher. Below is a detailed explanation of each parameter.

## Retriever & Embedding Settings

### `RETRIEVER`
*   **Default:** `"gemini_grounding"`
*   **Description:** Specifies the retriever method used for fetching relevant information. Options may include search engines or specific retrieval algorithms like `tavily`, `google`, `bing`, `duckduckgo`, `searx`, `arxiv`, `pubmed`, `google_scholar` or `gemini_grounding` for Google's grounding capabilities.

### `EMBEDDING`
*   **Default:** `"gemini_native:gemini-embedding-001"`
*   **Description:** Defines the embedding model provider and model name used for vectorizing text. The format is typically `provider:model_name`.

### `SIMILARITY_THRESHOLD`
*   **Default:** `0.42`
*   **Description:** The threshold score (between 0 and 1) for determining if a retrieved document is similar enough to the query to be included in the context. Higher values require closer matches.

## LLM Settings

### `FAST_LLM`
*   **Default:** `"google_genai:gemini-2.5-flash-lite"`
*   **Description:** The "fast" Large Language Model used for simpler, speed-critical tasks such as summarization or quick queries. Format: `provider:model_name`.

### `SMART_LLM`
*   **Default:** `"google_genai:gemini-2.5-flash"`
*   **Description:** The "smart" LLM used for complex reasoning, generating the final report, and handling longer contexts. It typically supports longer responses (2k+ words).

### `STRATEGIC_LLM`
*   **Default:** `"google_genai:gemini-2.5-pro"`
*   **Description:** A model optimized for planning, outlining, and high-level strategic tasks in the research process.

### `TEMPERATURE`
*   **Default:** `0.4`
*   **Description:** Controls the randomness of the LLM's output. Lower values (closer to 0) make the output more deterministic and focused, while higher values make it more creative and varied.

### `LLM_KWARGS`
*   **Default:** `{}`
*   **Description:** A dictionary of additional keyword arguments to pass directly to the LLM initialization (e.g., specific API parameters).

### `EMBEDDING_KWARGS`
*   **Default:** `{}`
*   **Description:** A dictionary of additional keyword arguments to pass directly to the embedding model initialization.

## Token Limits & Context

### `FAST_TOKEN_LIMIT`
*   **Default:** `3000`
*   **Description:** The maximum number of tokens allowed for the `FAST_LLM` context window.
*   **Maximum Value:** Depends on the selected model's context window size (e.g., ~128k for GPT-4o, ~1M for Gemini 1.5 Flash). Ensure this value is within your model's limits.

### `SMART_TOKEN_LIMIT`
*   **Default:** `6000`
*   **Description:** The maximum number of tokens allowed for the `SMART_LLM` context window.
*   **Maximum Value:** Depends on the selected model's context window size. Since `SMART_LLM` handles larger contexts for report generation, you can set this higher (e.g., 100k+) if your model supports it.

### `STRATEGIC_TOKEN_LIMIT`
*   **Default:** `4000`
*   **Description:** The maximum number of tokens allowed for the `STRATEGIC_LLM` context window.
*   **Maximum Value:** Depends on the selected model's context window size.

### `SUMMARY_TOKEN_LIMIT`
*   **Default:** `700`
*   **Description:** The maximum number of tokens reserved for generating summaries of sources.
*   **Maximum Value:** Should be comfortably within the `FAST_LLM` context limit. Setting this too high may slow down research or exceed rate limits.

### `BROWSE_CHUNK_MAX_LENGTH`
*   **Default:** `8192`
*   **Description:** The maximum character length for chunks of text read from websites during browsing.
*   **Maximum Value:** Limited by the `FAST_TOKEN_LIMIT`. Since chunks are processed by `FAST_LLM`, this value (in characters) should roughly correspond to a token count lower than `FAST_TOKEN_LIMIT` (approx. 4 chars per token).

## Research & Scraper Settings

### `MAX_SEARCH_RESULTS_PER_QUERY`
*   **Default:** `5`
*   **Description:** The number of search results to process for each research query.

### `SCRAPER`
*   **Default:** `"bs"`
*   **Description:** The web scraping method to use. `"bs"` stands for BeautifulSoup. Other options might include `"playwright"` or `"selenium"` if configured.

### `MAX_SCRAPER_WORKERS`
*   **Default:** `15`
*   **Description:** The maximum number of concurrent workers allowed for web scraping tasks.

### `SCRAPER_RATE_LIMIT_DELAY`
*   **Default:** `0.0`
*   **Description:** The minimum delay (in seconds) between scraper requests. Useful for avoiding IP bans or adhering to API rate limits.

### `CURATE_SOURCES`
*   **Default:** `False`
*   **Description:** If set to `True`, the agent will curate and filter sources more aggressively before using them.

### `USER_AGENT`
*   **Default:** (A common browser User-Agent string)
*   **Description:** The User-Agent string sent in HTTP headers during web requests to mimic a real browser.

## Report Generation Settings

### `TOTAL_WORDS`
*   **Default:** `1200`
*   **Description:** The target word count for the final generated report.
*   **Maximum Value:** Constrained by the `SMART_LLM`'s maximum output token limit. For example, if a model outputs max 4096 tokens, the word count should be kept under ~3000 words.

### `REPORT_FORMAT`
*   **Default:** `"APA"`
*   **Description:** The citation and formatting style for the report (e.g., "APA", "MLA").

### `REPORT_SOURCE`
*   **Default:** `"web"`
*   **Description:** The primary source of information for the report. Options: `"web"` (internet search) or `"local"` (local documents).

### `DOC_PATH`
*   **Default:** `"./my-docs"`
*   **Description:** The file path to the directory containing local documents if `REPORT_SOURCE` is set to `"local"`.

### `PROMPT_FAMILY`
*   **Default:** `"default"`
*   **Description:** Selects the family of prompts to use for the research process, allowing for different personas or instructions sets.

### `LANGUAGE`
*   **Default:** `"english"`
*   **Description:** The language in which the research and report should be conducted and generated.

## Execution Control

### `MAX_ITERATIONS`
*   **Default:** `3`
*   **Description:** The maximum number of iterations the agent can perform during the research process (e.g., refining queries).

### `MAX_SUBTOPICS`
*   **Default:** `3`
*   **Description:** The maximum number of subtopics to generate and research for a given main topic.

### `AGENT_ROLE`
*   **Default:** `None`
*   **Description:** Can be used to assign a specific persona or role to the agent. If `None`, the agent may determine its own role or use a default.

### `MEMORY_BACKEND`
*   **Default:** `"local"`
*   **Description:** The backend used for storing agent memory. Options typically include `"local"`, `"redis"`, etc.

### `VERBOSE`
*   **Default:** `False`
*   **Description:** If `True`, enables detailed logging output for debugging purposes.

## Deep Research Settings

### `DEEP_RESEARCH_BREADTH`
*   **Default:** `3`
*   **Description:** Determines the breadth of the research tree; how many distinct paths or sub-questions to explore at each level.

### `DEEP_RESEARCH_DEPTH`
*   **Default:** `2`
*   **Description:** Determines the depth of the research tree; how many levels deep the research should go.

### `DEEP_RESEARCH_CONCURRENCY`
*   **Default:** `4`
*   **Description:** The number of concurrent research tasks that can be executed during deep research.
