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

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Blendanim (Animate Blender objects with Python)</h3>

  <p align="center">
    Blendanim is a package written in Python for easily animating objects in Blender.
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
I built this project after I had to automate the animation of some objects within Blender.
I've found it very tedious to work with the Blender Python API and all the long, hard to read bpy.something operations
started annoying me.  

With blendanim, the goal was to create an easy to use package, with a simple, intuitive syntax, that does all the
heavy lifting for animating in Blender for you (and for me).

### Built With

* Python 3.9
* [Blender 3.0](https://www.blender.org/download/releases/3-0/)


<!-- GETTING STARTED -->
## Getting Started

There are many ways on the internet on how to use python scripts and packages within blender.
I've found it most efficient to attach a Python script to a Blender subprocess.
This way, I can easily use an external IDE for writing the code and test it immediately running a custom script
that executes blender.

### Installation

1. Download the repository and move the [src](src) directory in to your desired folder.
2. At the top of your folder, create a `main.py` file from where we will start our blender subprocess with a custom script file.
Create a `blender_script.py` file as well.    
    
    Use the following code snippet for the `main.py` file and edit the subprocess_cmnds list according to your file system structure:  
    ```python
    import subprocess
    
    subprocess_cmnds = ['/path/to/blender/exe', '-d', '--python',
                        '/path/to/custom/script/blender_script.py', '--', '/path/to/project/folder/']
    subprocess.call(subprocess_cmnds)
    ```
    
    Use the following code snippet for the `blender_script.py` file:  
    ```python
    import sys
    # We need to append the working dir to the PYTHONPATH for blender to look inside our project's source folder
    working_dir = sys.argv[-2]
    sys.path.append(working_dir)
    
    from src import entities, animation
    
    def test_animation():
        cube = entities.Cube(width=2, height=2)
        animate = animation.Animate(cube)
    
        animate.scale("x", 2, start=0, end=1000)

    test_animation()
    ```
3. Now, execute the `main.py` file.
This should open Blender with our `blender_script.py` script and execute it.
If you start the animation via the keyframe editor, our cube will start to scale double in size for 1 second.

<!-- USAGE EXAMPLES -->
## Usage

This section shows some examples on how to use the package for writing a blender script.

#### Rotate object
This code creates and rotates a cube infinitely on it's x axis. 
```python
from src import entities, animation

cube = entities.Cube(width=2, height=2)
animate = animation.Animate(cube) 
animate.extrapolation = 'LINEAR'

animate.rotate('x', value=1, start=0, end=0)
animate.rotate('x', value=90, start=0, end=400)
```

### Scale object
This code creates and scales a cube by the value 2, on it's x axis for 1 second.

```python
from src import entities, animation

cube = entities.Cube(width=2, height=2)
animate = animation.Animate(cube)

animate.scale("x", 2, start=0, end=1000)
```

### Move object
This code creates and moves a cube, on the x axis, 5 blender units in the positive direction and then back to it's
original position. 

```python
from src import entities, animation

cube = entities.Cube(width=2, height=2)
animate = animation.Animate(cube)

animate.location("x", 5, start=0, end=500)
animate.location("x", 0, start=500, end=1000)
```
### Chaining different animations

This code shows how to chain different manipulations of the object to create cool, fluent animations that stack up.
```python
from src import entities, animation

cube = entities.Cube(width=2, height=2)
animate = animation.Animate(cube)

animate.location("x", 5, start=0, end=500)
animate.scale("xyz", 2, start=500, end=1000)
animate.location("z", 5, start=1000, end=1200)
animate.rotate("y", 180, start=1200, end=2000)
```

<!-- CONTRIBUTING -->
## Contributing

Since this is my first Open Source Project, any kind of feedback on documentation, usability, project structure etc. is highly appreciated!

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
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



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
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