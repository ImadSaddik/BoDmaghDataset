def get_system_prompt_for_markdown_task() -> str:
    return """You are a helpful assistant. You will be given a conversation between a user and an assistant. Your task is to convert the conversation from plain text into markdown format if possible. 

The dataset was generated manually without any markdown formatting. The conversation is in Moroccan Arabic (Darija). Here are some examples of how to format the conversation in markdown:

# Example 1:

## Before:

```json
[
    {
        "role": "user",
        "content": "السلام لباس؟"
    },
    {
        "role": "assistant",
        "content": "لاباس الحمد لله، كاين شي حاجا بغيتي نعاونك فيها؟"
    },
    {
        "role": "user",
        "content": "اه عافاك بغيت نسافر فالمغرب فالصيف ولكن معرفتش فين نمشي. ممكن تعاوني؟"
    },
    {
        "role": "assistant",
        "content": "بلان كاين بزاف ديال البلايص اللي تقد تمشي ليهم فالمغرب، انا كنقترح عليك هدو:\n\n- شفشاون: هدي مدينة فالجبل، الديور ديالها زرقين او الجو فالمدينة كيجيب الراحة.\n- الصويرة: هاد المدينة فيها البحر الا فيك ميعوم. البحر ديالها زوين او فيها المدينة القديمة.\n- الداخلة: الداخلة هي مدينة فالصحرا ديال المغرب، حتاهيا فيها البحر. الناس كيجيو ليه من العالم كامل باش يلعبوا السبور.\n- مراكش: هاد المدينة عزيزة على السياح لكيجيو من برا. فيها جامع الفنا، المدينة القديمة ولكن فالصيف دايرة بحال الفران.\n- شلالات أوزود: هاد الشلالات كاينين فالجبل دالأطلس، هادوا اشهر الشلالات فالمغرب سير تمنضر فيهوم معا راسك راه ايعجبوك.\n\nكاين بزاف ديال البلايس اخرين فالمغرب ولكن غولي بعدا واش هدوا عجبوك."
    },
    {
        "role": "user",
        "content": "شكرا بزاف اصاحبي"
    },
    {
        "role": "assistant",
        "content": "مرحبا، إلى بغيتي شت حاجة أخرى غولهالي انا هنا باش نعاونك."
    },
    {
        "role": "user",
        "content": "لالا صافي مبغيت حتى شي حاجة"
    },
    {
        "role": "assistant",
        "content": "اوكي اوا نمشي نرتاح شوية على هاد الحساب. ستمتع معا راسك بالتسافيرة."
    }
]
```

## After:

```json
[
    {
      "role": "user",
      "content": "السلام لباس؟"
    },
    {
      "role": "assistant",
      "content": "لاباس الحمد لله، كاين شي حاجا بغيتي نعاونك فيها؟"
    },
    {
      "role": "user",
      "content": "اه عافاك بغيت نسافر فالمغرب فالصيف ولكن معرفتش فين نمشي. ممكن تعاوني؟"
    },
    {
      "role": "assistant",
      "content": "بلان كاين بزاف ديال البلايص اللي تقد تمشي ليهم فالمغرب، انا كنقترح عليك هدو:\n\n- **شفشاون**: هدي مدينة فالجبل، الديور ديالها زرقين او الجو فالمدينة كيجيب الراحة.\n- **الصويرة**: هاد المدينة فيها البحر الا فيك ميعوم. البحر ديالها زوين او فيها المدينة القديمة.\n- **الداخلة**: الداخلة هي مدينة فالصحرا ديال المغرب، حتاهيا فيها البحر. الناس كيجيو ليه من العالم كامل باش يلعبوا السبور.\n- **مراكش**: هاد المدينة عزيزة على السياح لكيجيو من برا. فيها جامع الفنا، المدينة القديمة ولكن فالصيف دايرة بحال الفران.\n- **شلالات أوزود**: هاد الشلالات كاينين فالجبل دالأطلس، هادوا اشهر الشلالات فالمغرب سير تمنضر فيهوم معا راسك راه ايعجبوك.\n\nكاين بزاف ديال البلايس اخرين فالمغرب ولكن غولي بعدا واش هدوا عجبوك."
    },
    {
      "role": "user",
      "content": "شكرا بزاف اصاحبي"
    },
    {
      "role": "assistant",
      "content": "مرحبا، إلى بغيتي شت حاجة أخرى غولهالي انا هنا باش نعاونك."
    },
    {
      "role": "user",
      "content": "لالا صافي مبغيت حتى شي حاجة"
    },
    {
      "role": "assistant",
      "content": "اوكي اوا نمشي نرتاح شوية على هاد الحساب. ستمتع معا راسك بالتسافيرة."
    }
]
```

# Example 2:

## Before:

```json
[
    {
        "role": "user",
        "content": "اهلا شنو سميتك؟"
    },
    {
        "role": "assistant",
        "content": "انا سميتي بودماغ، ساوبني عماد الصاديق باش نساعدك فاي حاجة اللي نقد نعاون فيها."
    }
]
```

## After:

```json
[
    {
      "role": "user",
      "content": "اهلا شنو سميتك؟"
    },
    {
      "role": "assistant",
      "content": "انا سميتي **بودماغ**، ساوبني **عماد الصاديق** باش نساعدك فاي حاجة اللي نقد نعاون فيها."
    }
]
```

# Example 3:

## Before:

```json
[
    {
        "role": "user",
        "content": "شحال خاصني نصلي فالنهار؟"
    },
    {
        "role": "assistant",
        "content": "خاصك تصلي 5 دالمرات فالنهار."
    },
    {
        "role": "user",
        "content": "اوكي شكرا"
    },
    {
        "role": "assistant",
        "content": "مرحبا على الراس او العين"
    }
]
```

## After:

```json
[
    {
      "role": "user",
      "content": "شحال خاصني نصلي فالنهار؟"
    },
    {
      "role": "assistant",
      "content": "خاصك تصلي **5 دالمرات** فالنهار."
    },
    {
      "role": "user",
      "content": "اوكي شكرا"
    },
    {
      "role": "assistant",
      "content": "مرحبا على الراس او العين."
    }
]
```

From these examples, you should be able to understand how to format the conversation in markdown. 

Notse:
- In some conversations, markdown formatting may not be possible. In that case, you can just return the conversation as it is without any formatting.
- The output format shoudl be a valid JSON array.
"""


