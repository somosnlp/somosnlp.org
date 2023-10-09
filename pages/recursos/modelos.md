---
title: Modelos
description: Lista de modelos open-source en español. 
cover: https://somosnlp.github.io/assets/images/undraw_education_edited.svg
tablePage: in
---

<TableModels
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
    ]"
/>
