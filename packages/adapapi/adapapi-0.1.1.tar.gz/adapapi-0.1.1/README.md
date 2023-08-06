Module adapapi
==============

Classes
-------

`Appen(api_key)`
:   

    ### Methods

    `bonus_contributor(self, job_id, worker_id, amount_in_cents)`
    :   Max at one time is $20.00 or 2000 cents
        
        Args:
            job_id (int): ADAP Job ID
            worker_id (int): ADAP Contributor ID
            amount_in_cents (int): Amount in cents. The max amount to bonus per API request is $20.00. Function will split out your amount in max $20.00 chunks + remainder if more than $20.00 is to be bonused.

    `delete_unit(self, job_id, unit_id)`
    :   Units cannot be deleted from a running or paused job.
        
        Args:
            job_id (int): ADAP job ID
            unit_id (int): ADAP Unit ID

    `deprecate_job(self, job_id)`
    :   Deprecating an ADAP job.
        
        Args:
            job_id (int): ADAP job ID

    `download_jobid(self, job_id, reporttype, to_csv=False)`
    :   Recommended to regenerate report first. Downloads ADAP report to DataFrame object or CSV file.
        
        Args:
            job_id (int): ADAP Job ID
            reporttype (str): ADAP report type -- full, aggregated, json, gold_report, workset, source
            to_csv (bool): True if report should be saved to CSV, False if report to output as DataFrame object
        
        Returns:
            Pandas dataframe: Pandas dataframe of report

    `download_jobid_list(self, list_job_ids, reporttype, outfile_concat=False)`
    :   Download reports from a list of job IDs
        
        Args:
            list_job_ids (list): list of job IDs
            reporttype (str): ADAP report type -- full, aggregated, json, gold_report, workset, source
            outfile_concat (boolean): Option to concat all of the downloaded reports into one Pandas dataframe. Default is set to False.
        
        Returns:
            Pandas dataframe: Dependent on outfile_concat flag, will return concatenated dataframe of all listed job IDs

    `duplicate_job(self, job_id, include_uploaded_rows=False, include_tq=False)`
    :   Duplicate ADAP job
        
        Args:
            job_id (int): ADAP Job ID
            include_uploaded_rows (bool): Flag to include previously uploaded rows. Includes test questions if present. Default set to False. 
            include_tq (bool): Flag to include test questions only.
        
        Returns:
            int: New ADAP Job ID
    
    `get_all_jobs(self):
        """Retrieves list of all jobs. 
        More information https://developer.appen.com/#tag/Account-Info/paths/~1jobs.json/get

        Returns:
            list: List of all jobs.
        """

    `filter_jobs_by_tag(self, tag)`
    :   Retrieves list of job IDs with associated tag. 
        More information https://developer.appen.com/#tag/Account-Info/paths/~1jobs.json/get
        
        Args:
            tag (str): For multiple tags, delimit by comma. eg. 'tag1, tag2'
        
        Returns:
            list: List of job IDs with tag

    `filter_jobs_by_title(self, title):
        """Retrieves list of job IDs with associated title.
        More information https://developer.appen.com/#tag/Account-Info/paths/~1jobs.json/get
        
        Args:
            title (str): keywords to search for in job title
        
        Returns:
            list: List of jobs with title
        """

    `filter_jobs_by_copied_from(self, copied_from):
        """Retrieves list of job IDs with associated copied_from job_id.
        More information https://developer.appen.com/#tag/Account-Info/paths/~1jobs.json/get
        
        Args:
            copied_from (int): fileter jobs by the job id they were copied from
        
        Returns:
            list: List of jobs copied from  the copied_from_id

    `get_unit_state(self, job_id, unit_id)`
    :   Retrieves current unit state within job
        
        Args:
            job_id (int): ADAP Job ID
            unit_id (int): ADAP Unit ID
        
        Returns:
            dict: Dictionary containing _unit_id and _unit_state

    `get_unit_state_row(self, job_id, row)`
    :   Retrieves current unit state within job. To be used when row data needs to be returned.
        
        Args:
            job_id (int): ADAP Job ID
            row (Pandas Series or dictionary): Row from ADAP report 
        
        Returns:
            dict: Dictionary containing all data within row and _unit_state

    `internal_launch(self, job_id, units_to_launch)`
    :   Launching job internally
        
        Args:
            job_id (int): ADAP Job ID
            units_to_launch (int or str): Provide number of units to launch OR use "all" to launch all units.
        
        Returns:
            int: Number of units launched

    `job_json(self, job_id)`
    :   Get job json
        
        Args:
            job_id (int): ADAP Job ID
        
        Returns:
            dict: Job JSON

    `job_summary(self, job_id)`
    :   Getting job stats
        
        Args:
            job_id (int): ADAP Job ID
        
        Returns:
            dict: Returns golden_units, all_units, ordered_units, completed_units_estimate, needed_judgments, all_judgments, tainted_judgments, completed_gold_estimate, completed_non_gold_estimate

    `regenerate_jobid(self, job_id, reporttype)`
    :   Regenerates ADAP job
        
        Args:
            job_id (int_or_list): ADAP Job ID. If a list of job IDs provided, will regenerate them sequentially
            reporttype (str): ADAP report type -- full, aggregated, json, gold_report, workset, source

    `split_column(self, job_id, columnname, character)`
    :   Corresponds to the "Split Column" button in platform UI. This operation will split the contents of a column on a certain character, transforming strings into arrays of strings.
        
        Args:
            job_id (int): ADAP Job ID
            columnname (str): Column name
            character (str): Delimiting character

    `tag_add(self, job_id, tag)`
    :   Adding new tags. https://developer.appen.com/#tag/Manage-Job-Settings/paths/~1jobs~1{job_id}~1tags/post
        
        Args:
            job_id (int): ADAP Job ID
            tag (str): For multiple tags, delimit by comma. eg. 'tag1, tag2'

    `tag_get(self, job_id)`
    :   Tagging jobs. https://developer.appen.com/#tag/Manage-Job-Settings/paths/~1jobs~1{job_id}~1tags/post
        
        Args:
            job_id (int): ADAP Job ID
        
        Returns:
            list: List of tags attached to ADAP Job

    `tag_replace(self, job_id, tag)`
    :   Replacing existing tags with new tags. https://developer.appen.com/#tag/Manage-Job-Settings/paths/~1jobs~1{job_id}~1tags/post
        
        Args:
            job_id (int): ADAP Job ID
            tag (str): For multiple tags, delimit by comma. eg. 'tag1, tag2'

    `unit_json(self, job_id, unit_id)`
    :   Get unit json
        
        Args:
            job_id (int): ADAP Job ID
            unit_id (int): ADAP Unit ID
        
        Returns:
            dict: Unit JSON

    `update_job_json(self, job_id, indict)`
    :   Updating job settings
        
        Args:
            job_id (int): ADAP Job ID
            indict (dict): Dictionary of items to update within job json

    `update_unit_state(self, job_id, unit_id, state)`
    :   Updating unit state
        
        Args:
            job_id (int): ADAP job ID
            unit_id (int): ADAP Unit ID
            state (str): One of the following -- new, golden, finalized, canceled, deleted

    `upload(self, data_to_upload, job_id=None)`
    :   Uploads CSV (specify path), list of dictionaries, a single dictionary, or DataFrame. If no job ID is specified, a new job will be created.
        
        Args:
            data_to_upload (pd.DataFrame_or_str_or_list_or_dict): DataFrame object, path to CSV file, list of dictionaries, or single dictionary
            job_id (int): ADAP Job ID. If None then a new job will be created