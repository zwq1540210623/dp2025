int16量化 和 float对比
![](figture/Pasted%20image%2020250125083139.png)
int16量化 和 uint8量化对比
![](figture/Pasted%20image%2020250125083354.png)
通过初步对比，发现int16量化后，和flaot对比，基本在小数点2位对齐，所以结果是比较接近的；而uint8量化 和 int16量化对比，则很多在小数点1位都没有对齐。