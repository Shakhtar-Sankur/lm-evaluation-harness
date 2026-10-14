# MILU

### Paper

Title: `MILU: A Multi-task Indic Language Understanding Benchmark`

Abstract: https://arxiv.org/abs/2411.02538 (NAACL 2025)

MILU is a multiple-choice benchmark of questions from Indian regional and national exams, in 11
languages: Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil
and Telugu. It spans 8 domains and 42 subjects, including culturally specific ones such as local
history, arts, festivals and law.

Homepage: https://github.com/AI4Bharat/MILU

The dataset ([ai4bharat/MILU](https://huggingface.co/datasets/ai4bharat/MILU), CC BY 4.0) is
gated: accept its terms on Hugging Face and log in (`huggingface-cli login`, or set `HF_TOKEN`)
before running these tasks.

The prompt, choices and scoring follow the authors' evaluation code: the question and the four
options labelled A–D, then "Answer:", scored by the log-likelihood of each option's text, with
few-shot examples taken in order from the validation split. The paper reports 5-shot accuracy.

### Citation

```bibtex
@inproceedings{verma-etal-2025-milu,
  title     = {{MILU}: A Multi-task {I}ndic Language Understanding Benchmark},
  author    = {Verma, Sshubam and Khan, Mohammed Safi Ur Rahman and Kumar, Vishwajeet and Murthy, Rudra and Sen, Jaydeep},
  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies},
  year      = {2025}
}
```

### Groups, Tags, and Tasks

#### Groups

* `milu`: all 11 languages; accuracy averaged over questions (weighted by size).

#### Tasks

* `milu_bengali`, `milu_english`, `milu_gujarati`, `milu_hindi`, `milu_kannada`,
  `milu_malayalam`, `milu_marathi`, `milu_odia`, `milu_punjabi`, `milu_tamil`, `milu_telugu`

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog

* 1.0: initial version.
