---
title: Modelos
description: Lista de modelos open-source en español. 
cover: "https://somosnlp.github.io/assets/images/undraw_education_edited.svg" 
---

<Table3
  :resourceItems="[
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
        name: 'BERTIN',
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
        name: 'Spanish GPT-2',
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
        name: 'GPT-2 Spanish (BERTIN Team)',
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
        name: 'GPT-2 Spanish (DeepESP)',
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
        name: 'GPT-2 Small Spanish',
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
        name: 'Spanish T5 Small',
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
        name: 'Spanish GPT-J-6B (BERTIN Team)',
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
        name: 'BLOOM (BigScience)',
        tags: ['multiidioma', 'LLM', 'propósito general'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'bloom'
    },
    {
        name: 'BLOOMZ (BigScience)',
        tags: ['multiidioma', 'LLM', 'propósito general', 'instrucciones', 'IT'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'bloomz'
    },
    {
        name: 'mT0 (BigScience)',
        tags: ['multiidioma', 'LLM', 'propósito general', 'instrucciones', 'IT', 'encoder-decoder'],
        description: '',
        website: '',
        github: '',
        paper: '',
        hf_dataset_name: '',
        hf_contributor_handle: 'bigscience',
        hf_model_name: 'mt0-base'
    }
    ]"
/>
