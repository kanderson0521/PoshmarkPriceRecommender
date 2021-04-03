# Poshmark Data Pull
Pulls data from the Poshmark website to build a price recommendation tool for Poshmark sellers. Poshmark uses json responses to load their HTML, using this request and response, you can get their data. For my project I wanted to grab only sold items and I focused on a subset of item category (clutches and wristlists) and a few differently priced brands.

The code in <b>posh_data_pull.py</b> pulls the data by creating a request for the parameters listed in the code and stores it into a text file. If you want equal sized datapoints for each brand, run each brand separately and save them each to a separate file. The brand name is specified in the values dictionary. To grab more or less than 5,000 posts, change the count in the values dictionary.


The code in <b>insert_posh_db.py</b> will create a Mongo database and collection to store each item post, change the file and brand name vars as neeeded. I also included <b>posh_Data_question.py</b> to validate the data after insertion and learn how to query data from a Mongo database.

The Jupyter notebook, <b>Poshmark_Price_Recommender.pynb</b>, contains data exploration and linear regression used to built the price recommender for sellers.
