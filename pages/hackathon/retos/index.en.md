---
title: "Challenges #HackathonSomosNLP 2026"
description: Let's drive the creation of language models aligned with the culture of LATAM and the Iberian Peninsula.
lang: en
cover: /images/eventos/260511_hackathon_eventbrite.png
---

<script setup>
import ChallengesGrid from '../../../src/components/ChallengesGrid.vue'

const miniChallenges = [
  {
    title: "Exams (INCLUDE)",
    description: "Look for multiple-choice exams to evaluate how much LLMs know about your country. Prioritize exams in languages other than Spanish and/or focused on cultural topics (e.g., history, literature).",
    dates: "April 9 - May 31",
    points: "1 pt",
    requirements: "Know how to search on the internet",
    link: "https://somosnlp.org/en/hackathon/retos/include",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "Cultural Questions (BLEND)",
    description: "Answer questions about your country to evaluate LLMs' cultural knowledge. We will use these answers to extend the open BLEND benchmark.",
    dates: "April 14 - May 31",
    points: "2 pts",
    requirements: "Have lived in society",
    link: "https://somosnlp.org/en/hackathon/retos/blend",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const mainChallenges = [
  {
    title: "1. Generate a Preferences Dataset",
    description: "Design prompts that evaluate cultural adequacy with your country and choose the best response in an LLM Arena. The prompts and responses will be collected and shared with all participating teams as the v0 preferences dataset for the alignment phase.",
    dates: "April 14 - May 21",
    points: "3 pts",
    requirements: "Have lived in society and want to dig into the concept of cultural adequacy",
    link: "https://somosnlp.org/en/hackathon/retos/preferencias",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.A. Align a textual model (LLM)",
    description: "Process, filter and extend the v0 preferences dataset adapting it to your use case. Use it to align an LLM with optimized training and alignment techniques such as LoRA, quantization and Direct Preference Optimization (DPO).",
    dates: "April 21 - May 31 (Max. 2 weeks)",
    points: "3 pts",
    requirements: "Know how to program",
    link: "https://somosnlp.org/en/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.B. Align a multimodal model",
    description: "Generate a dataset of images and descriptions using the Cohere API. Use it to create a multimodal model (VLLM) that generates image descriptions taking context into account, using the latest optimized training techniques.",
    dates: "April 21 - May 31 (Max. 2 weeks)",
    points: "3 pts",
    requirements: "Have experience in NLP",
    link: "https://somosnlp.org/en/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const finalChallenges = [
  {
    title: "3. Create a demo",
    description: "Create a demo of your project in a Hugging Face Space so everyone can see your work.",
    dates: "Until May 31",
    points: "0.5 pts",
    requirements: "Have completed a main challenge",
    link: "https://somosnlp.org/en/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "4. Record a video",
    description: "Record a 5-minute video presenting your project to the jury and the rest of the community.",
    dates: "Submission until June 1",
    points: "0.5 pts",
    requirements: "Have completed a main challenge",
    link: "https://somosnlp.org/en/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "5. (Optional) Write a paper",
    description: "Write a paper describing your project. If you're interested, we can mentor you and help you submit it to a LatinX in NLP workshop.",
    dates: "Starting in June",
    points: "0.5 pts",
    requirements: "Have completed a main challenge",
    link: "https://somosnlp.org/en/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]
</script>

This year's hackathon focuses on creating resources to evaluate and align language models with the culture of LATAM and Iberian Peninsula countries. The hackathon has been extended **until MAY 31**.

The hackathon consists of a main challenge and several mini-challenges through which you can also collect points towards the final prizes and win extra prizes. The maximum total score is 10 points.

On this page you'll find information about:
- Getting started
- Incentives and prizes
- Mini-challenges
- Main challenge
- Frequently asked questions

Good luck! 🚀

---

## 👣 Getting started

Before getting started, everyone needs to:
- ✅ Join the [SomosNLP Discord server](https://discord.com/invite/my8w7JUxZR)
- ✅ Create a [Hugging Face account](https://huggingface.co/join)
- ✅ Fill out the [registration form](https://hackathon-somosnlp-2026.eventbrite.com)
- ✅ Join the hackathon's [Hugging Face organization](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD), where the datasets, models and demos will be shared

To create a team:
- You can sign up with people you already know (e.g. your class or work group) or meet people from the SomosNLP community from other countries, universities and companies. If you'd like to meet new people, check the [#encuentra-equipo channel](https://discord.com/channels/938134488670675055/1082369575666073611)
- Once you've put your team together, ONE person must [register the team](https://forms.gle/mLKEURUXGiNhq31T9)

---

## 👏 Incentives and prizes

By participating you'll have the opportunity to:
- ✨ Learn from live workshops and talks
- ✨ Get access to $500 in Cohere API credits
- ✨ Get access to a Hugging Face L40S GPU
- ✨ Win $1000 in Mistral API credits
- ✨ Win hundreds of USD in GPU credits and AI/language books
- ✨ Win access to an online AI Master's program
- ✨ Win a ticket to the WomenTech Network online conference
- ✨ Win a nomination to the Nova talent network
- ✨ Earn mentorships with leading people in the NLP field
- ✨ Co-author papers at international NLP conferences
- ✨ Get a participation (or winning team) certificate for the hackathon

Let's go! 🚀

---

## ✨ Mini-challenges

Take part in these mini-challenges to help build datasets that evaluate LLMs' cultural knowledge and stereotypes. You'll collect points and can win extra prizes!

<ChallengesGrid :challenges="miniChallenges" />

---

## 🔥 Main challenge

1. Generate a preferences dataset
2. Align a textual (option A) or multimodal (option B) model — your choice
3. Create a demo of your project
4. Present your project in a 5-minute video
5. (Optional) write a paper presenting your project

<ChallengesGrid :challenges="mainChallenges" />

<ChallengesGrid :challenges="finalChallenges" />

---

## ❓ Frequently asked questions

<details>
<summary>Why should I take part?</summary>

By joining this hackathon you'll have the opportunity to:

- ✅ Understand how large language models work, both textual (LLMs) and multimodal (VLLMs), and discover the challenges of each stage of their development: corpus creation, training, alignment and evaluation
- ✅ Help build the first diverse, high-quality preferences corpus for aligning LLMs with the culture of LATAM and Iberian Peninsula countries (great experience and great for your CV)
- ✅ Be part of the team that creates some of the datasets for the first open LLM leaderboard in Spanish: La Leaderboard
- ✅ Get all your NLP questions answered during "Ask Me Anything" mentoring sessions
- ✅ Get support to present your work in a paper
- ✅ Win prizes to keep growing as a professional and earn a certificate you can share on LinkedIn
- ✅ Join the largest community of Spanish speakers who study, work and research in NLP

</details>

<details>
<summary>What level is required?</summary>

The SomosNLP team encourages you to take part regardless of your current knowledge. In previous editions we've had both research-institute groups and undergraduate student groups — every project counts!

- 📖 We'll run a series of **hands-on workshops** to walk you through how to build a project, so you have a reference example.

- ❓ We'll organize **AMAs** (Ask Me Anything) with experts and mentors so they can answer your questions.

</details>

<details>
<summary>What determines how complex a project is?</summary>

We'll provide an example of how to create a dataset, train a model and build a demo. It's up to you and your team to decide how much to research and work to improve on the baseline. The difficulty also depends on the use case, the data source, how much time you spend curating the data, the training technique, how many iterations you do and how polished you want your demo to be. You're free to choose everything!

</details>

<details>
<summary>Do we really need 4 weeks?</summary>

No — it depends on your availability, you can develop a great project in a week. We know people study and work, so we leave more time than strictly needed so everyone can take part. We also want to give you extra time to enjoy attending the talks and mentorships live during the hackathon.

</details>

<details>
<summary>Until when can I create a team?</summary>

EDITED: We welcome new teams until May 23. The final day to submit projects is May 31.

</details>

<details>
<summary>How do I join a team?</summary>

Read the "To create a team:" section at the top of this page and the README in the #encuentra-equipo channel of our Discord server :)

</details>

<details>
<summary>Can there be teams of 1 person?</summary>

Yes, we accept teams of 1 to 5 people.

</details>

<details>
<summary>How do you recommend we organize ourselves?</summary>

- Use your project's Discord channel to communicate and stay organized.
- Since this is an international hackathon, we recommend async communication, or splitting the work and holding smaller meetings.
- Schedule meetings or chat spontaneously using the new voice channels in the "SALAS DE REUNIÓN" category on Discord.
- Pin important messages in your project channel — e.g. task allocation, next meeting date, etc. To pin a message, click the three dots and select "Pin message".
- For extra clarity, you can also create a shared document with the team to write down the project goal, split tasks and so on (and pin the link in the chat).

</details>

<details>
<summary>I don't understand Discord — which channels are the most important?</summary>

- Check the [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115) channel — we recommend enabling notifications; we post 2–3 times a week
- Ask your questions in the Discord [#pide-ayuda](https://discord.com/channels/938134488670675055/1051997272356966430) channel so everyone can benefit from the answer
- We announce events in the [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) channel and add them to the [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)

</details>

<details>
<summary>How can I find out about the events?</summary>

- We announce events in the [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) channel
- We add them to the [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- We announce them on social media ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_))
- [Follow us on YouTube](https://www.youtube.com/c/somosnlp?sub_confirmation=1) and save the [2026 hackathon playlist](https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

</details>

<details>
<summary>How can I give feedback on the event?</summary>

- You can give us feedback to improve the challenge guides with this [form](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anonymous)
- We'll also share a general feedback form at the end of the event

</details>


*If we've told you there's info on this page you can't find, clear your cookies and reload the page.*

---

## 🙌 Other ways to support LLMs' cultural alignment

<details>
<summary>How can I help?</summary>

- Share posts from the @SomosNLP accounts ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_)) and invite your colleagues and classmates to put a team together!
- Are you at university? [Share this info with your professor](https://somosnlp.org/en/hackathon/universidades) or someone in the AI/CS group so your university can collaborate with the event.
- Want to support the initiative with visibility, sponsored vouchers or a financial donation? [Sponsor the hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>
