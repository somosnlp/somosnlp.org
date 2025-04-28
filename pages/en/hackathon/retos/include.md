---
title: "Challenge #HackathonSomosNLP 2025: INCLUDE Exams"
description: How to participate in this challenge and help improve the cultural knowledge of language models
lang: en
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Look for multiple-choice exams from your country to evaluate LLMs' knowledge. Prioritize exams in languages other than Spanish and/or focused on cultural topics (e.g., history, literature). We will use these questions and answers to extend the open INCLUDE benchmark.

*April 9 - April 28 (EXTENDED) | max 1 point*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participate now!</a></center>

Incentives (numbers refer to questions with their respective answers):
- Per team:
    - 100 questions in total = 0.5 points
    - 200 questions in total = 1 point
- Per person:
    - Every 100 questions = 50 USD in GPU credits or books
    - 300 per person = invitation to the global project Slack and co-authorship in the INCLUDE v2 paper
- ATTENTION: Exams must meet the requirements!

Resources:
- [Alfonso Amayuelas' Workshop](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
- GitHub repository with workshop code: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)

---

## Protocol for Collecting Multilingual Exams

Below, we present the protocol for participating in the INCLUDE project focused on collecting multilingual exams.

### 1. Search for Exams

Check if the exam meets the following requirements:
- **Not proprietary.** If the license restricts commercial use but allows redistribution for research purposes, then we can use this exam. If the license is unknown, include the exam.
- **It is an exam with multiple-choice question format** and has 4 options per question.
- **Contains the answers** and there is only one correct answer per question.
- The exam topic must be related to a country's **culture** (e.g., history, literature) or be regional information (e.g., driver's license). Exams in exact or natural sciences (e.g., mathematics, physics) are not valid.
- Prioritize finding exams in **languages** native to LATAM or co-official in Spain. Exams from these regions in Spanish are also valid.
- Unless it is an exam with a very important cultural component, we are not looking for more exams from Spain in Spanish.

Ideas for finding exams:
- University entrance exams
- Primary or secondary education exams
- Professional qualifying exams (medicine, psychology, law, etc.)
- Language exams
- Nationalization exams
- Driver's licenses
- Questions from "Who Wants to Be a Millionaire?" style programs
- Questions from Trivial Pursuit type games
- Self-assessment tests in textbooks

Remember: it doesn't need to be a digitized exam, you can also digitize books or take photos of documents.

### 2. Add Exams to the Spreadsheet

When you find an exam, save its URL/name/article/source documentation and add it to the [spreadsheet](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y/edit?usp=sharing).

Include the following:
- Your name
- Your Discord name
- Exam name (as detailed as possible)
- Language and country of origin of the exam
- Exam domain (e.g., Literature, Law, Driving, etc.)
- Exam level
- Number of questions
- Exam link (if available online, if not the name of the book or document)
- Format (e.g., PDF, web page, textbook, etc.)

### 3. Process the Exams

After finding an exam:

- Extract the questions and answers and create a final file in **JSON** format (example below).
    - We recommend [Alfonso Amayuelas' workshop](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
- Upload the final file to a **PRIVATE** dataset in [huggingface.co/somosnlp-hackathon-2025](https://huggingface.co/somosnlp-hackathon-2025) with the exam name. If you are not part of the organization, join with this [invite](https://huggingface.co/somosnlp-hackathon-2025).
- In the Discord channel [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), mention @mariagrandury and share the link to the created dataset.
- We will verify the content and inform if any changes are needed.

Example JSON in the expected format:

```json
{
  "language": "en",
  "country": "Brazil",
  "exam_name": "High School Final History Exam 2017",
  "source": "https://exam-url",
  "license": "CC-BY-SA",
  "level": "University Entrance",
  "category_en": "History",
  "category_original_lang": "História",
  "original_question_num": 1,
  "question": "In which of the following years did the Proclamation of the Republic begin?",
  "options": [ "1889", "1890", "1891", "1892" ],
  "answer": 0
}
```

## Team

Many thanks to:
- EPFL: Prizes and global team organization
- The team: María Grandury and Angelika Romanou 


<center style="margin-top:40px;"><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participate now!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/en/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Back to challenges</a></center>
