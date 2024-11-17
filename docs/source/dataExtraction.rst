================
Data Extraction
================

This section details the data extraction process implemented in the TEXTRA-AI project focusing on Reinforcement Learning (RL) papers from arXiv.

Overview
---------

The data extraction pipeline is designed to systematically collect and process academic papers related to Reinforcement Learning.

Pipeline Components
--------------------

1. Paper Collection
~~~~~~~~~~~~~~~~~~~~

* **Source**: arXiv academic repository
* **Focus**: Papers tagged with or containing "reinforcement learning"
* **Implementation**: Using the ``arxiv`` Python package for API access
* **Search Criteria**: 

  * Primary search term: "reinforcement learning"
  * Sort order: By submission date (most recent first)
  * Customizable result limit

2. Data Processing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1 Initial Data Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Papers are downloaded as PDFs
* **Metadata** is extracted and stored, including:

  * Title
  * Authors
  * Publication date
  * arXiv ID
  * Categories
  * Abstract
  * PDF URL
  * Local storage path

2.2 File Organization
^^^^^^^^^^^^^^^^^^^^^^

The pipeline organizes data into the following structure::

    project_root/
    ├── data/
    │   ├── raw/
    │   │   ├── pdfs/           # Downloaded PDF files
    │   │   └── metadata/       # Paper metadata
    │   ├── processed/
    │   │   ├── text/          # Extracted text content
    │   │   └── vectors/       # Vectorized representations
    │   └── knowledge_base/    # Final processed data

3. Details
------------

3.1 Paper Search and Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def search_papers(max_results: int = 10):
        """Search for RL papers on ArXiv"""
        query = "reinforcement learning"
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        return list(search.results())

3.2 Metadata Extraction
^^^^^^^^^^^^^^^^^^^^^^^^

* Each paper's metadata is collected and stored in a structured format
* Metadata includes bibliographic information and local file references
* Data is saved in CSV format for easy access and manipulation

3.3 RL-Specific Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Papers are verified for RL content through:

  * Title analysis
  * Abstract scanning for RL-related terms
  * Category checking (cs.LG, cs.AI, etc.)



Notes
~~~~~~

The current implementation includes:

* Automated paper discovery and download
* Metadata extraction and storage
* Basic content validation
* Structured file organization

Next step
~~~~~~~~~~~

- OCR and layout analysis implementation


Usage
------

To use the data extraction pipeline:

1. Install required packages:

    .. code-block:: bash

        pip install arxiv pytesseract pdf2image pandas tqdm

2. Configure the desired paper count and search parameters in the script
3. Run the extraction pipeline
4. Monitor the organized output in the data directory structure

Some considerations
--------------------

* API rate limiting must be respected when accessing arXiv
* PDF processing can be computationally intensive
* Storage space requirements increase with the number of papers

Notebook
----------
.. raw:: html

   <iframe src="notebooks\ArXiv_rl_papers.html" width="100%" height="600px"></iframe>