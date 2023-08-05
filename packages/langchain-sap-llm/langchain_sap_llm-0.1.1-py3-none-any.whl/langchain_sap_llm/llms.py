import requests
from langchain.llms.base import LLM
from langchain_sap_llm.types import SAP_AI_PLAYGROUND_MODEL
from langchain_sap_llm.config import SAPLLM_DEFAULT_MODEL
from typing import Optional, List, Mapping, Any
import re


class SAPLLM(LLM):
    x_csrf_token: str
    cookie: str
    model: SAP_AI_PLAYGROUND_MODEL = SAPLLM_DEFAULT_MODEL

    @staticmethod
    def _extract_model_name_from_curl_command(curl_command: str) -> str:
        model_name_search = re.search(r'"model":"(.+?)"', curl_command)
        if model_name_search:
            model_name = model_name_search.group(1)
            return model_name
        else:
            raise ValueError("Failed to extract model name from the curl command.")

    @classmethod
    def from_curl_command(cls, curl_command: str | None = None):
        if curl_command is None:
            import pyperclip

            curl_command = pyperclip.paste().strip()
        x_csrf_token = None
        cookie = None

        # Extract x-csrf-token
        x_csrf_token_search = re.search(r"-H 'x-csrf-token: (.+?)'", curl_command)
        if x_csrf_token_search:
            x_csrf_token = x_csrf_token_search.group(1)

        # Extract cookie
        cookie_search = re.search(r"-H 'cookie: (.+?)'", curl_command)
        if cookie_search:
            cookie = cookie_search.group(1)

        # Extract model name
        model_name: SAP_AI_PLAYGROUND_MODEL
        try:
            model_name = cls._extract_model_name_from_curl_command(curl_command)  # type: ignore
        except ValueError:
            model_name = SAPLLM_DEFAULT_MODEL

        if not x_csrf_token or not cookie:
            raise ValueError(
                "Failed to extract x-csrf-token and/or cookie from the curl command."
            )

        return cls(x_csrf_token=x_csrf_token, cookie=cookie, model=model_name)

    @property
    def _llm_type(self) -> str:
        return f"sap-llm-{self.model}"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        headers = {
            'authority': 'ai-playground.cfapps.sap.hana.ondemand.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': self.cookie,
            'referer': 'https://ai-playground.cfapps.sap.hana.ondemand.com/index.html',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-csrf-token': self.x_csrf_token,
        }

        headers['content-type'] = 'application/json; charset=UTF-8'
        headers['origin'] = 'https://ai-playground.cfapps.sap.hana.ondemand.com'
        data = {"message": prompt, "model": self.model}
        response = requests.post(
            'https://ai-playground.cfapps.sap.hana.ondemand.com/aicore/chat',
            headers=headers,
            json=data,
        )

        if response.status_code != 200:
            raise ValueError("Failed to get a response from the API.")

        response_json = response.json()
        return response_json["value"]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"x_csrf_token": self.x_csrf_token, "cookie": self.cookie}
