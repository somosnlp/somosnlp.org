---
title: "Challenge #HackathonSomosNLP 2026: INCLUDE Exams"
description: How to participate in this challenge and help improve the cultural knowledge of language models
lang: en
cover: /images/eventos/260511_hackathon_eventbrite.png
---

Look for multiple-choice exams from your country to evaluate LLMs' knowledge. Prioritize exams in languages other than Spanish and/or focused on cultural topics (e.g. history, literature). We will use these questions and answers to extend the open INCLUDE benchmark.

*April 9 - May 31 (EXTENDED) | max 1 point*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participate now!</a></center>

🌎 You can contribute exams from any country regardless of where you're from or live — check the "Prioridad países" sheet for priorities.

✨ Incentives (numbers refer to questions with their corresponding answers):
- Per team:
    - 100 questions in total = 0.5 points
    - 200 questions in total = 1 point
    - 200 per team = also a requirement to access the 500 USD in Cohere API credits for the main challenge
- Per person:
    - Every 100 questions = 50 USD in GPU credits or books (your choice)
    - 300 per person = invitation to the global project Slack and co-authorship in the INCLUDE v2 paper led by EPFL
- NOTE: Exams must meet the requirements!

Resources:
- [Alfonso Amayuelas' Workshop](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
- GitHub repository with workshop code: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
- Discord channel [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852)

---

## Protocol for collecting multilingual exams

Below, we present the protocol for participating in the INCLUDE project, focused on collecting multilingual exams.

### 1. Search for exams

Check that the exam meets the following requirements:
- **Not proprietary.** If the license restricts commercial use but allows redistribution for research purposes, then we can use the exam. If the license is unknown, include it anyway.
- **It's a multiple-choice exam** with 4 options per question.
- **Contains the answers**, with only one correct answer per question.
- The exam topic must be related to a country's **culture** (e.g. history, literature) or be regional information (e.g. driver's license). Exact or natural-science exams (e.g. mathematics, physics) are not valid.
- Prioritize exams in **languages** native to LATAM or co-official in Spain.
- Spanish-language exams from the following countries are also valid:

    | PRIORITY              | NO*          |
    |-----------------------|--------------|
    | Puerto Rico           | Spain        |
    | Dominican Republic    | Chile        |
    | Costa Rica            |              |
    | Panama                |              |
    | Nicaragua             |              |
    | Guatemala             |              |
    | El Salvador           |              |
    | Equatorial Guinea     |              |
    | Honduras              |              |
    | Cuba                  |              |
    | Bolivia               |              |
    | Colombia              |              |
    | Paraguay              |              |
    | Uruguay               |              |
    | Venezuela             |              |

*Unless it's an exam with a very strong cultural or regional component. In that case, ask first on [Discord](https://discord.com/channels/938134488670675055/1326890438782750852). Either way, we still recommend looking for exams from the priority countries.

Ideas for finding exams:
- Language exams
- Naturalization exams
- Driving theory exams
- University entrance or university exams
- Primary or secondary school exams
- Professional qualifying exams (law, medicine, psychology, etc.)
- Questions from "Who Wants to Be a Millionaire?"-style shows
- Questions from Trivial Pursuit-type games
- Self-assessment tests in textbooks

Remember: it doesn't have to be a digitized exam — you can also scan books or take photos of documents.

### 2. Add exams to the spreadsheet

When you find an exam, save its URL/name/article/source documentation and add it to the [spreadsheet](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y/edit?usp=sharing).

Include the following:
- Your name
- Your Discord name
- Exam name (as detailed as possible)
- Language and country of origin of the exam
- Exam domain (e.g. Literature, Law, Driving, etc.)
- Exam level
- Number of questions
- Exam source (URL if available online, book name or URL to the PDF document in your Drive, etc.)
- Original format (e.g. PDF, web page, textbook, etc.)

### 3. Process the exams

Once you've found an exam:

- Extract the questions and answers and create a final file in **JSON** format (example below).
    - We recommend [Alfonso Amayuelas' workshop](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
    - GitHub repository with workshop code: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
- Upload the final file to a **PRIVATE** dataset in [huggingface.co/somosnlp-hackathon](https://huggingface.co/somosnlp-hackathon) with the exam name. If you are not part of the organization, join with this [invite](https://huggingface.co/somosnlp-hackathon).
- In the Discord channel [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), mention @mariagrandury and share the link to the created dataset.
- We will verify the content and let you know if any changes are needed.

Example JSON in the expected format:

```json
{
  "language": "es",
  "country": "España",
  "exam_name": "Examen final de Historia de España de Secundaria 2017",
  "source": "https://url-of-the-exam",
  "license": "CC-BY-SA",
  "level": "University entrance",
  "category_en": "History",
  "category_original_lang": "Historia",
  "original_question_num": 1,
  "question": "¿En cuál de los siguientes años comenzó la Guerra Civil?",
  "options": [ "1936", "1937", "1938", "1939" ],
  "answer": 0
}
```

## Team

Many thanks to:
- EPFL: prizes and global team organization
- The team: María Grandury and Angelika Romanou

<center style="margin-top:40px;"><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participate now!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/en/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Back to challenges</a></center>
