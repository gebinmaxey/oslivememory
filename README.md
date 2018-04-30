# oslivememory


## What is it?

OS independent disk and memory usage visualizer


## Ubuntu

```sh
  sudo apt-get install python-dev python-tk python-pip
  python -m pip install matplotlib psutil
```

## Windows

1. Download and install python https://www.python.org/downloads/
2. [Add python to environment variables](https://www.java.com/en/download/help/path.xml)
3. python -m easy_install pip
4. python -m pip install matplotlib psutil

## OS X

1. Download and install python https://www.python.org/downloads/
2. [Add python to environment variables](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255)
3. python -m easy_install pip
4. python -m pip install matplotlib psutil


## Ubuntu extras:

To easily access on single command add the following to your ***.profile*** or ***.bashrc***

```sh
  gedit ~/.profile
```

Add the following and save. ***Make sure to replace {installtion} with the directory you cloned the repo to***

```sh
  get_disk(){
    cd {installation}
    python disk.py
  }
  
  get_disk(){
    cd {installation}
    python ram.py
  }
  
```
