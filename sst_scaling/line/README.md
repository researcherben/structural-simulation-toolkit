Docker limited to 2GB of RAM, 1GB of Swap

    sst --version
    SST-Core Version (10.0.0)

    seconds  kbytes
      1.076   80004  /usr/bin/time -v  sst --run-mode=init config_network.py 10000
      9.161  569928  /usr/bin/time -v  sst --run-mode=init config_network.py 100000
     10.511  569776  /usr/bin/time -v  sst --run-mode=init config_network.py 100000
     39.507 1853136  /usr/bin/time -v  sst --run-mode=init config_network.py 1000000 --> killed


    sst --version
    SST-Core Version (-dev, git branch : master, SHA: 3662fd2f0c930a7fde5139474014acf0ea258293)

    seconds  kbytes
      0.994   81724  /usr/bin/time -v  sst --run-mode=init config_network.py 10000
     10.117  587984  /usr/bin/time -v  sst --run-mode=init config_network.py 100000
      7.948    /usr/bin/time -v  sst --run-mode=init config_network.py 100000
      7.621    /usr/bin/time -v  sst --run-mode=init config_network.py 100000
     40.342  1839128  /usr/bin/time -v  sst --run-mode=init config_network.py 1000000 --> killed
     38.003  /usr/bin/time -v  sst --run-mode=init config_network.py 10000000 --> killed
