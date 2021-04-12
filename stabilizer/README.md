
docker build -t sst_10_with_stabilizer .

Status: 
Unable to build stabilizer due to clang++ dependency.
* no package available from apt-cache search
* unable to build LLVM from source
  * cmake version not sufficient


docker run -it --rm  sst_10_with_stabilizer /bin/bash
