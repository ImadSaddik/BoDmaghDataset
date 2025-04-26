import os
import sys
import json
import time
import logging

from tqdm import tqdm
from dotenv import load_dotenv
from models import Conversation

from google import genai
from google.genai.client import Client
from google.genai.types import GenerateContentConfig, GenerateContentResponse

from system_prompts import (
    get_system_prompt_for_topic_classification,
    get_system_prompt_for_markdown_task,
    get_system_prompt_for_safety_flags_classification
)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def enrich_dataset(dataset_to_enrich: list, client: Client) -> list:
    logger.info("Starting dataset enrichment process.")

    logger.info("Step 1: Adding conversation field and ID.")
    enriched_dataset = _add_conversation_field_and_id(dataset_to_enrich)

    logger.info("Step 2: Adding token count.")
    _add_token_count(enriched_dataset)

    logger.info("Step 3: Adding number of turns.")
    _add_number_of_turns(enriched_dataset)

    logger.info("Step 4: Adding conversation in markdown format.")
    _add_conversation_in_markdown_format(enriched_dataset, client)

    logger.info("Step 5: Adding data source.")
    _add_data_source(enriched_dataset)

    logger.info("Step 6: Adding conversation topic.")
    _add_conversation_topic(enriched_dataset, client)

    logger.info("Step 7: Adding safety flags.")
    _add_safety_flags(enriched_dataset, client)

    logger.info("Dataset enrichment process finished.")
    return enriched_dataset


def _load_dataset_to_enrich() -> list:
    with open("../input_dataset.json") as f:
        data = json.load(f)

    return data


def _add_conversation_field_and_id(data: list) -> list:
    new_data = []
    for i, entry in enumerate(data):
        new_data.append({
            "id": i,
            "conversation": entry
        })
    return new_data


def _add_token_count(data: list) -> None:
    tokenizer = _load_tokenizer()

    for entry in data:
        token_count = 0
        for conversation_turn in entry["conversation"]:
            content = conversation_turn["content"]
            if content:
                tokens = tokenizer.encode(content)
                token_count += len(tokens)

    entry["token_count"] = token_count


def _load_tokenizer() -> object:
    from minbpe import RegexTokenizer

    tokenizer = RegexTokenizer()
    tokenizer.load("../tokenizer/darija_tokenizer.model")
    return tokenizer


def _add_number_of_turns(data: list) -> None:
    for entry in data:
        number_of_turns = len(entry["conversation"])
        entry["number_of_turns"] = number_of_turns


def _add_conversation_in_markdown_format(data: list, client: Client) -> None:
    def _get_user_prompt(conversation: list[dict]) -> str:
        return f"""Please format the following conversation in markdown format. If you cannot format it, return it as is without any formatting.

    {conversation}
    """

    def _get_formatted_conversation(response: GenerateContentResponse) -> list[dict]:
        if not response:
            return []

        formatted_conversation = []
        for conversation_turn in response.parsed.conversation:
            formatted_conversation.append({
                "role": conversation_turn.role,
                "content": conversation_turn.content
            })
        return formatted_conversation

    for entry in tqdm(data, total=len(data), desc="Formatting conversations in markdown"):
        conversation = entry["conversation"]
        user_prompt = _get_user_prompt(conversation)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_prompt,
            config=GenerateContentConfig(
                system_instruction=[
                    get_system_prompt_for_markdown_task()
                ],
                response_mime_type="application/json",
                response_schema=Conversation,
            )
        )
        if not response:
            entry["markdown_conversation"] = []
        else:
            formatted_conversation = _get_formatted_conversation(response)
            entry["markdown_conversation"] = formatted_conversation

        time.sleep(5)


def _add_data_source(data: list) -> None:
    for entry in data:
        entry["data_source"] = "Manually generated"


def _add_conversation_topic(data: list, client: Client) -> None:
    def _get_user_prompt(conversation: list[dict]) -> str:
        return f"""Classify the topic of the following conversation:

    {conversation}
    """

    for entry in tqdm(data, total=len(data), desc="Classifying conversation topics"):
        conversation = entry["conversation"]
        user_prompt = _get_user_prompt(conversation)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_prompt,
            config=GenerateContentConfig(
                system_instruction=[
                    get_system_prompt_for_topic_classification()
                ]
            )
        )
        if not response:
            entry["topic"] = []
        else:
            topic = response.text.strip()
            entry["topic"] = topic

        time.sleep(5)


def _add_safety_flags(data: list, client: Client) -> None:
    def _get_user_prompt(conversation: list[dict]) -> str:
        return f"""Classify the safety flags for the following conversation:

    {conversation}
    """

    for entry in tqdm(data, total=len(data), desc="Classifying safety flags"):
        conversation = entry["conversation"]
        user_prompt = _get_user_prompt(conversation)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_prompt,
            config=GenerateContentConfig(
                system_instruction=[
                    get_system_prompt_for_safety_flags_classification()
                ]
            )
        )
        if not response:
            entry["safety_flags"] = []
        else:
            safety_flags = response.text.strip()
            entry["safety_flags"] = json.loads(safety_flags)

        time.sleep(5)


def append_to_the_global_dataset(dataset_to_add: list) -> None:
    logger.info("Appending enriched dataset to the global dataset.")
    with open("../dataset.json") as f:
        global_dataset = json.load(f)
        last_id = global_dataset[-1]["id"]

        for i, entry in enumerate(dataset_to_add, start=last_id + 1):
            entry["id"] = i
            global_dataset.append(entry)

    with open("../dataset.json", "w") as f:
        json.dump(global_dataset, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    sys.path.append("..")
    load_dotenv()

    dataset_to_enrich = _load_dataset_to_enrich()
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    enriched_dataset = enrich_dataset(dataset_to_enrich, client)
    append_to_the_global_dataset(enriched_dataset)
    logger.info(
        "Successfully enriched the dataset and appended it to the global dataset.")
