# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a course materials repository for UPJV (Université Picardie Jules Verne) containing educational content for multiple subjects. The repository is organized by subject area, with each course containing presentations (PDFs) and infographics (PNGs).

## Repository Structure

### Python Course
```
python_course_upjv/
├── Introduction/              # Historical content (kept)
│   ├── presentations/
│   └── images/
├── presentations/             # Centralized: slides from NotebookLM
├── images/                    # Centralized: infographics from NotebookLM
├── TD06_Bases_Listes/
│   ├── notebook.ipynb        # Interactive Colab notebook
│   ├── README.md             # TD objectives and content
│   └── resources/            # Data files and supplementary materials
├── TD07_Fonctions_Packages_Numpy/
├── TD08_Matplotlib_Dictionnaires_Pandas/
├── TD09_Logique_Controle_Etude_Cas/
├── Travail_Maison_Enquete_Netflix/  # Home project (in binomial teams)
└── README.md
```

### Power BI Course
```
power_bi_course_upjv/
├── introduction/              # Historical content (kept)
│   ├── presentations/
│   └── images/
├── presentations/             # Centralized: slides from NotebookLM
├── images/                    # Centralized: infographics from NotebookLM
├── TD01_Premiers_pas_Power_BI/
│   ├── notebook.ipynb
│   ├── README.md
│   └── resources/
├── TD02_Visualiser_Filtrer/
├── TD03_DAX_Contexte/
├── TD04_DAX_Dates_Visualisation/
├── TD05_Visualisation_Emotionnelle/
├── Travail_Maison_Etude_Cas_Desabonnement/  # Home project (in binomial teams)
└── README.md
```

## Key Points

- **File Organization**: Each TD has a notebook, resources folder, and README. Slides and infographics are centralized in root `presentations/` and `images/` folders.
- **Notebook Storage**: Interactive notebooks are stored as `.ipynb` files and opened directly in Google Colab via direct links.
- **No Build Process**: This is a content repository, not a software project. There are no build, test, or lint commands.
- **Git Management**: Use standard git workflows to track changes. Include meaningful commit messages.
- **Learning Platform**: GitHub (storage) + Google Colab (notebooks) + Google Classroom (hub) + Google Forms (attendance/quizzes) + Google Sheets (results tracking).

## Workflow Overview

### For Students
1. Access course materials via Google Classroom (hub)
2. Open notebook links (direct Colab access via GitHub URL)
3. Complete attendance form (Google Form) at start of class
4. Complete quiz (Questionnaire in Classroom) at end of class
5. For home projects: work in binomial teams, submit by deadline

### For Instructors
1. **Add notebooks**: Place `.ipynb` files in each `TD##/` folder
2. **Add resources**: Upload datasets and files to `TD##/resources/`
3. **Generate slides**: Use NotebookLM to create PDFs from notebooks → save to `presentations/`
4. **Generate infographics**: Export infographics from NotebookLM → save to `images/`
5. **Setup Google Classroom**: Create class, add assignments with Colab links and quizzes
6. **Create attendance form**: Google Form with student name, ID, PC number, and daily code
7. **Track results**: Responses auto-sync to Google Sheets

## Common Tasks

### Adding Notebooks to a TD
1. Create or upload the `.ipynb` file to `TD##/notebook.ipynb`
2. Update the README.md with the correct Colab link: `https://colab.research.google.com/github/Maxencegu/[repo]/blob/main/TD##/notebook.ipynb`
3. Commit: `git add TD##/notebook.ipynb && git commit -m "Add notebook: TD## [title]"`

### Adding Presentations and Infographics
1. Generate PDFs and PNGs using NotebookLM from your notebooks
2. Save PDFs to `presentations/` with naming: `NN_descriptive_title.pdf`
3. Save PNGs to `images/` with naming: `infographie_NN.png`
4. Include references in the notebook to these files
5. Commit: `git add presentations/ images/ && git commit -m "Add NotebookLM content: [title]"`

### Adding Resources/Datasets to a TD
1. Place data files (CSV, Excel, etc.) in `TD##/resources/`
2. Reference them in the notebook with relative paths: `resources/filename.csv`
3. Commit: `git add TD##/resources/ && git commit -m "Add resources: TD## [files]"`

### Updating TD Documentation
- Edit the `TD##/README.md` file to update objectives, content, or instructions
- Keep descriptions concise and clear for students

## Learning Platform Setup

### Google Classroom
- **Python Course Class**: "Python TDs - UPJV"
- **Power BI Course Class**: "Power BI TDs - UPJV"
- Each class contains:
  - Assignments for each TD with Colab notebook links
  - Embedded questionnaires (quizzes) for in-class assessment
  - Announcement section for course updates
  - Grades section (automatically synced with questionnaires)

### Google Forms & Google Sheets
- **Attendance Form**: Daily presence tracking
  - Fields: Name, Student ID, PC Number, Daily Code
  - Responses → Google Sheet for analysis
  - Code ensures in-class only (given verbally at session start)

- **Questionnaire**: In-class quizzes via Google Classroom
  - Integrated into Classroom assignments
  - Auto-graded and synced to Grades

### Colab Direct Links
Format: `https://colab.research.google.com/github/Maxencegu/[repo]/blob/main/[path]/notebook.ipynb`

Example:
```
https://colab.research.google.com/github/Maxencegu/python_course_upjv/blob/main/TD06_Bases_Listes/notebook.ipynb
```

## Useful Git Commands

```powershell
# View course content changes
git log --oneline python_course_upjv/
git log --oneline power_bi_course_upjv/

# Check status of modified materials
git status

# View differences in course materials
git diff python_course_upjv/README.md

# Push changes to GitHub
git push origin main
```

## Notes for Future Development

- As additional TDs or courses are added, maintain consistent directory structure
- Keep NotebookLM-generated content (presentations/ and images/) in sync with notebooks
- Consider creating a template notebook for consistency across TDs
- Monitor and update Google Classroom as courses evolve
- Archive or update TDs based on student feedback and content improvements
