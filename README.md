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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
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

* [Python 3.9](https://www.python.org/downloads/)
* [Blender 3.0](https://www.blender.org/download/releases/3-0/)


<!-- GETTING STARTED -->
## Getting Started

There are many ways on the internet on how to use python scripts and packages within blender.
I've found it most efficient to attach a Python script to a Blender subprocess.
This way, I can easily use an external IDE for writing the code and test it immediately running a custom script
that executes blender.

### Installation

1. Download the repository into your desired folder.
2. Run the included [install.py](install.py) script and follow it's instructions.
3. The script created two files for you `main.py` and `blender_script.py`.  
`main.py` is the script that will run blender with an attached custom script, the `blender_script.py` script, in a subprocess.
The `blender_script.py` is a test script to see if all the imports from the package and it's functionalities are working as expected.
You should see a cube that will be scaled on it's x axis when you run the animation from the keyframe editor.

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
Just post an issue with your feedback and I will respond to that as soon as possible.

If you have improvements/extensions for the code base, feel free to fork the repository and create a pull request :)
<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<!-- CONTACT -->
## Contact

I have no contact email or website at the moment.
