[![Build Status](https://travis-ci.com/FourmiPanda/py-choco.svg?branch=master)](https://travis-ci.com/FourmiPanda/py-choco)
# Py-Choco
Choco API for python

## Get started 
Set your JDK_HOME

```shell
 set JDK_HOME=YOUR_JDK_PATH
```

Add JVM to your PATH

```shell
 set PATH=YOUR_OLD_PATH;C:\...\YOUR_JDK_HOME\jre\bin\server
```

Add choco to your classpath

```shell
    set CLASSPATH=C:\PATH_TO_CHOCO\choco-4.10.0\choco-solver-4.10.0.jar
```

You need to install Cython and Pyjnius. 

```shell
      pip install Cython
```

```shell
      pip install Pyjnius
```

Pyjnius Documentation

https://pyjnius.readthedocs.io/en/stable/

To install Pyjnius you need to have JDK 8+ and Microsoft Visual C++

https://visualstudio.microsoft.com/downloads/


In Pychoco/demo there is a demo script: try.demo.py

Run it to verify your installation

You should have this:

```shell
** Choco 4.10.0 (2018-12) : Constraint Programming Solver, Copyright (c) 2010-2018
- Model[simple problem] features:
        Variables : 3
        Constraints : 2
        Building time : 0,279s
        User-defined search strategy : no
        Complementary search strategy : no
- Complete search - 1 solution found.
        Model[simple problem]
        Solutions: 1
        Building time : 0,279s
        Resolution time : 0,278s
        Nodes: 1 (3,6 n/s)
        Backtracks: 0
        Backjumps: 0
        Fails: 0
        Restarts: 0
X -> 2
Y -> 2
** Choco 4.10.0 (2018-12) : Constraint Programming Solver, Copyright (c) 2010-2018
- Model[simple problem 2] features:
        Variables : 3
        Constraints : 2
        Building time : 0,001s
        User-defined search strategy : no
        Complementary search strategy : no
- Complete search - No solution.
        Model[simple problem 2]
        Solutions: 0
        Building time : 0,001s
        Resolution time : 0,003s
        Nodes: 0 (0,0 n/s)
        Backtracks: 0
        Backjumps: 0
        Fails: 1
        Restarts: 0
X -> 0
Y -> 1

```
