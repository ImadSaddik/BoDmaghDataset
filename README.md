# BoDmagh dataset 🧠

The BoDmagh dataset is a Supervised Fine-Tuning (SFT) dataset for the Darija language. I created it manually, ensuring high quality. The dataset is in JSON format and includes conversations between a user and an assistant.

You can find the dataset on Hugging Face: [here](https://huggingface.co/datasets/ImadSaddik/BoDmaghDataset)

I update the dataset daily, so make sure to check the repository regularly.

## Time spent  

Creating this dataset has been a labor of love. I’ve dedicated approximately **13 hours and 00 minutes** so far, manually curating each entry to ensure high quality. I continue to add new entries daily, so this number will keep growing.

## Content

### 1. Structure

Each item in the JSON file is a list. The list contains multiple objects, where each object represents a turn in the conversation. The turns are marked as either `user` or `assistant`. The `system` message is not included, but you can add it at the start of the list if needed.

Here are 2 examples:

```json
[
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
    ],
    [
        {
            "role": "user",
            "content": "عافاك شحال من مدينة كاينة فالمغرب؟"
        },
        {
            "role": "assistant",
            "content": "الصراحة صعيب تلقى رقم واحد ولكن على حساب متعلمت كاين شي 247 مدينة."
        },
        {
            "role": "user",
            "content": "اوكي شكرا."
        },
        {
            "role": "assistant",
            "content": "العفو، كاين شي حاجة أخرى بغيتي نعاونك فيها؟"
        }
    ]
]
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
3. Add entries to the dataset.
4. Create a pull request.

## Wanna talk?

You can contact me through:

- **Discord** - Username: imad_saddik
- **LinkedIn** – [Connect with me](https://www.linkedin.com/in/imadsaddik/).
- **Email** – [simad3647@gmail.com](mailto:simad3647@gmail.com).  
