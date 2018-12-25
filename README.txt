Arabidopsis thaliana transcriptomics
************************************

With these data, you can do your own fancy plant transcriptomics studies! Below are two ideas.

Hypothesis: Since Arabidopsis (thale cress) grows naturally in Scandanavia, drought is likely associated with frozen conditions. So, does cold stress trigger the same expressional response as drought stress? If so, is it a subset of differentially expressed (DE) genes in each condition, or is it the entire bundle of DE genes?

Hypothesis: Is there a point, developmentally, at which time expression for some set of genes stops changing (is adulthood a transcriptionally stable condition for plants)? Remember that some genes will change expression seasonally or according to stress, so this will be a "messy data" challenge.


Or test your own hypotheses.



################### FOLDER AND FILE FORMAT ######################
Special folders:
  - annotationFiles
      Use the file in here to convert Affymetrix 25k IDs (in the "Probe" column)
      to transcript IDs or get other fancy annotation information
      (what the gene does, which organism it comes from)
      (interestingly, some transcripts in these data come from bacteria or other organisms, which are technical controls on the array).
  - scripts
      Some example python scripts for you. You're welcome.

All other folders have
  a) a bunch of zip files,
  b) a bash script "getAll.sh" that I used to download the files, and
  c) a folder called "tmp" where I copied and unzipped one zip file for your reference.

Each zip file contains three files (which I name using their regular expressions) :
  1) .*\.cel
                        -- Raw data. Ignore this one. It's in some kind of binary format,
                           and since microarrays are becoming old fashioned,
                           you really don't need to know how to use their binary format.
  2) .*README\.txt
                        -- Simple README file, tells you about experimental condition,
                           control condition, and other useful stuff.
  3) .*[^"README"]\.txt
                        -- Normalized data. This is the one you'll want to use.
                           It's tab-delimited, it looks like the comment lines all occur before one blank line.
                           The header tells you what each of the columns are. Not all lines have content in all columns,
                           but all lines have enough tabs to match the header (so most lines have tons of invisible tabs at the end.)
                           In python, use " line.split('\t') " to break up the line by tabs into a list, indexed from 0.
                           I recommend storing a split (list) version of the header in a variable for reference as you script.

                           Note about data filtering:
                              You mostly care about the Signal column, because that's a quantitative measure of gene expression.
                              You'll also notice a column for Detection and one for Detection p-value.
                              It's a way that they estimate whether the signal is true or not.
                              When the p-value is low, Detection is "P" for present.
                              When the p-value is high, Detection is "A" for absent.
                              You can probably ignore the p-value and trust the Detection column.
                              One way to handle this while scripting is to save 0 expression ("Signal" column) for all Detection "A" genes.




Sources
--------------------------------------------------
All data downloaded from
https://www.arabidopsis.org/portals/expression/microarray/ATGenExpress.jsp#note

============== MICROARRAY  DATASETS ==============

Developmental: Expression Atlas of Arabidopsis Development
  https://www.arabidopsis.org/servlets/TairObject?type=hyb_descr_collection&id=1006710873

Experiment: Cold stress 
  https://www.arabidopsis.org/servlets/TairObject?type=hyb_descr_collection&id=1007966553

Experiment: Drought stress
  https://www.arabidopsis.org/servlets/TairObject?type=hyb_descr_collection&id=1007966668

Experiment: Heat stress
  https://www.arabidopsis.org/servlets/TairObject?type=hyb_descr_collection&id=1007967124

================ ANNOTATION FILE =================

ftp://ftp.arabidopsis.org/home/tair/Microarrays/Affymetrix/affy_ATH1_array_elements-2010-12-20.txt

