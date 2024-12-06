"""
LLM Service Module for handling Llama model interactions.
This module provides a singleton service class that manages the initialization
and interaction with the Llama language model, ensuring thread-safe operations
for concurrent requests.
"""

import threading
from llama_cpp import Llama
from flask import current_app


class LLMService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_model()
        return cls._instance

    def _initialize_model(self):
        self.model = Llama.from_pretrained(
            repo_id="TheBloke/Llama-2-7B-Chat-GGUF",
            filename="llama-2-7b-chat.Q4_K_M.gguf",
            verbose=False,
            cache_dir="models",
            n_ctx=2048,
            n_threads=4
        )
        current_app.logger.info("LLM model initialized")

        self.model_lock = threading.Lock()

    def generate_response(self, prompt):
        try:
            with self.model_lock:
                formatted_prompt = f"""
                <|im_start|>system
                You are a helpful AI assistant. Respond in a clear and friendly manner.
                <|im_end|>
                <|im_start|>user
                {prompt}
                <|im_end|>
                <|im_start|>assistant"""

                stream = self.model(
                    formatted_prompt,
                    max_tokens=256,
                    temperature=0.7,
                    top_p=0.95,
                    echo=False,
                    stop=["<|im_end|>", "<|im_start|>"],
                    stream=True
                )

                current_app.logger.info("Generating response...")
                for output in stream:
                    token = output['choices'][0]['text']
                    current_app.logger.info(token)
                    yield token

        except Exception as e:
            current_app.logger.error(f"Error generating response: {str(e)}")
            raise
