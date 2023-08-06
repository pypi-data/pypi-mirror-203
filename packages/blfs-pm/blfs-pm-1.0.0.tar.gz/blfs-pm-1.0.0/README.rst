BLFS-automation:
================

A simple python script to ease your BLFS project in many ways…

About this project:
-------------------

This project is designed for people who have built their own
LinuxFromScratch (LFS) system, and are now working on the next stage -
BeyondLinuxFromScratch (BLFS). BLFS packages often require many other
dependencies to work, and sometimes it is a bit cumbersome to install
all of those.

Download and installation:
--------------------------

To get a local copy up and running follow these steps.

Prerequisites:
~~~~~~~~~~~~~~

.. raw:: html

   <ul>

.. raw:: html

   <li>

A working LFS system (check them out at
https://www.linuxfromscratch.org/)

.. raw:: html

   </li>

.. raw:: html

   <li>

A working internet connection - you may need to install a couple of BLFS
packages like NetworkManager, DHCPClient, and WPA-supplicant.

.. raw:: html

   </li>

.. raw:: html

   <li>

A working Python environment

.. raw:: html

   </li>

.. raw:: html

   <li>

Python3 package manager (Pip)

.. raw:: html

   </li>

.. raw:: html

   <li>

Git (https://www.linuxfromscratch.org/blfs/view/svn/general/git.html)

.. raw:: html

   </li>

.. raw:: html

   </ul>

Installation:
~~~~~~~~~~~~~

1. Clone this repository:

::

   git clone https://github.com/ahron-maslin/BLFS-automation.git 

2. Install the requirements:

::

   sudo pip install -r requirements.txt

Note: Installing the requirements, must be done as root - this fixes a
bug where the ``wget`` module does not get imported.

Usage:
------

It is recommended that the main script ``deps.py`` should always be run
as root, in order to prevent errors when installing packages to the
system.

This package has many options to list, download, list commands, or
install a given package. Note: once again it is *highly* recommended
that you always run this as ``root``!

Main usage:
``blfs-pm [-h] [-a] [-b PACKAGE] [-c PACKAGE] [-d PACKAGE] [-e PACKAGE] [-f] [-l PACKAGE] [-o] [-r] [-s PACKAGE]``

Note: It is recommended to follow along the installation process in the
BLFS book. This tool is not perfect and I have not tested every BLFS
package. There are still some issues with circular dependencies, and at
the moment it is best to moniter everything to prevent problems.
Additionally, the ``-b (build)`` option will prompt the user to run
EVERY command provided for the specific package. Some commands can only
be run if optional dependencies are installed (like Texlive, Docbook,
etc.). Furthermore, some packages require further kernel configuration
(and recompilation) as a prerequisite for installation.

::

     -h, --help                        show this help message and exit

     -a, --all                         Downloads ALL BLFS packages - uses a lot of time and space.

     -b PACKAGE, --build PACKAGE       Install a given Package on the system.

     -c PACKAGE, --commands PACKAGE    List installation (without installing) commands for a given package.
     
     -d PACKAGE, --download PACKAGE    Downloads a given BLFS package along with all of its dependencies.

     -e PACKAGE, --everything PACKAGE  Downloads and installs the given package with all of it's dependencies.

     -f, --force                       Force package installation even though it is already installed

     -l PACKAGE, --list PACKAGE        Lists all of the dependencies for a given BLFS package in order of installation.

     -o, --optional                    List/download optional packages.

     -r, --recommended                 List/download recommended packages.

     -s PACKAGE, --search PACKAGE      Search for a given package.

Additional options:
-------------------

Contributers:
-------------

Ahron Maslin (creator, maintainer, and designer), Josh W. (moral
support), Dan the Man (Chief Psychologist)

Todo
----

-  implement different db’s for different LFS versions
