Datasets can be found here:

---------------
Cleaned Resume Dataset - csv -> https://drive.google.com/file/d/1UytVjID0HTIM-8sH3b1VKXYeBgz80J8M/view?usp=sharing

The dataset now has all (hopefully!) the important information cleaned and ready for modeling: skills, degrees, job titles, and processed text.
We’re saving it so we can use it later for TF-IDF and model training.

---------------
Cleaned Dataser Model Ready - csv -> https://drive.google.com/file/d/1msMq-bi3K2r07UHorhCfhYwFOCEzVkEI/view?usp=sharing
a smaller "model-ready" version of the dataset

This version keeps only the columns that will be useful later:
 - job_position_name = what role the resume belongs to (target label)
 - skills_combined = for reference or to build skill-based recommendations
 - model_text = the final cleaned and combined text we’ll feed into the model
We’re dropping the rest to make the file lighter and easier to work with.
