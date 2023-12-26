<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="notebook/static/images/calmMind.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CalmMind</h3>

  <p align="center">
    A note taking app made using Django
  </p>
</div>


## About The Project
CalmMind is a note taking app that allows for users with their own independant data to be added and managed by admins.


### Built With

[![Django][Django.com]][Django-url]
[![Bootstrap][Bootstrap.com]][Bootstrap-url]



## Installation and Setup

1. Clone the repo
   ```sh
   git clone https://github.com/Sufyaan323/calmMind.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Perform migration to generate database tables
   ```sh
   python manage.py migrate
   ```
4. Start the server
   ```sh
   python manage.py runserver
   ```


## Notes

A superuser should be created using the following command:
```sh
python manage.py createsuperuser
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/