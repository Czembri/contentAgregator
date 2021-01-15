<br />
<p align="center">
  <a href="https://github.com/Czembri/contentAgregator">
    <img src="https://user-images.githubusercontent.com/57504533/104786284-c9f13c00-578c-11eb-86ce-eaeb16547a30.png" width="80" height="80">
  </a>

  <h3 align="center">Redactor Zone</h3>

  <p align="center">
    Great move to become a true journalist!
    <br />
    <a href="https://github.com/Czembri/contentAgregator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Main site](https://user-images.githubusercontent.com/57504533/104786507-64ea1600-578d-11eb-82cb-2c9bce2a68ea.png "Main")

Project has been created for journalists freelancers and casual users. It allows You to create Your own articles, share news, integrate on the blogs and more...

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)


<!-- GETTING STARTED -->
## Getting Started

Clone this repo to your local machine simply using https://github.com/Czembri/contentAgregator.git
You need to have installed python 3.8 > and postgres database. 

### Installation

1. Open terminal in the source directory
2. Create and activate a virtual environment
   * Windows:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   * Linux/MacOS
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   
3. Install requirements.txt
  * windows
   ```sh
   python -m pip install -r requirements.txt
   ```
  * Linux/MacOS
   ```sh
   python3 -m pip install -r requirements.txt
   ```
4. Create app_config.ini file and fill it with suitable data.
   ```ini
   [DATABASE]
    login = 
    password = 
    url = 
    db = 

    [MAIL]
    username =
    password =
    mail_default_sender = 
    mail_sender = 
    mail_receiver = 

    [SECRETS]
    secret_key = 
    jwt_secret_key = 

    [GOOGLE]
    google_client_id =
    google_client_secret =
   ```
5. Upgrade Your database using:
  ```sh
    flash db upgrade
  ```
6. Seed Your database using:
  ```sh
  flask seed run
  ```


<!-- USAGE EXAMPLES -->
## Usage

### Discover news made by users

![Discover](https://user-images.githubusercontent.com/57504533/104787446-d75bf580-578f-11eb-9188-57318a2812d8.png "discover")


### or check pupular news

![Popular](https://user-images.githubusercontent.com/57504533/104787549-0ffbcf00-5790-11eb-8e8e-bb9ad6a3a84e.png "popular")


### Enjoy Your dashboard

![Dashboard](https://user-images.githubusercontent.com/57504533/104787569-1e49eb00-5790-11eb-8513-b2a1e6f68994.png "dashboard")


### Integrate with users on the forum

![Forum](https://user-images.githubusercontent.com/57504533/104787641-57825b00-5790-11eb-8aea-28de24da6c4e.png "forum")

![Forum-comment](https://user-images.githubusercontent.com/57504533/104787669-7254cf80-5790-11eb-82ae-3e29eed4bccf.png "comment")

<!-- ROADMAP -->
## Roadmap

-- to do



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MY License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@CzembrowskaOla](https://twitter.com/CzembrowskaOla)

Project Link: [https://github.com/Czembri/contentAgregator](https://github.com/Czembri/contentAgregator)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
