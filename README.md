<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



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



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jfrancoboeta/southflalerts">
    <img src="https://southflalerts.com/static/favicon.ico" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">South Florida Alerts</h3>

  <p align="center">
    A full-stack website app that will notify you when a seat becomes available for USF registration purposes
    <br />
    <a href="https://github.com/jfrancoboeta/southflalerts"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://southflalerts.com">View Demo</a>
    ·
    <a href="https://github.com/jfrancoboeta/southflalerts/issues">Report Bug</a>
    ·
    <a href="https://github.com/jfrancoboeta/southflalerts/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<a href = "https://southflalerts.com/">![Alt text](/README_screenshot.png?raw=true "Project Screenshot")</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
* <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
* <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" />
* <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
* <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need the following installations to have the web up and running using pip commands.
* Python 3.1 or later (https://www.python.org/downloads/)
* Django
  ```sh
  pip install Django
  ```
* BeautifulSoup
  ```sh
  pip install beautifulsoup4
  ```
* MySQL connector
  ```sh
  pip install mysql-connector-python
  ```
* ReCaptcha Django App
  ```sh
  pip install django-recaptcha
  ```

### Installation

1. Finish all the prerequisites
2. Clone the repo
   ```sh
   git clone https://github.com/jfrancoboeta/southflalerts.git
   ```
3. Run the <a href = "/alertsdb.sql">alertsdb.sql</a> file to install the database with MySQL in your host
4. Get a new Django secret key by running the following pip command, and add it in <a href = "/southflalerts/southflalerts/settings.py">southflalerts/southflalerts/settings.py</a> SECRET_KEY field
    ```sh
     python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
5. Update the Python script in <a href = "/alerts/Settings.py">alerts/Settings.py</a> with your info: SMTP and database credentials
6. Update Django settings.py in <a href = "/southflalerts/southflalerts/settings.py">southflalerts/southflalerts/settings.py</a> with your info: Allowed Hosts and trusted origins with your website URL; SMTP and database with your credentials; Your Google ReCaptcha public and private key; (Make sure you added your generated)
7. Run Django migration to migrate the Django database and other related data to your MySQL database
   ```sh
     python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
9. Run the Django app (make sure you are in the directory where manage.py is located):
     ```sh
     python manage.py makemigrations
     ```
     ```sh
     python manage.py migrate
     ```
10. Use a scheduler (like the Windows one) or something related to periodically run the script in <a href = "/alerts/Searcher.py">alerts/Searcher.py</a> - Note that making many requests to a website might get your host blocked from accessing it, so please give some time between running the script

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Please refer to this [Documentation](https://southflalerts.com/faq)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Subscribe only by selecting the term and class CRN (ID) instead of searching the URL
- [ ] Make more regular checks without excessive amount of website requests
- [ ] Implement waitlist seats to the web too
  - [ ] Give the option to choose whether the user is interested in receiving waitlist seats availability notification or not
- [ ] Add SMS notifications

See the [open issues](https://github.com/jfrancoboeta/southflalerts/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL v3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Juan Franco - j.francoboeta@gmail.com

Project Link: [https://github.com/jfrancoboeta/southflalerts](https://github.com/jfrancoboeta/southflalerts)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []() Base HTML template worked on - by W3 Docs (https://w3docs.com)
* []() Everyone who gave me feedback on the project and helped me make a user-friendly web app

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jfrancoboeta/southflalerts.svg?style=for-the-badge
[contributors-url]: https://github.com/jfrancoboeta/southflalerts/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jfrancoboeta/southflalerts.svg?style=for-the-badge
[forks-url]: https://github.com/jfrancoboeta/southflalerts/network/members
[stars-shield]: https://img.shields.io/github/stars/jfrancoboeta/southflalerts.svg?style=for-the-badge
[stars-url]: https://github.com/jfrancoboeta/southflalerts/stargazers
[issues-shield]: https://img.shields.io/github/issues/jfrancoboeta/southflalerts.svg?style=for-the-badge
[issues-url]: https://github.com/jfrancoboeta/southflalerts/issues
[license-shield]: https://img.shields.io/github/license/jfrancoboeta/southflalerts.svg?style=for-the-badge
[license-url]: https://github.com/jfrancoboeta/southflalerts/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jfrancoboeta
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
