# Native Gemini Embeddings Implementation
# Uses google-genai SDK for full feature support

import os
import numpy as np
from typing import List, Optional, Any
import logging
from langchain_core.embeddings import Embeddings

logger = logging.getLogger(__name__)


class GeminiEmbeddings(Embeddings):
    """
    Native Google Gemini embeddings with full feature support.
    
    Supports:
    - Task type specification (RETRIEVAL_DOCUMENT, RETRIEVAL_QUERY, etc.)
    - Configurable output dimensionality (128-3072)
    - Automatic normalization for dimensions < 3072
    - LangChain-compatible interface
    """
    
    # Supported task types from Gemini API
    TASK_TYPES = {
        "RETRIEVAL_DOCUMENT": "Optimized for document indexing in RAG systems",
        "RETRIEVAL_QUERY": "Optimized for search queries in RAG systems",
        "SEMANTIC_SIMILARITY": "Optimized for similarity comparisons",
        "CLASSIFICATION": "Optimized for text classification",
        "CLUSTERING": "Optimized for document clustering",
        "QUESTION_ANSWERING": "Optimized for Q&A systems",
        "FACT_VERIFICATION": "Optimized for fact checking",
        "CODE_RETRIEVAL_QUERY": "Optimized for code search queries",
    }
    
    def __init__(
        self,
        model: str = "gemini-embedding-001",
        task_type: Optional[str] = None,
        output_dimensionality: Optional[int] = 768,
        normalize: bool = True,
        api_key: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Initialize Gemini embeddings.
        
        Args:
            model: Model name (default: gemini-embedding-001)
            task_type: Task type for optimization (default: RETRIEVAL_DOCUMENT)
            output_dimensionality: Output dimension size (128-3072, default: 768)
            normalize: Whether to normalize embeddings for dimensions < 3072
            api_key: Gemini API key (defaults to GEMINI_API_KEY env var)
            **kwargs: Additional arguments
        """
        self.model = model
        self.task_type = task_type or "RETRIEVAL_DOCUMENT"
        self.output_dimensionality = output_dimensionality
        self.normalize = normalize
        self.api_key = api_key or self._get_api_key()
        self.client = None
        self.types = None
        
        # Validate task type
        if self.task_type not in self.TASK_TYPES:
            logger.warning(
                f"Unknown task type '{self.task_type}'. "
                f"Supported types: {', '.join(self.TASK_TYPES.keys())}"
            )
        
        # Validate dimensionality
        if self.output_dimensionality:
            if not (128 <= self.output_dimensionality <= 3072):
                raise ValueError(
                    f"output_dimensionality must be between 128 and 3072, "
                    f"got {self.output_dimensionality}"
                )
        
        # Initialize client
        if self.api_key:
            self._initialize_client()
        else:
            logger.warning(
                "No Gemini API key found. Set GEMINI_API_KEY environment variable."
            )
    
    def _get_api_key(self) -> str:
        """Get Gemini API key from environment."""
        return os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")
    
    def _initialize_client(self):
        """Initialize the Gemini client."""
        try:
            from google import genai
            from google.genai import types
            
            self.client = genai.Client(api_key=self.api_key)
            self.types = types
            logger.info(f"Initialized Gemini embeddings: {self.model}")
        except ImportError as e:
            logger.error(
                f"Failed to import google-genai SDK: {e}\n"
                "Install with: pip install google-genai"
            )
            raise
        except Exception as e:
            logger.error(f"Failed to initialize Gemini client: {e}")
            raise
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of documents.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        if not texts:
            return []
        
        if not self.client:
            raise RuntimeError("Gemini client not initialized")
        
        try:
            # Build config
            config_params = {
                "task_type": self.task_type,
            }
            
            if self.output_dimensionality:
                config_params["output_dimensionality"] = self.output_dimensionality
            
            config = self.types.EmbedContentConfig(**config_params)
            
            # Generate embeddings
            result = self.client.models.embed_content(
                model=self.model,
                contents=texts,
                config=config
            )
            
            # Extract embeddings
            embeddings = [list(emb.values) for emb in result.embeddings]
            
            # Normalize if needed (for dimensions < 3072)
            if self.normalize and self.output_dimensionality and self.output_dimensionality < 3072:
                embeddings = [self._normalize_embedding(emb) for emb in embeddings]
            
            return embeddings
            
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise
    
    def embed_query(self, text: str) -> List[float]:
        """
        Embed a single query text.
        
        Uses RETRIEVAL_QUERY task type if available, otherwise uses configured task type.
        
        Args:
            text: Text string to embed
            
        Returns:
            Embedding vector
        """
        if not self.client:
            raise RuntimeError("Gemini client not initialized")
        
        try:
            # Use RETRIEVAL_QUERY for queries if current task is RETRIEVAL_DOCUMENT
            task_type = (
                "RETRIEVAL_QUERY" 
                if self.task_type == "RETRIEVAL_DOCUMENT" 
                else self.task_type
            )
            
            # Build config
            config_params = {
                "task_type": task_type,
            }
            
            if self.output_dimensionality:
                config_params["output_dimensionality"] = self.output_dimensionality
            
            config = self.types.EmbedContentConfig(**config_params)
            
            # Generate embedding
            result = self.client.models.embed_content(
                model=self.model,
                contents=text,
                config=config
            )
            
            # Extract embedding
            embedding = list(result.embeddings[0].values)
            
            # Normalize if needed
            if self.normalize and self.output_dimensionality and self.output_dimensionality < 3072:
                embedding = self._normalize_embedding(embedding)
            
            return embedding
            
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            raise
    
    def _normalize_embedding(self, embedding: List[float]) -> List[float]:
        """
        Normalize embedding vector to unit length.
        
        Required for dimensions < 3072 for accurate semantic similarity.
        The 3072 dimension embeddings are already normalized by Gemini.
        
        Args:
            embedding: Raw embedding vector
            
        Returns:
            Normalized embedding vector
        """
        embedding_array = np.array(embedding)
        norm = np.linalg.norm(embedding_array)
        
        if norm == 0:
            logger.warning("Embedding has zero norm, returning as-is")
            return embedding
        
        normalized = embedding_array / norm
        return normalized.tolist()
    
    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Async version of embed_documents.
        
        Note: Current implementation is synchronous. For true async,
        consider using asyncio.to_thread or aiohttp.
        """
        return self.embed_documents(texts)
    
    async def aembed_query(self, text: str) -> List[float]:
        """
        Async version of embed_query.
        
        Note: Current implementation is synchronous.
        """
        return self.embed_query(text)
