# BoDmagh dataset 🧠

The BoDmagh dataset is a Supervised Fine-Tuning (SFT) dataset for the Darija language. I created it manually, ensuring high quality. The dataset is in JSON format and includes conversations between a user and an assistant.

You can find the dataset on Hugging Face: [here](https://huggingface.co/datasets/ImadSaddik/BoDmaghDataset)

I update the dataset daily, so make sure to check the repository regularly.

## Time spent  

Creating this dataset has been a labor of love. I’ve dedicated approximately **16 hours and 25 minutes** so far, manually curating each entry to ensure high quality. I continue to add new entries daily, so this number will keep growing.

## Content

### 1. Structure

The dataset is a JSON file containing a list of objects. Each object represents a single conversation entry and includes several metadata fields along with the conversation itself.

Here are the main fields within each conversation object:

* **`id`**: A unique integer identifier for the conversation.
* **`conversation`**: A list of message objects representing the turns in the conversation. Each message object has:
  * `role`: Either `user` or `assistant`.
  * `content`: The text content of the message turn (plain text).
* **`token_count`**: The total number of tokens in the `conversation` field, calculated using the [darija tokenizer](https://github.com/ImadSaddik/DarijaTokenizers).
* **`turns_count`**: The total number of turns (messages) in the `conversation`.
* **`markdown_conversation`**: A list of message objects similar to `conversation`, but the `content` may include Markdown formatting (e.g., bolding, lists) where applicable.
* **`source`**: Indicates how the conversation was generated (e.g., "Manually generated").
* **`topic`**: A label indicating the primary topic of the conversation (e.g., "Science", "Travel", "Chit-chat/Games/Humor").
* **`safety_flags`**: A list of strings indicating any safety concerns identified in the conversation (e.g., `["harmful_content_request", "refusal"]`). An empty list `[]` means the conversation is considered safe.

*Note: The `system` message is not included, but you can add it if needed for your specific fine-tuning format.*

Here is an example of a single conversation object:

```json
{
    "id": 74,
    "conversation": [
        {
            "role": "user",
            "content": "شحال بعيدة علينا الشمس؟"
        },
        {
            "role": "assistant",
            "content": "الشمس بعيدة علينا ب 150 مليون كيلومتر تقريبا."
        },
        {
            "role": "user",
            "content": "ويلي ويلي شحال بعيداااا."
        },
        {
            "role": "assistant",
            "content": "واييه راه هاد الكون كبير بزاف صعيب الواحد يتخيل الكبورية ديالو."
        },
        {
            "role": "user",
            "content": "شناهية سنة ضوئية؟"
        },
        {
            "role": "assistant",
            "content": "هي المسافة اللي الضو كيضربها فعام."
        },
        {
            "role": "user",
            "content": "شحال فيها من كيلومتر؟"
        },
        {
            "role": "assistant",
            "content": "سنة ضوئية فيها 9.461 تريليون كيلومتر."
        },
        {
            "role": "user",
            "content": "والله اتا بزاف هاد الكون."
        },
        {
            "role": "assistant",
            "content": "الى عندك شي سؤال خور غولهالي."
        }
    ],
    "token_count": 97,
    "turns_count": 10,
    "markdown_conversation": [
        {
            "role": "user",
            "content": "شحال بعيدة علينا الشمس؟"
        },
        {
            "role": "assistant",
            "content": "الشمس بعيدة علينا ب **150 مليون كيلومتر** تقريبا."
        },
        {
            "role": "user",
            "content": "ويلي ويلي شحال بعيداااا."
        },
        {
            "role": "assistant",
            "content": "واييه راه هاد الكون كبير بزاف صعيب الواحد يتخيل الكبورية ديالو."
        },
        {
            "role": "user",
            "content": "شناهية سنة ضوئية؟"
        },
        {
            "role": "assistant",
            "content": "هي المسافة اللي الضو كيضربها فعام."
        },
        {
            "role": "user",
            "content": "شحال فيها من كيلومتر؟"
        },
        {
            "role": "assistant",
            "content": "سنة ضوئية فيها **9.461 تريليون كيلومتر**."
        },
        {
            "role": "user",
            "content": "والله اتا بزاف هاد الكون."
        },
        {
            "role": "assistant",
            "content": "الى عندك شي سؤال خور غولهالي."
        }
    ],
    "source": "Manually generated",
    "topic": "Science",
    "safety_flags": []
}
```

### 2. Assistant's name

Sometimes the assistant's name is included. The assistant's name is `بودماغ`. If you find this word, you can replace it with any other name. Here's an example:

```json
[
    {
        "role": "user",
        "content": "أهلا شنو سميتك؟"
    },
    {
        "role": "assistant",
        "content": "انا سميتي بودماغ، ساوبني عماد الصاديق باش نساعدك فاي حاجة اللي نقد نعاون فيها."
    },
    {
        "role": "user",
        "content": "هههه سمية واعرة عجباتني"
    },
    {
        "role": "assistant",
        "content": "هههه واييه راه عندي دماغ كبير غا باش نقد نعاونك فاي حاجة الى كنت نعرف ليها."
    },
    {
        "role": "user",
        "content": "شناهيا العاصمة دالمغرب؟"
    },
    {
        "role": "assistant",
        "content": "العاصمة دالمغرب هي الرباط."
    }
]
```

### 3. Special tokens

This dataset doesn't use any special tokens. Since everyone uses different tokens, feel free to add them as needed.

## Contributing

As I mentioned, I'm manually creating this dataset to ensure high quality. If you'd like to help, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Add your new conversations to the `input_dataset.json` file. Each conversation should be a list of message objects (see example below).
4. Run the `enrich_dataset.py` script in the `scripts` directory to enrich your conversations with metadata and append them to the global dataset.
5. Create a pull request.

### Example: Adding to `input_dataset.json`

The `input_dataset.json` file should contain a list of conversations. Each conversation is itself a list of message objects, where each message has a `role` (either `user` or `assistant`) and a `content` field. For example:

```json
[
    [
        {"role": "user", "content": "أهلا شنو سميتك؟"},
        {"role": "assistant", "content": "انا سميتي بودماغ، ساوبني عماد الصاديق باش نساعدك فاي حاجة اللي نقد نعاون فيها."}
    ],
    [
        {"role": "user", "content": "شنو تحب تشرب؟"},
        {"role": "assistant", "content": "نحب نشرب قهوة، ونتمنى انك زادة تحبها."}
    ]
]
```

After adding your conversations, run:

```bash
python scripts/enrich_dataset.py
```

This will process your new conversations and add them (with metadata) to the main dataset.

## Wanna talk?

You can contact me through:

* **Discord:** Username: imad_saddik
* **LinkedIn:** [Connect with me](https://www.linkedin.com/in/imadsaddik/).
* **Email:** [simad3647@gmail.com](mailto:simad3647@gmail.com).
