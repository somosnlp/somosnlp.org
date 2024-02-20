---
title: Modelos
description: Lista de modelos open-source en español. 
cover: https://somosnlp.github.io/assets/images/ilustraciones/undraw_education_edited.svg
tablePage: in
---

<TableModels
  :resourceItems="[
    {
        name: 'Bark',
        tags: ['multilingüe', 'texto a audio'],
        description: '',
        website: 'https://www.suno.ai',
        github: 'https://github.com/suno-ai/bark',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'suno',
        hf_model_name: 'bark'
    },
    {
        name: 'BETO',
        tags: ['BERT', 'base (case, uncased)', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: 'https://users.dcc.uchile.cl/~jperez/papers/pml4dc2020.pdf',
        hf_dataset_name: '',
        hf_contributor_handle: 'dccuchile',
        hf_model_name: 'bert-base-spanish-wwm-uncased'
    },
    {
        name: 'BETO (Spanish BERT) + Spanish SQuAD2.0 + distillation using 'bert-base-multilingual-cased' as teacher',
        tags: ['SQuAD-es-v2.0', 'BETO', 'Respuestas a preguntas'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
    },
    {
        name: 'BERTIN-GPT-J-6B',
        tags: ['GPT-J', 'LLM', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bertin-project',
        hf_model_name: 'bertin-gpt-j-6B'
    },
    {
        name: 'BERTIN RoBERTa',
        tags: ['RoBERTa', 'base', 'propósito general'],
        description: '',
        website: 'https://huggingface.co/spaces/bertin-project/bertin',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bertin-project',
        hf_model_name: 'bertin-roberta-base-spanish'
    },
    {
        name: 'BioMedtra',
        tags: ['Electra', 'small', 'textos bioclínicos'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'biomedtra-small-es'
    },
    {
        name: 'Biomedical-clinical language model for Spanish',
        tags: ['RoBERTa', 'textos bioclínicos'],
        description: '',
        website: '',
        github: 'https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'PlanTL-GOB-ES',
        hf_model_name: 'bsc-bio-ehr-es'
    },
    {
        name: 'BioMistral-7B',
        tags: ['multilingüe', 'LLM', 'textos bioclínicos'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'BioMistral',
        hf_model_name: 'BioMistral-7B'
    },
    {
        name: 'BLOOM',
        tags: ['multilingüe', 'LLM', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'bloom'
    },
    {
        name: 'BLOOMZ',
        tags: ['multilingüe', 'LLM', 'propósito general', 'instrucciones', 'IT'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'bloomz'
    },
    {
        name: 'Electricidad',
        tags: ['Electra', 'small, base', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'electricidad-base-discriminator'
    },
    {
        name: 'Fake news detection spanish',
        tags: ['RoBERTa', 'clasificación de texto'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'Narrativaai',
        hf_model_name: 'fake-news-detection-spanish'
    },
    {
        name: 'Falcon-40b',
        tags: ['multilingüe', 'LLM', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'tiiuae',
        hf_model_name: 'falcon-40b'
    },
    {
        name: 'GPT-2 BERTIN',
        tags: ['GPT-2', 'base', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'flax-community',
        hf_model_name: 'gpt-2-spanish'
    },
    {
        name: 'GPT-2 BNE',
        tags: ['GPT-2', 'base, large', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'PlanTL-GOB-ES',
        hf_model_name: 'gpt2-base-bne'
    },
    {
        name: 'GPT-2 Datificate',
        tags: ['GPT-2', 'small', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'datificate',
        hf_model_name: 'gpt2-small-spanish'
    },
    {
        name: 'GPT-2 DeepESP',
        tags: ['GPT-2', 'base', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'DeepESP',
        hf_model_name: 'gpt2-spanish'
    },
    {
        name: 'GPT-2 mrm8488',
        tags: ['GPT-2', 'base', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'spanish-gpt2'
    },
    {
        name: 'Gpt2 small spanish',
        tags: ['LLM', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'datificate',
        hf_model_name: 'gpt2-small-spanish'
    },
    {
        name: 'Legalectra',
        tags: ['Electra', 'small, base', 'legal'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'legalectra-base'
    },
    {
        name: 'LINCE-ZERO',
        tags: ['LLM', '7B, 40B', 'propósito general', 'instrucciones', 'IT'],
        description: '',
        website: 'https://huggingface.co/clibrain/lince-zero',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'clibrain',
        hf_model_name: 'lince-zero'
    },
    {
        name: 'mBART-50',
        tags: ['multilingüe', 'traducción'],
        description: '',
        website: '',
        github: '',
        paper: 'https://arxiv.org/abs/2008.00401',
        hf_dataset_name: '',
        hf_contributor_handle: 'facebook',
        hf_model_name: 'mbart-large-50'
    },
    {
        name: 'Mixtral-8x7B-v0.1',
        tags: ['multilingüe', 'LLM', 'propósito general'],
        description: '',
        website: 'https://mistral.ai/',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mistralai',
        hf_model_name: 'Mixtral-8x7B-v0.1'
    },
    {
        name: 'mT5 multilingual XLSum',
        tags: ['multilingüe', 'resumen', 'mT5'],
        description: '',
        website: '',
        github: 'https://github.com/csebuetnlp/xl-sum',
	    paper: 'https://aclanthology.org/2021.findings-acl.413/',
        hf_dataset_name: '',
        hf_contributor_handle: 'csebuetnlp',
        hf_model_name: 'mT5_multilingual_XLSum'
    },
    {
        name: 'mT0',
        tags: ['multilingüe', 'LLM', 'propósito general', 'instrucciones', 'IT', 'encoder-decoder'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'mt0-base'
    },
    {
        name: 'Projecte Aina’s Basque-Catalan machine translation model',
        tags: ['traducción'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'projecte-aina',
        hf_model_name: 'mt-aina-eu-ca'
    },
    {
        name: 'Projecte Aina’s Galician-Catalan machine translation model',
        tags: ['traducción'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'projecte-aina',
        hf_model_name: 'mt-aina-gl-ca'
    },
    {
        name: 'RoBERTa Biomedical Clinical',
        tags: ['RoBERTa', 'base', 'textos bioclínicos'],
        description: '',
        website: '',
        github: 'https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es',
        paper: 'https://arxiv.org/abs/2109.03570',
        hf_dataset_name: '',
        hf_contributor_handle: 'PlanTL-GOB-ES',
        hf_model_name: 'roberta-base-biomedical-clinical-es'
    },
    {
        name: 'RoBERTa BNE',
        tags: ['RoBERTa', 'base, large', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'PlanTL-GOB-ES',
        hf_model_name: 'roberta-base-bne'
    },
    {
        name: 'RoBERTalex',
        tags: ['RoBERTa', 'base', 'legal'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'PlanTL-GOB-ES',
        hf_model_name: 'RoBERTalex'
    },
    {
        name: 'RoBERTuito',
        tags: ['Roberta', 'cased, uncased, deaccented', 'redes sociales'],
        description: '',
        website: '',
        github: 'https://github.com/pysentimiento/robertuito',
        paper: 'https://arxiv.org/abs/2111.09453',
        hf_dataset_name: '',
        hf_contributor_handle: 'pysentimiento',
        hf_model_name: 'robertuito'
    },
    {
        name: 'robertuito sentiment analysis',
        tags: ['RoBERTa', 'clasificación de texto'],
        description: '',
        website: '',
        github: 'https://github.com/pysentimiento/pysentimiento',
	    paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'pysentimiento',
        hf_model_name: 'robertuito-sentiment-analysis'
    },
    {
        name: 'sentence similarity spanish es',
        tags: ['BERT', 'sentence-transformers', 'Similitud de oraciones'],
        description: '',
        website: '',
        github: '',
	      paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'hiiamsid',
        hf_model_name: 'sentence_similarity_spanish_es'
    },
    {
        name: 'Spanish BERT2BERT (BETO) fine-tuned on MLSUM ES for summarization',
        tags: ['BERT', 'resumen'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'mrm8488',
        hf_model_name: 'bert2bert_shared-spanish-finetuned-summarization'
    },
    {
        name: 'T5 Small',
        tags: ['T5', 'small', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'flax-community',
        hf_model_name: 'spanish-t5-small'
    },
    {
        name: 'Tulio Chilean Spanish BERT',
        tags: ['BETO', 'propósito general'],
        description: '',
        website: '',
        github: '',
	    paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'dccuchile',
        hf_model_name: 'tulio-chilean-spanish-bert'
    },
    {
        name: 'xlm roberta base language detection',
        tags: ['RoBERTa', 'multilingüe', 'clasificación de texto'],
        description: '',
        website: '',
        github: '',
	    paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'papluca',
        hf_model_name: 'xlm-roberta-base-language-detection'
    },
    ]"
/>