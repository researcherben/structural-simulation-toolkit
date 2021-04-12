
docker build -t sst_10_with_stabilizer .

Status: 
Unable to build stabilizer due to clang++ dependency.
* no package available from apt-cache search
* unable to build LLVM from source
  * cmake version not sufficient
* https://github.com/silkeh/docker-clang/blob/master/11.Dockerfile
#15 1.631 LowerIntrinsics.cpp:6:10: fatal error: 'llvm/Module.h' file not found                                                                              
#15 1.631 #include "llvm/Module.h"

Take a look at 
https://github.com/silkeh/docker-clang

docker run -it --rm  sst_10_with_stabilizer /bin/bash
