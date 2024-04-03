---
title: "Hackathon #Somos600M: How to participate"
description: Everything you need to know to present a good project at the hackathon
lang: en
cover: https://somosnlp.github.io/assets/images/eventos/240301_hackathon.jpg
---

Each participating team will generate a corpus of instructions, train their LLM, and create a demo to share their great work with the community. This year the focus is on projects that represent the richness of Spanish and the diversity of Spanish-speaking people. As always, we encourage projects to have a social impact and be related to one of the UN's Sustainable Development Goals. Thank you for participating! ✨

<div class="flex justify-center">
<a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank">
    <img src="https://somosnlp.github.io/assets/images/eventos/240301_hackathon.jpg"
        width="650" height="365" alt="Hackathon 2024 Poster" />
</a>
</div>

<center><a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">📝 Registrations open until March 15!</a></center>

## ✅ Steps to participate

Participating in our hackathon and applying your knowledge to democratize NLP in Spanish is very simple, go for it!

1. Join our [Discord](https://discord.com/invite/my8w7JUxZR) community (and introduce yourself in #intros!)

2. Create an account on [Hugging Face](https://huggingface.co/join) and join the [SomosNLP](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc) organization.

3. Register on [Eventbrite](https://hackathonsomosnlp2024.eventbrite.com/?aff=w), choose the "Hackathon (English)" ticket.

4. Create your team or join one (teams of 1 to 5 people). Teams must be registered in the #encuentra-equipo channel (more info in the channel's README).

5. Create your instruction corpus and push it to hf.co/somosnlp. We recommend using the `distilabel` library. Check the [example notebook](https://distilabel.argilla.io/latest/tutorials/pipeline-notus-instructions-preferences-legal/) provided by the Argilla team!

6. Write the [Dataset Card](https://huggingface.co/docs/datasets/dataset_card) for your dataset: inspect the dataset, evaluate, and mitigate biases.

7. Fine-tune an LLM (up to 7B) and push it to hf.co/somosnlp. You can train it directly from a Space in the HuggingFace hub using [autotrain (no-code)](https://huggingface.co/docs/autotrain/llm_finetuning) or [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter). You can use T4s sponsored by HuggingFace. Remember that it's very important to test on smaller machines to verify that the code is correct and not find errors after several hours of training.

8. Write the [Model Card](https://huggingface.co/docs/hub/model-cards) for your model: evaluate its quality, biases, and carbon footprint. Important: link the dataset used for training.

9. Create a [demo Space](https://huggingface.co/spaces) to showcase your project to the community. You can use Nvidia T4 - small GPUs. Important: link the dataset(s) and model(s) used.

10. Submit your project by filling out the [submission form](https://forms.gle/zUhoHo45vRBoyMZD7). You can continue making modifications until 23h59 Anywhere on Earth on Sunday, April 10 (we will check the commit times 👀).

- Extra. You can present your project to the [Workshop LatinX in NLP @NAACL](https://somosnlp.org/blog/latinx-in-ai-at-naacl-2024).

11. Optionally, do a 5 min presentation of your project in front of the jury and the community.

Help us improve for the next edition by rating with stars different aspects of the hackathon in this [mini feedback form](https://forms.gle/jy6jNxxPYcUYmEkZ8). Thanks!

If you have any questions, we are at your disposal in the #pide-ayuda channel, write a descriptive title and select the "hackathon" tag.

We wish you much success! 🚀


## 👏 Evaluation and Prizes

<details>
<summary>🗓️ Important Dates</summary>

- April 10th 23:59 [*Anywhere On Earth*](https://time.is/Anywhere_on_Earth): Deadline to [submit projects](ttps://forms.gle/zUhoHo45vRBoyMZD7) to the Hackathon #Somos600M and the [LatinX in NLP @NAACL](https://somosnlp.org/blog/latinx-in-ai-at-naacl-2024) Workshop.
- April 11th: Live project presentations, 5 mins per team.
- April 18th: Announcement of the winning projects.
- Soon: Live presentation of the winning projects, 30 mins per team.

</details>

<details>
<summary>🏆 Benefits and Prizes</summary>

All participants 👏
- Access to PRO endpoints on Hugging Face for creating synthetic corpora.
- Access to GPUs with up to 25GB of RAM on Hugging Face for model training and demo.
- Access to "persistent storage" on Hugging Face for creating Argilla annotation spaces.
- Support to present your project at the LatinX in NLP @NAACL 2024 workshop, one of the most important international NLP conferences. Learn how in [this post](https://somosnlp.org/blog/latinx-in-ai-at-naacl-2024). Also, the LatinX in AI team is available for questions!

Everyone that presents a project 🚀
- Certificate of participation or winning team of the "Hackathon #Somos600M 2024" (verified on our website).
<!-- - 60% discount on the LenguajeNaturalAI course ["The NLP Revolution: LLMs and Beyond"](https://academia.lenguajenatural.ai/course/nlp-llms). -->
- 20% discount for the [WomenTech Global Conference 2024](https://www.womentech.net/women-tech-conference).
- Possibility of obtaining a completely free pass to attend the WomenTech Global Conference 2024 (let us know your interest in the project submission form).
- Possibility of receiving a nomination to join [Nova](https://www.novatalent.com/top-talent) (let us know your interest in the project submission form).
- Possibility to continue developing your project with our support, contact us!

3rd place team (prizes per person) 🥉
- Certificate, recognition on the website and social media, and honorary role in the Discord server.
- 20k credits from the MonsterAPI by [Q Blocks](https://www.qblocks.cloud/) for LLM training.
<!-- - Full scholarship for the LenguajeNaturalAI course ["The NLP Revolution: LLMs and Beyond"](https://academia.lenguajenatural.ai/course/nlp-llms). -->

2nd place team (prizes per person) 🥈
- Certificate, recognition on the website and social media, and honorary role in the Discord server.
- 30k credits from the MonsterAPI by [Q Blocks](https://www.qblocks.cloud/) for LLM training.
<!-- - Full scholarship for the LenguajeNaturalAI course ["The NLP Revolution: LLMs and Beyond"](https://academia.lenguajenatural.ai/course/nlp-llms).
- Full scholarship for the Cálamo & Cran course ["Advanced Word Tricks"](https://www.calamoycran.com/cursos/herramientas-para-freelancers/trucos-avanzados-de-word/). -->

1st place team (prizes per person) 🥇
- Certificate, recognition on the website and social media, and honorary role in the Discord server.
- 50k credits from the MonsterAPI by [Q Blocks](https://www.qblocks.cloud/) for LLM training.
<!-- - Full scholarship for the LenguajeNaturalAI course ["The NLP Revolution: LLMs and Beyond"](https://academia.lenguajenatural.ai/course/nlp-llms).
- Full scholarship for the Cálamo & Cran course ["Spelling and Grammar Course"](https://www.calamoycran.com/cursos/correccion/curso-de-ortografia-y-gramatica/).
- Full scholarship for the [SaturdaysAI Master's](https://saturdays.ai/master-ia-online/). -->

</details>


<details>
<summary> ✅ Project Evaluation</summary>

A complete project consists of instruction corpora + model + demo. Likewise, given the hackathon's focus on data, we also accept projects that have focused on corpus creation (maximum score: 7 points).

Corpus (4 points):
- Focus on linguistic varieties
- Correct corpus structure
- Corpus creation technique
- Clarity and reproducibility of scripts
- Completeness of the Dataset Card
- Corpus quality

Model (3 points):
- Training method used
- Clarity and reproducibility of scripts
- Completeness of the Model Card
- Model evaluation

Demo (1 point):
- Clarity and UX of the demo

Project and presentation (2 points):
- Motivation, originality, and social impact
- Clarity and quality of the presentation

Extra point:
- Each jury member can assign an extra point to a project that has particularly caught their attention.

</details>


## ❓ Frequently Asked Questions

<details>
<summary>Can I participate if I'm not from a Spanish-speaking country?</summary>

Absolutely! While the focus of the hackathon is on the Spanish language and its varieties, we welcome participants from all over the world. Diversity enriches the projects and the community!

</details>

<details>
<summary>Why should I participate?</summary>

By joining this hackathon, you will have the opportunity to:

- ✅ Understand how large language models (LLMs) work and discover the challenges of each stage of their development: corpus creation, training, and evaluation
- ✅ Participate in the creation of a quality and diverse corpus that includes the different varieties of Spanish and co-official languages (top as an experience and top for the CV)
- ✅ Resolve all your doubts about NLP during "Ask Me Anything" mentoring sessions
- ✅ Receive support to present your work in a paper
- ✅ Win prizes to continue growing as a professional and get a certificate
- ✅ Join the largest community of Spanish speakers who study, work, and research in NLP

</details>

<details>
<summary>What is the required level?</summary>

From the SomosNLP team, we want to encourage you to participate regardless of your current knowledge. In previous editions, we have had groups from research institutes and groups of undergraduate students, all projects add up!

We are at your disposal to help you in every step of the development of your project! Just post your question in the #pide-ayuda channel or ping us in your project's thread.

</details>

<details>
<summary>What does the complexity of the projects depend on?</summary>

We will provide an example of how to create a dataset, train a model, and create a demo. It's up to you and your team to choose how much to research and work to improve the base version. The difficulty also depends on the use case, the origin of the data, the time you dedicate to its curation, the training technique, the iterations you make, and how elaborate you want your demo to be. You are free to choose everything!

</details>

<details>
<summary>How long do I have to form a team?</summary>

Ideally all teams will be registered during the first week of the hackathon, until March 8th.

EDIT: We accept new teams until April 7th.

</details>

<details>
<summary>How can I find a team?</summary>

Finding a team is easy! Check the README of the #encuentra-equipo channel on our Discord server!

You have two options:
- 👀 Filter for posts from other participants who are "looking for people" and respond to them, OR
- 📢 Create a new thread specifying the topic you would like to work on

We encourage diversity in teams, including a mix of skills, experiences, and backgrounds. This diversity often leads to more innovative and comprehensive projects.

</details>

<details>
<summary>Can there be teams of 1 person?</summary>

Yes, we accept teams between 1 and 5 people.

</details>

<details>
<summary>How do you recommend organizing the work?</summary>

- Use your project channel on Discord to communicate and organize
- Since it's an international hackathon, we recommend asynchronous communication or dividing the work and holding meetings with fewer people
- Schedule meetings or talk spontaneously using the new voice channels in the "SALAS DE REUNIÓN" (meeting rooms) category on Discord
- Pin important messages in the project channel, e.g., task allocation, day of the next meeting, ... To pin a message, click on the three dots and select "Pin message"
- For better clarity, you can also create a shared document with team members to write down the project's objective, allocate tasks, and more (and pin the link in the chat)

</details>

<!--
## 📅 Important Dates

- **March 1**: Official start of the hackathon and release of detailed guidelines.
- **March 15**: Registration deadline. Make sure your team is registered by this date!
- **March 24**: Submission deadline for projects.
- **March 26**: Presentation of projects to the community and jury evaluation.
- **April 1**: Announcement of winners and closing ceremony.

Remember, the most important thing is to learn, share, and enjoy the process. We can't wait to see what you'll create!
-->

Good luck to all participants! 🌟

---

[Back to hackathon main page](https://somosnlp.org/en/hackathon)
