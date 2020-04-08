What makes scientific results reproducible?
===========================================

The idea of reproducible science is to provide not only the final results of
your research (often in the form of a paper), but also enable others to redo
your experiments and analysis. This allows for external verification, greater
trust in your results and comparative ease in reconstructing details of your
own work in the future.

So what is necessary for your computational results to be reproducible? The following is based on loosly [this article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285), which I would encourage you to read.

Automate everything
-------------------

Keep everything under version control
-------------------------------------

Archive your environment
------------------------

For Analyses That Include Randomness, Note Underlying Random Seeds
------------------------------------------------------------------

Record intermediate results
---------------------------

This is where it gets tricky. If you're intermediate files are just a couple of
MBs, than sure, check them into Git and be done with it (use Git LFS).

For large simulations, possible approaches could be
1. Put them into \<insert-favorite-cloud-storage-provider-here\>, and make it clear where to find this data.
2. Take a look at [Git-Annex](https://git-annex.branchable.com/), where you can combine git with storing data anywhere you want (other servers, your phone, Dropbox, Amazon S3, USB stick, Git LFS, Bittorrent, Google Drive, **IPFS**, ...).
3. Just give up. At a certain scale, in situ visualization is the only feasible thing anyway.

Provide Public Access to Scripts, Runs, and Results
---------------------------------------------------

