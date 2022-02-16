# Stanford ~ Programming in Journalism

Sundry notes and code bits for Stanford's Programming in Journalism class (COMM 177P/277P).

## Important links

* [Syllabus][]
* [Assignments](assignments/README.md) and [Grading](assignments/grading.md)
* [Bookshelf](docs/bookshelf.md) - recommended books, tutorials, cheatsheets, etc.
* [Code solutions](https://github.com/zstumgoren/stanford-progj-2022-solutions) - A private repo containing solutions to class exercises.
* [DataKit][] - overview and details on install and usage
* [Getting Help](docs/getting_help.md) - Resources and strategies for finding help.
* [Glossary](docs/glossary.md) - technical terms used in class
* [Python](docs/python/README.md) - overview, tutorials, etc.
* [Technical setup](docs/tech_setup.md) and [FAQ](docs/tech_faq.md) - recommended and required software (all free)
* [Workflow advice](docs/workflow_advice.md) - working on the command line, etc.

[Syllabus]: https://canvas.stanford.edu/courses/146027/assignments/syllabus

## Class notes

### Week 1

#### Day 1 - Course Intro

* Course overview - syllabus, [grading](assignments/grading.md), etc.
* Discuss the [history](docs/history.md) of code and data analysis in journalism
* Preview of [automation with Bash](exercises/bash_preview.md)
* [How to Succeed in this Course](docs/how_to_succeed.md)

#### Day 2 - The Owl, Problem Solving, and the Unix Workbench

* [The Owl, Problem Solving, and the Unix Workbench](docs/owl_probs_unix.md)
* [Bash intro](https://tinyurl.com/bash-intro)
* [Bash drill](exercises/bash_drill.md)
* **[Assignment 0](assignments/bash_intro.md)** - Unix practice and failed banks script


### Week 2

#### Day 3 - Unix Power Tools

* Misc
  * [Bashcrawl Mac bug](https://github.com/stanfordjournalism/stanford-progj-2022/issues/7)
  * [Prettify your shell prompt](docs/tech_faq.md#how-do-i-prettify-my-shell-prompt)
  * [Silence zsh warning](docs/tech_faq.md#how-do-i-silence-zsh-shell-warning)
  * [Bash drill](exercises/bash_drill.md)
  * Workflow advice: [Tinker, copy, run. Repeat.](docs/workflow_advice.md#tinker-copy-run-repeat)
* [Software installs](docs/tech_setup.md) -- everyone must have Python installed and GitHub configured by end of class.
* [Unix Power Tools for Data Wrangling](docs/power_tools_for_data_wrangling.md)
* [Bash drill](exercises/bash_drill.md) - Yep. Again. This time using the "Blind-folded" and "Plain English" [variations](exercises/bash_drill.md#variations-on-the-drill).
* **[Assignment 1](assignments/python_intro.md)** - Python reading/practice and code challenge

#### Day 4 - Python Intro

* Review [Assignment 0 (failed banks)](assignments/bash_intro.md) if everyone submitted...
* [Python Intro and resources](docs/python) links to misc docs/tutorials on this GitHub repo
* [Python overview and coding contexts](docs/python/overview.md)
* Questions about [Assignment 1](assignments/python_intro.md)? It covered a lot of important fundamentals:
  - Python interactive shell
  - Expressions
  - Basic data types
  - Variables
  - Flow control (conditions and blocks, if/else/elif etc.)
* [Python Syntax Crash Course](docs/python/python_syntax_crash_course.md)
* **[Assignment 2](assignments/python_lists_dicts.md)** - Python lists/dicts and DataKit overview


### Week 3

#### Day 5 - MLK Day

No class.


#### Day 6 - Python Intro Part Deux

* Questions about [Assignment 2](assignments/python_lists_dicts.md) on Python lists/dicts?
* Complete [configuration steps](docs/tech_setup.md#configure)
* **Pop Quiz: Lists/Dicts** (on [Tmux][] in the cloud for a little taste of [Pair Programming][])
* [Dictionaries crash course](docs/python/dict_basics.md)
* [Reading and writing text files](docs/python/file_io.md)
* Choose-your-own adventure pair coding challenge (election data or covid in prisons)
* **[Assignment 3](assignments/libraries_and_fdic_py.md)** - Practical Python skills and Failed Banks in Python

### Week 4

#### Day 7 - Automating Workflows and DataKit

* [Automating workflows](docs/automating_workflows.md)
* Overview of [DataKit][]
* Complete Tech Setup [configuration](docs/tech_setup.md#configure) and install [DataKit][]
* Continue work in-class on **[Assignment 3 - FDIC python script](assignments/libraries_and_fdic_py.md)** (**due by next class**)

[Tmux]: https://en.wikipedia.org/wiki/Tmux
[Pair programming]: https://en.wikipedia.org/wiki/Pair_programming

#### Day 8 - Practical Python Practice (Datakit Edition)

* [DataKit][] workflow review
* Wherefore, [virtual environments][] and [pipenv][]?
* Libraries - Overview and practice practical skills
  * Learn how to use [code libraries](/docs/python/libraries.md) included with Python or offered by third parties
  * Learn how to [download remote files](/docs/python/remote_files.md)
  * Learn how to [work with CSVs](/docs/python/csv.md)
* Continue pair programming on **[Assignment 3 - FDIC python script](assignments/libraries_and_fdic_py.md)** (**due by next class**)
* **[Assignment 4](assignments/python_functions_sorting_web_basics.md)** - Level up on Python functions, sorting and web basics (**due by next class**)

[virtual environments]: https://realpython.com/pipenv-guide/
[pipenv]: https://pipenv.pypa.io/en/latest/


### Week 5

#### Day 9

* [APIs and the News](/docs/apis_and_the_news.md) overview and [presentation](https://tinyurl.com/apis-and-the-news)
* [Working with APIs](/docs/python/working_with_apis.md) - we didn't
  have time to work through this one, but it's got some good background and exercises. Check it out!
* [Quakebot exercise](/exercises/quakebot.md) - hands-on practice with a JSON feed
* **[Assignment 5](assignments/senate_compromisers.md)** - Senate compromisers Python script

#### Day 10

* [Quakebot exercise](/exercises/quakebot.md) solutions?
* [The Art of Writing Functions](/docs/python/art_of_functions.md)
* **[Assignment 5](assignments/senate_compromisers.md)** - Senate compromisers Python script
* **[Assignment 6](/assignments/final_project_story_idea.md)** - Final project story idea pitches

### Week 6

#### Day 11 - Web scraping for the news

* [Web scraping for the news](/docs/web_scraping/README.md) - a high-level overview of web scraping in a news context.
* [Web scraping 101](/docs/web_scraping/101.md) - how to dissect a website, various obstacles to scraping and strategies for overcoming them
* [Web scraping exercises](/docs/web_scraping/exercises.md) - some websites to challenge your newfound scraping skills
* [Web scraping resources](/docs/web_scraping/resources.md) - tutorials, etc.

#### Day 12 - API Services and Data Pipelines with Modules

* [Data Pipelines with Modules](/docs/python/data_pipelines_with_modules.md)
* [API Services](/docs/api_services.md)
* [Refinitiv Entity Extraction](/code/refinitiv_example/README.md)
* **[Project (extra credit): FDA Recall Entities](/projects/fda_recall_entities.md)** - Scrape FDA recalls and extract entities using the OpenCalais/Refinitiv API
* **[Assignment 9](/assignments/first_notebook.md)** - First Python Notebook

### Week 7

#### Day 13 - Data Journalism Overview and Final Project Check-ins

* Discuss [data journalism readings](/assignments/dj_intro.md)
* [Whirlwind Tour of the Data Journalism Process](https://docs.google.com/presentation/d/1cEoPLJpZ6FVNLtW5f3jtWhgEeIhPv6eqWae85LAFPcs/edit?usp=sharing)
* **[Final Project](projects/sf_data_analysis.md)** - Present your [story idea](/assignments/final_project_story_idea.md) and begin data sleuthing & coding as teams.

#### Day 14 - Jupyter/pandas Overview and Coding Workshop

* [Data Analysis with Jupyter and pandas](/docs/python/data_analysis_intro.md) Overview
* Coding workshop: Work on [Final Project](projects/sf_data_analysis.md) or [FDA Recalls (extra credit)](/projects/fda_recall_entities.md)]



[DataKit]: docs/datakit.md
