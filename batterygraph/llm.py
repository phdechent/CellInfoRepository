"""One small interface to the LLM providers used in the evaluation.

The provider is chosen from the model name:

* ``gpt-*``, ``o1-*``, ``o3-*``, ``o4-*`` -> OpenAI      (``OPENAI_API_KEY``)
* ``claude-*``                            -> Anthropic   (``ANTHROPIC_API_KEY``)
* ``gemini-*``                            -> Google      (``GEMINI_API_KEY`` or ``GOOGLE_API_KEY``)
* anything else                           -> local Ollama server

API keys are read from environment variables, or from a ``.env`` file in the
working directory if ``python-dotenv`` is installed. Never commit keys.
"""

from __future__ import annotations

import os
import time
from functools import lru_cache
from typing import Optional

try:  # optional convenience
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def provider_for(model: str) -> str:
    name = model.lower()
    if name.startswith(("gpt-", "o1", "o3", "o4")):
        return "openai"
    if name.startswith("claude"):
        return "anthropic"
    if name.startswith("gemini"):
        return "gemini"
    return "ollama"


@lru_cache(maxsize=None)
def _client(provider: str):
    if provider == "openai":
        from openai import OpenAI

        return OpenAI()
    if provider == "anthropic":
        import anthropic

        return anthropic.Anthropic()
    if provider == "gemini":
        from google import genai

        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        return genai.Client(api_key=key) if key else genai.Client()
    if provider == "ollama":
        import ollama

        return ollama
    raise ValueError(provider)


class LLM:
    """``LLM("claude-sonnet-5").complete(prompt, system=...) -> str``"""

    def __init__(self, model: str, pause: float = 0.0, retries: int = 3, max_tokens: int = 2048):
        self.model = model
        self.provider = provider_for(model)
        self.pause = pause  # optional sleep after every call (rate limits)
        self.retries = retries
        self.max_tokens = max_tokens

    def __repr__(self) -> str:
        return f"LLM({self.model!r}, provider={self.provider!r})"

    def complete(self, prompt: str, system: Optional[str] = None) -> str:
        for attempt in range(self.retries):
            try:
                text = self._call(prompt, system)
                if self.pause:
                    time.sleep(self.pause)
                return (text or "").strip()
            except Exception:
                if attempt == self.retries - 1:
                    raise
                time.sleep(3 * (attempt + 1))
        return ""

    def _call(self, prompt: str, system: Optional[str]) -> str:
        client = _client(self.provider)
        if self.provider == "openai":
            messages = ([{"role": "system", "content": system}] if system else []) + [
                {"role": "user", "content": prompt}
            ]
            response = client.chat.completions.create(model=self.model, messages=messages)
            return response.choices[0].message.content
        if self.provider == "anthropic":
            kwargs = {"system": system} if system else {}
            response = client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
            return "".join(getattr(b, "text", "") for b in response.content if getattr(b, "type", "") == "text")
        if self.provider == "gemini":
            from google.genai import types

            config = types.GenerateContentConfig(system_instruction=system) if system else None
            response = client.models.generate_content(model=self.model, contents=prompt, config=config)
            return response.text
        # Ollama
        messages = ([{"role": "system", "content": system}] if system else []) + [
            {"role": "user", "content": prompt}
        ]
        response = client.chat(model=self.model, messages=messages)
        return response["message"]["content"]


def check_models(*models: str) -> None:
    """Send a one-word prompt to each model and print the reply (API smoke test)."""
    for model in models:
        try:
            reply = LLM(model).complete("Reply with the single word: ok")
            print(f"{model:35s} OK   -> {reply[:40]!r}")
        except Exception as exc:
            print(f"{model:35s} FAIL -> {type(exc).__name__}: {str(exc)[:120]}")
