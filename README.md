<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#importing-from-json-to-mysql">Generate Test Data for Your Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#clone-this-repository">Clone this repository</a></li>
        <li><a href="#configure-your-python-environment">Configure your Python environment</a></li>
        <li><a href="#running-the-script">Running the script</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!--<li><a href="#acknowledgments">Acknowledgments</a></li>-->
  </ol>
</details>

# Generate Test Data for Your project
For testing purposes, especially if you're building an app that uses any database technology to store information, you may need data to try out your project. In that case, you have two options:

* Find a good dataset ([Kaggle](https://kaggle.com/))
* Use a library like [Faker](https://github.com/joke2k/faker)

With Faker you can generate data through methods defined in the library. For example:
```python
from faker import Faker

fake = Faker()
for _ in range(10):
    print(fake.name())
```

Above code will print ten namess, and on each call to method `name()`, it will produce a random value. `name()` is a property of the generator, it's called a `fake`. and there are many of them packaged in `providers`. You can find more information on [bundled](https://faker.readthedocs.io/en/stable/providers.html) and [community](https://faker.readthedocs.io/en/stable/communityproviders.html) providers in the documentation.

```
Shannon Larson
Timothy Murray
Courtney Moore
Jody Jones
Sandra Miller
Anne Proctor
Brenda Rubio
Craig Turner
Nicole Barton
Nicholas Gentry
```

Some properties avaliable in the Faker library include:

* first_name()
* last_name()
* job()
* address()
* city()
* email()

Calling the `create_dataframe()` method of the `dataframe` module will create a Pandas DataFrame with data generated with Faker. This data will later be imported into the database. This DataFrame will contain the following columns, with values assigned by calling the methods listed above.

```
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   first_name  60000 non-null  object
 1   last_name   60000 non-null  object
 2   job         60000 non-null  object
 3   address     60000 non-null  object
 4   city        60000 non-null  object
 5   email       60000 non-null  object
```

On this repository, you can find two Python scripts:

* `sql.py`: Generate test data for MySQL and PostgreSQL.
* `mongodb.py`: Generate test data for MongoDB.

And you will find the following modules in the `modules` directory:

* `base.py`: Establish connection to the database, required for MySQL and PostgreSQL.
* `dataframe.py`: Contains the `create_dataframe()` method that will create a Pandas DataFrame with test data. It uses the `multiprocessing` module.
* `schema.py`: Contains the schema definition, required by Pandas `to_sql()` method.

The `mongodb.py` script uses the `dataframe` module for generating test data. Connection to the database and data importing are made directly from the script.

## Built With

<div align="center">
  <a href="https://github.com/mattdark/json-mysql-importer">
    <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Python Logo">
  </a>
</div>

* [pandas](https://pandas.pydata.org/)
* [SQLAlchemy](https://sqlalchemy.org/)
* [tqdm](https://github.com/tqdm/tqdm)
* [faker](https://github.com/joke2k/faker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequisites
### MySQL
Tests were run on Percona Server for MySQL. If you already have MySQL running on your system, skip this step.

For installing Percona Server for MySQL from the repositories on Debian and Ubuntu, follow the instructions below. For other operating systems check the [documentation](https://docs.percona.com/percona-server/latest/installation.html).

Before installing Percona Server for MySQL, make sure `curl` and `gnupg2` are installed.
```
$ sudo apt install gnupg2 curl
```

Then, install `percona-release`, a tool that allows users to automatically configure which Percona Software repositories are enabled or disabled.

Get the repository package:
```
$ wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
```

Install the downloaded package with dpkg:
```
$ sudo dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
```

Enable the ps80 repository:
```
$ sudo percona-release setup ps80
```

Install percona-server-server, the package that provides the Percona Server for MySQL:
```
$ sudo apt install percona-server-server
```

MySQL Shell is also recommended to be installed.

```
$ sudo apt install percona-mysql-shell
```

After installing, make sure MySQL is running.

During installation, `root` password is assigned. You can log into MySQL with this user or create a new one. Also, `movienet` database must be created.

Log into MySQL using MySQL Shell:

```
$ mysqlsh root@localhost
```

Replace `root` with your user if necessary, and replace `localhost` with the IP address or URL for your MySQL server instance if needed.

Change to SQL mode and create the `movienet` database:
```
\sql
create database company;
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### PostgreSQL
Tests were run on Percona Distribution for PostgreSQL. If you already have PostgreSQL running on your system, skip this step.

For installing Percona Distribution for PostgreSQL from the repositories on Debian and Ubuntu, follow the instructions below. For other operating systems check the [documentation](https://docs.percona.com/postgresql/14/).

Before installing Percona Distribution for PostgreSQL, make sure `curl` and `gnupg2` are installed.
```
$ sudo apt install gnupg2 curl
```

Then, install `percona-release`, a tool that allows users to automatically configure which Percona Software repositories are enabled or disabled.

Get the repository package:
```
$ wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
```

Install the downloaded package with dpkg:
```
$ sudo dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
```

Enable the `ppg14` repository:
```
$ sudo percona-release setup ppg-14
```

Install `percona-postgresql-14`, the package that provides the Percona Distribution for PostgreSQL:
```
$ sudo apt install percona-postgresql-14
```

After installing, make sure PostgreSQL is running.

You can connect to the PostgreSQL server with the `postgres` user or create a new one.
```
$ sudo su postgres
```

For Python you will need to create another user. Run:

```
$ createuser --interactive --pwprompt
```

It will ask you to enter new user details:

```
Enter name of role to add:
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n)
```

Choose `y` as this new user required superuser permissions.

Then open the PostgreSQL interactive terminal:
```
$ psql
```

And create the `company` database.
```
create database company;
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### MongoDB
Tests were run on Percona Server for MongoDB. If you already have MongoDB running on your system, skip this step.

For installing Percona Server for MongoDB from the repositories on Debian and Ubuntu, follow the instructions below. For other operating systems check the [documentation](https://docs.percona.com/percona-server-for-mongodb/5.0/install/index.html).

Before installing Percona Distribution for PostgreSQL, make sure `curl` and `gnupg2` are installed.
```
$ sudo apt install gnupg2 curl
```

Then, install `percona-release`, a tool that allows users to automatically configure which Percona Software repositories are enabled or disabled.

Get the repository package:
```
$ wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
```

Install the downloaded package with dpkg:
```
$ sudo dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
```

Enable the `psmdb-50` repository:
```
$ sudo percona-release enable psmdb-50 release
```

Install `percona-server-mongodb`, the package that provides the Percona Server for MongoDB:
```
$ sudo apt install percona-server-mongodb
```

After installing, make sure MongoDB is running.

Run the following script to enable authentication:

```
$ sudo /usr/bin/percona-server-mongodb-enable-auth.sh
```

This script creates the `dba` user with the `root` role. Don't forget to copy the password.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Conda
Before running the Python script that imports the data into a MySQL DB, you must install Conda through Anaconda or Miniconda. [Here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda) you can find more information on which one is better for you.

To install Anaconda, go to [anaconda.com/products/distribution](https://www.anaconda.com/products/distribution) and download the installer for your operating system.

If you're on Linux, run the following command after getting the installer:
```
$ bash Anaconda3-2022.05-Linux-x86_64.sh
```

Replacing the filename according to the version you're installing

It will prompt you to confirm some configuration details:
* Accepting license
* Confirming installation folder
* Initializing Anaconda (by the installer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
### Clone this repository
```
git clone https://github.com/mattdark/json-mysql-importer.git
```

### Configure your Python environment
#### virtualenv and pip

#### Install Python runtime and dependencies
When you clone this repository to your local development environment, you will find an environment.yml file that contains information about the Python version and dependencies required by this project. This file is used by Conda to configure the virtual environment and install dependencies.

After installing Anaconda, change to the `data-generator` directory:
```
$ cd data-generator
```

Create the environment:
```
$ conda env create -f environment.yml
```

This command will create a virtual environment for your project, install Python 3.10 and dependencies specified in the `environment.yml` file.

Once the environment is created, you can activate it by running:
```
$ conda activate percona
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Running the script
Before running the script, don't forget to set `user`, `password` and `host` in the `base` module, required for connecting to your MySQL or PostgreSQL database.

It creates 60 thousand records by default, but you can change this value by modifying the following line in the `dataframe` module:
```python
x = int(60000/num_cores)
```

#### MySQL
After setting up authentication details in the `base` module, run the Python script:

Uncomment this line in the `base` module:
```python
engine = create_engine("mysql+pymysql://user:password@localhost/company")
```

Uncomment this line in the `sql.py` script:
```python
conn.execute("ALTER TABLE employees ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
```

Comment this line in the `base` module:
```python
#engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/company")
```

Comment this line in the `sql.py` script:
```python
#conn.execute("ALTER TABLE employees ADD COLUMN id SERIAL PRIMARY KEY;")
```

Run the script

```
$ python sql.py
```

This script will do the following:
* Generate test data with the Faker library
* Create a Pandas DataFrame
* Import the DataFrame into MySQL
* Add the `id` column and set it as the primary key

A progress bar was added using tqdm.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### PostgreSQL
After setting up authentication details in the `base` module, run the Python script:

Uncomment this line in the `base` module:
```python
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/company")
```

Uncomment this line in the `sql.py` script:
```python
conn.execute("ALTER TABLE employees ADD COLUMN id SERIAL PRIMARY KEY;")
```

Comment this line in the `base` module:
```python
#engine = create_engine("mysql+pymysql://user:password@localhost/company")
```

Comment this line in the `sql.py` script:
```python
#conn.execute("ALTER TABLE employees ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
```

Run the script

```
$ python sql.py
```

This script will do the following:
* Generate test data with the Faker library
* Create a Pandas DataFrame
* Import the DataFrame into PostgreSQL
* Add the `id` column and set it as the primary key

A progress bar was added using tqdm.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### MongoDB
Before running the script, don't forget to set `user`, `password` and `host` in the `mongodb.py` script, required for connecting to your MongoDB database.

Modify this line to set up authentication details:
```python
uri = "mongodb://user:password@localhost:27017/company?authSource=admin"
```

It creates 60 thousand records by default, but you can change this value by modifying the following line in the `dataframe` module:
```python
x = int(60000/num_cores)
```

Run the script

```
$ python mongodb.py
```

This script will do the following:
* Generate test data with the Faker library
* Create a Pandas DataFrame
* Import the DataFrame into MongoDB
* Add the id column and set it as the primary key

A progress bar was added using tqdm.

<!-- ROADMAP -->
## Roadmap

- [x] Set up a Python Env with Anaconda
    - [x] Create Env Config File (environment.yml)
        - [x] Python Runtime
        - [x] Dependencies
- [x] Create requirements.txt
- [x] Test Data created with Faker
- [x] Create Pandas DataFrame
- [x] Import data to MySQL
- [x] Import Data to PostgreSQL
- [x] Import data to MongoDB
- [x] Implement multiprocessing
- [ ] Write a tutorial / blog post

<!-- See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Mario García - [@mariogmd](https://twitter.com/mariogmd) - hi@mariog.xyz

Project Link: [https://github.com/mattdark/data-generator](https://github.com/mattdark/data-generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS 
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mattdark/data-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/mattdark/data-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mattdark/data-generator.svg?style=for-the-badge
[forks-url]: https://github.com/mattdark/data-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/mattdark/data-generator.svg?style=for-the-badge
[stars-url]: https://github.com/mattdark/data-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/mattdark/data-generator.svg?style=for-the-badge
[issues-url]: https://github.com/mattdark/data-generator/issues
[license-shield]: https://img.shields.io/github/license/mattdark/data-generator.svg?style=for-the-badge
[license-url]: https://github.com/mattdark/data-generator/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mariogmd