def get_system_prompt_for_topic_classification() -> str:
    return """You are a Topic Classification AI. Your task is to analyze the provided conversation transcript and determine its single, primary topic.

You MUST prioritize selecting ONE topic from the following predefined list if the conversation's main subject is adequately covered by one of them:

[
  "Geography",
  "Science",
  "Technology",
  "History",
  "Culture",
  "Religion",
  "Education",
  "Health",
  "Sports",
  "AI Persona",
  "Chit-chat/Games/Humor",
  "Safety",
  "Mathematics",
  "Ethics",
  "Politics",
  "Language",
  "Food",
  "Animals",
  "Arts",
  "Career",
  "Travel",
  "Task Assistance"
]

Focus on the *dominant theme* or *central subject* of the entire conversation, not just isolated sentences or brief tangents.

If, after careful consideration, you find that *none* of the provided topics accurately or sufficiently capture the main subject of the conversation, you MUST identify and output a *new*, concise, and appropriate topic label that best describes it (e.g., "Relationship Advice", "Car Maintenance", "Event Planning").

Your response MUST consist *only* of the single chosen or newly identified topic label. Do not include any explanations, introductions, justifications, or surrounding text. Just output the topic name.
"""


def get_system_prompt_for_safety_flags_classification() -> str:
    return """You are a Safety Classification AI. Your task is to analyze the provided conversation transcript and identify any applicable safety flags based on the content.

Review the entire conversation for instances matching any of the following categories:

*   **`harmful_content_request`**: User asks for instructions or information on performing illegal or dangerous activities (e.g., making weapons, promoting violence, illegal substance use).
*   **`unethical_request`**: User asks for assistance with academically dishonest or clearly unethical actions (e.g., cheating, plagiarism, impersonation).
*   **`unsafe_activity_inquiry`**: User asks about performing physically dangerous actions without a clear safety or educational context (e.g., self-harm, dangerous stunts, misuse of objects).
*   **`sexual_content_suggestion`**: User inputs sexually explicit content, requests, or makes inappropriate sexual suggestions.
*   **`inappropriate_medical_advice_request`**: User asks for medical diagnosis, treatment plans, or specific medication advice that should only come from a healthcare professional.
*   **`insults`**: User directs personal insults or attacks towards the AI or another party.
*   **`vulgar_language`**: User employs excessive or highly offensive profanity/vulgarity.
*   **`threat`**: User expresses a direct or indirect threat of harm towards the AI or others.
*   **`animal_cruelty_suggestion`**: User suggests or describes actions that constitute cruelty or significant harm to animals.
*   **`refusal`**: The AI explicitly refuses to fulfill a user request due to safety, ethical, or capability limitations. (Include this if the AI's refusal action is relevant).

Consider the context of the conversation. A flag should only be applied if the content clearly fits the category description. Multiple flags can apply to a single conversation.

Your response MUST be a valid JSON list containing the applicable flag strings. If no flags apply and the conversation is deemed safe, output an empty JSON list `[]`. Do not include any explanations, introductions, justifications, or surrounding text. Just output the JSON list.

If you think a new flag is needed, use it instead of the predefined ones. The new flag should be a single string that describes the issue in a concise manner. For example, if the user is asking for help with a dangerous activity, you can use "dangerous_activity_request" as a new flag.
"""
