from .base import BaseConfig

DEFAULT_CONFIG: BaseConfig = {
    "RETRIEVER": "gemini_grounding",
    "EMBEDDING": "gemini_native:gemini-embedding-001",
    "SIMILARITY_THRESHOLD": 0.42,
    "FAST_LLM": "google_genai:gemini-2.5-flash-lite",
    "SMART_LLM": "google_genai:gemini-2.5-pro",  # Has support for long responses (2k+ words).
    "STRATEGIC_LLM": "google_genai:gemini-2.5-flash",  # Fast model for planning and strategic tasks.
    "FAST_TOKEN_LIMIT": 6000,
    "SMART_TOKEN_LIMIT": 6000,
    "STRATEGIC_TOKEN_LIMIT": 8000,
    "BROWSE_CHUNK_MAX_LENGTH": 10000,
    "CURATE_SOURCES": False,
    "SUMMARY_TOKEN_LIMIT": 1200,
    "TEMPERATURE": 0.4,
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "MAX_SEARCH_RESULTS_PER_QUERY": 5,
    "MEMORY_BACKEND": "local",
    "TOTAL_WORDS": 6000,
    "REPORT_FORMAT": "APA",
    "MAX_ITERATIONS": 3,
    "AGENT_ROLE": None,
    "SCRAPER": "browser",
    "MAX_SCRAPER_WORKERS": 15,
    "SCRAPER_RATE_LIMIT_DELAY": 0.0,  # Minimum seconds between scraper requests (0 = no limit, useful for API rate limiting)
    "MAX_SUBTOPICS": 3,
    "LANGUAGE": "english",
    "REPORT_SOURCE": "web",
    "DOC_PATH": "./my-docs",
    "PROMPT_FAMILY": "default",
    "LLM_KWARGS": {},
    "EMBEDDING_KWARGS": {},
    "VERBOSE": False,
    # Deep research specific settings
    "DEEP_RESEARCH_BREADTH": 3,
    "DEEP_RESEARCH_DEPTH": 2,
    "DEEP_RESEARCH_CONCURRENCY": 4,
    
    # MCP retriever specific settings
    "MCP_SERVERS": [],  # List of predefined MCP server configurations
    "MCP_AUTO_TOOL_SELECTION": True,  # Whether to automatically select the best tool for a query
    "MCP_ALLOWED_ROOT_PATHS": [],  # List of allowed root paths for local file access
    "MCP_STRATEGY": "fast",  # MCP execution strategy: "fast", "deep", "disabled"
    "REASONING_EFFORT": "medium",
    
    # Gemini-specific settings
    "GEMINI_THINKING_BUDGET": None,  # None = default thinking enabled, 0 = disabled for faster responses, or custom value
    "GEMINI_GROUNDING_DYNAMIC_THRESHOLD": 0.7,  # Confidence threshold for dynamic retrieval (0.0-1.0)
    
    # Gemini Embedding settings
    "GEMINI_EMBEDDING_TASK_TYPE": "RETRIEVAL_DOCUMENT",  # Task type for embedding optimization
    "GEMINI_EMBEDDING_DIMENSIONALITY": 768,  # Output dimension size (128-3072, 768 recommended for storage efficiency)
}
