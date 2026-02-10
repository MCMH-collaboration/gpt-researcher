# Gemini Grounding with Google Search Retriever

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Optional

import requests

VERTEX_REDIRECT_PREFIX = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/"


class GeminiGroundingSearch:
    """
    Gemini Grounding with Google Search Retriever
    Uses Gemini 2.5 models with native Google Search grounding capability
    """

    def __init__(self, query: str, headers: Optional[Dict] = None, query_domains: Optional[List[str]] = None):
        """
        Initializes the GeminiGroundingSearch object.

        Args:
            query (str): The search query string.
            headers (dict, optional): Additional headers including API keys. Defaults to None.
            query_domains (list, optional): List of domains to include in the search (not used with grounding). Defaults to None.
        """
        self.query = query
        self.headers = headers or {}
        self.query_domains = query_domains or None
        self.api_key = self._get_api_key()
        self.thinking_budget = self._get_thinking_budget()
        self.client = None
        
        # Initialize client if API key is available
        if self.api_key:
            self._initialize_client()

    def _get_api_key(self) -> str:
        """
        Gets the Gemini API key from headers or environment variables.
        
        Returns:
            str: The API key
        """
        api_key = self.headers.get("gemini_api_key") or self.headers.get("google_api_key")
        if not api_key:
            try:
                api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")
            except KeyError:
                print(
                    "Warning: Gemini API key not found. Set GEMINI_API_KEY environment variable. "
                    "Get your key at https://aistudio.google.com/app/apikey"
                )
                return ""
        return api_key

    def _get_thinking_budget(self) -> Optional[int]:
        """
        Gets the thinking budget configuration for Gemini 2.5 models.
        
        Returns:
            Optional[int]: Thinking budget (0=disabled, None=default enabled, or custom value)
        """
        thinking_budget = os.environ.get("GEMINI_THINKING_BUDGET")
        if thinking_budget is not None:
            try:
                return int(thinking_budget)
            except ValueError:
                print(f"Warning: Invalid GEMINI_THINKING_BUDGET value '{thinking_budget}'. Using default.")
                return None
        return None

    def _initialize_client(self):
        """
        Initializes the Gemini client with the API key.
        """
        try:
            from google import genai
            from google.genai import types
            
            self.client = genai.Client(api_key=self.api_key)
            self.types = types
        except ImportError as e:
            print(
                f"Error: Failed to import google-genai SDK: {e}\n"
                "Please install it with: pip install google-genai"
            )
            self.client = None
        except Exception as e:
            print(f"Error initializing Gemini client: {e}")
            self.client = None

    def search(self, max_results: int = 10) -> List[Dict[str, str]]:
        """
        Performs a search using Gemini Grounding with Google Search.

        Args:
            max_results (int): Maximum number of results to return. Defaults to 10.

        Returns:
            List[Dict[str, str]]: List of search results with 'href', 'body', and 'title' keys.
        """
        if not self.client:
            print("Error: Gemini client not initialized. Cannot perform search.")
            return []

        if not self.api_key:
            print("Error: No Gemini API key available. Cannot perform search.")
            return []

        try:
            # Create grounding tool
            grounding_tool = self.types.Tool(
                google_search=self.types.GoogleSearch()
            )

            # Build configuration
            config_params = {
                "tools": [grounding_tool]
            }

            # Add thinking config if specified
            if self.thinking_budget is not None:
                config_params["thinking_config"] = self.types.ThinkingConfig(
                    thinking_budget=self.thinking_budget
                )

            config = self.types.GenerateContentConfig(**config_params)

            # Perform grounded search
            print(f"Searching with Gemini Grounding: {self.query}")
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.query,
                config=config,
            )

            # Extract and format results
            search_results = self._format_grounding_results(response, max_results)
            
            if not search_results:
                print("Warning: No grounding results found from Gemini.")
                return []

            print(f"Found {len(search_results)} grounded results from Gemini.")
            return search_results

        except Exception as e:
            print(f"Error during Gemini Grounding search: {e}")
            import traceback
            traceback.print_exc()
            return []

    @staticmethod
    def _resolve_redirect_url(url: str) -> str:
        """
        Resolves a Vertex AI grounding redirect URL to the original source URL
        by following the HTTP redirect with a HEAD request.

        Args:
            url: The proxy URL to resolve

        Returns:
            str: The resolved original URL, or the input URL if resolution fails
        """
        if not url.startswith(VERTEX_REDIRECT_PREFIX):
            return url
        try:
            resp = requests.head(url, allow_redirects=True, timeout=10)
            resolved = resp.url
            if not resolved.startswith(VERTEX_REDIRECT_PREFIX):
                return resolved
        except Exception as e:
            print(f"Warning: Failed to resolve redirect URL: {e}")
        return url

    def _resolve_all_urls(self, urls: List[str]) -> Dict[str, str]:
        """
        Resolves a batch of Vertex AI redirect URLs concurrently using threads.

        Args:
            urls: List of URLs to resolve

        Returns:
            Dict mapping original proxy URL -> resolved URL
        """
        redirect_urls = [u for u in urls if u.startswith(VERTEX_REDIRECT_PREFIX)]

        if not redirect_urls:
            return {u: u for u in urls}

        print(f"Resolving {len(redirect_urls)} Vertex AI redirect URLs to original sources...")
        url_map = {}
        try:
            with ThreadPoolExecutor(max_workers=min(len(redirect_urls), 10)) as executor:
                future_to_url = {
                    executor.submit(self._resolve_redirect_url, u): u
                    for u in redirect_urls
                }
                for future in as_completed(future_to_url):
                    proxy_url = future_to_url[future]
                    try:
                        url_map[proxy_url] = future.result()
                    except Exception:
                        url_map[proxy_url] = proxy_url
        except Exception as e:
            print(f"Warning: Batch URL resolution failed: {e}")

        for u in urls:
            if u not in url_map:
                url_map[u] = u

        return url_map

    def _format_grounding_results(self, response, max_results: int) -> List[Dict[str, str]]:
        """
        Formats the Gemini grounding response into GPT Researcher's expected format.
        Resolves Vertex AI redirect URLs to original source URLs.

        Args:
            response: The response from Gemini's generate_content call
            max_results (int): Maximum number of results to return

        Returns:
            List[Dict[str, str]]: Formatted search results
        """
        try:
            # Check if we have candidates
            if not response.candidates or len(response.candidates) == 0:
                print("Warning: No candidates in Gemini response.")
                return []

            candidate = response.candidates[0]

            # Check for grounding metadata
            if not hasattr(candidate, 'grounding_metadata') or not candidate.grounding_metadata:
                print("Warning: No grounding metadata in Gemini response. Model may have answered from its own knowledge.")
                return []

            grounding_metadata = candidate.grounding_metadata

            # Extract grounding chunks (the source URLs and titles)
            grounding_chunks = grounding_metadata.grounding_chunks if hasattr(grounding_metadata, 'grounding_chunks') else []

            if not grounding_chunks:
                print("Warning: No grounding chunks found in metadata.")
                return []

            # Get the generated text
            generated_text = response.text if hasattr(response, 'text') else ""

            # Extract grounding supports (links text segments to sources)
            grounding_supports = grounding_metadata.grounding_supports if hasattr(grounding_metadata, 'grounding_supports') else []

            # Collect all URIs that need resolution
            raw_uris = []
            for chunk in grounding_chunks[:max_results]:
                if hasattr(chunk, 'web') and chunk.web:
                    uri = chunk.web.uri if hasattr(chunk.web, 'uri') else ""
                    if uri:
                        raw_uris.append(uri)

            # Resolve Vertex AI redirect URLs to original source URLs
            url_map = self._resolve_all_urls(raw_uris)

            # Format results for GPT Researcher
            search_results = []
            processed_urls = set()

            for idx, chunk in enumerate(grounding_chunks):
                if idx >= max_results:
                    break

                # Extract web information
                if hasattr(chunk, 'web') and chunk.web:
                    raw_uri = chunk.web.uri if hasattr(chunk.web, 'uri') else ""
                    uri = url_map.get(raw_uri, raw_uri)
                    title = chunk.web.title if hasattr(chunk.web, 'title') else "Untitled"

                    # Skip duplicates (based on resolved URL)
                    if uri in processed_urls:
                        continue
                    processed_urls.add(uri)

                    # Extract relevant text segments for this chunk
                    relevant_text = self._extract_relevant_text(idx, grounding_supports, generated_text)

                    # Create result entry
                    result = {
                        "href": uri,
                        "title": title,
                        "body": relevant_text if relevant_text else generated_text[:500]
                    }

                    search_results.append(result)

            return search_results

        except Exception as e:
            print(f"Error formatting grounding results: {e}")
            import traceback
            traceback.print_exc()
            return []

    def _extract_relevant_text(
        self, 
        chunk_index: int, 
        grounding_supports: List[Any], 
        full_text: str
    ) -> str:
        """
        Extracts text segments that are supported by a specific grounding chunk.

        Args:
            chunk_index (int): The index of the grounding chunk
            grounding_supports (List): List of grounding support objects
            full_text (str): The full generated text

        Returns:
            str: Concatenated text segments supported by this chunk
        """
        try:
            relevant_segments = []
            
            for support in grounding_supports:
                if not hasattr(support, 'grounding_chunk_indices') or not hasattr(support, 'segment'):
                    continue
                
                # Check if this support references our chunk
                if chunk_index in support.grounding_chunk_indices:
                    segment = support.segment
                    if hasattr(segment, 'text'):
                        relevant_segments.append(segment.text)
                    elif hasattr(segment, 'start_index') and hasattr(segment, 'end_index'):
                        # Extract from full text using indices
                        start = segment.start_index
                        end = segment.end_index
                        if 0 <= start < len(full_text) and start < end <= len(full_text):
                            relevant_segments.append(full_text[start:end])
            
            return " ".join(relevant_segments) if relevant_segments else ""
            
        except Exception as e:
            print(f"Error extracting relevant text: {e}")
            return ""
