# My-CTF-Web-Challenges
## 国城杯-2024

### n0ob_un4er

**Difficulty**: ★★★★☆

**Solved**: 2 / 934

**Tag**: PHP, unserialize, phar ,session,pseudo-protocol

**description**: Please take me back to the golden age of PHP😭.

**hint**: 

- 不用管$SECRET，主要考虑copy()怎么利用
- 你可以创建一个session文件吗？
- 要怎么消除session文件中的垃圾字符呢？
- 执行/readflag读取flag

#### Source Code

- [index.php](https://github.com/litsasuk/My-CTF-Web-Challenges/blob/main/国城杯-2024/n0ob_un4er/html/index.php)

#### Solution

1. 将phar文件编码为字符串
2. 将编码后的phar字符串通过PHP_SESSION_UPLOAD_PROGRESS字段写入session文件中
3. 利用伪协议消除session文件前后的垃圾字符并将phar文件还原到/tmp/tmp.tmp文件中
4. 使用phar伪协议触发phar反序列化

#### Inspiration

出题思路主要是参考了orange师傅的两道题：One Line PHP Challenge以及Baby^h-master-php-2017，前者是orange师傅最喜欢的题目之一,后者是phar反序列化作为0day第一次出现在ctf题目当中。我将两道题的思路结合过后出了这么一道不需要上传phar文件的phar反序列化。

题目描述是：Please take me back to the golden age of PHP😭.虽然php最近爆出了很多很生猛的漏洞，但是我还是希望借这些"过时"的思路和trick，带大家回到那个独属于php的黄金年代。

#### Write Ups

- https://www.cnblogs.com/Litsasuk/articles/18593334
- https://blog.csdn.net/weixin_59166557/article/details/144435630
- https://www.cnblogs.com/dghh/p/18598149

### master-ast(线下awdp)

**Difficulty**: ★★★★☆

**Solved**: 0 / 10

**fixed**: 9 / 10

**Tag**: python,flask,sandbox bypass

**description**: None.

**hint**: None.

#### Source Code

- [app.py](https://github.com/litsasuk/My-CTF-Web-Challenges/blob/main/国城杯-2024/master_ast(awdp)/app.py)

#### Solution
- bypass BLACK_LIST = ['\'', '\"', '(', ')']
- bypass check_ast(no import、no call)
- bypass safe_globals

#### Inspiration

参考了一位大佬的推文https://x.com/emil_lerner/status/1369221697145016322
当时觉得这个思路很妙就拿来出题了。研究了一下怎么构造出"/"但是由于和题目环境不太兼容然后就没考。

#### Write Ups

- [先知](https://xz.aliyun.com/t/16869)

## LitCTF-2025

### 君の名は

**Difficulty**: ★★★☆☆

**Solved**: 16 / 613

**Tag**: PHP, unserialize, Anonymous Function, native class

**description**: None

**hint**: None

#### Source Code

- [index.php](https://github.com/litsasuk/My-CTF-Web-Challenges/blob/main/LitCTF2025/web-%E5%90%9B%E3%81%AE%E5%90%8D%E3%81%AF/html/index.php)

#### Solution

1. 构造pop链
2. 寻找可以调用方法的原生类
3. 找到匿名函数的名称规则
4. 绕过数据开头检测

#### Inspiration

Baby^h-master-php-2017其中的一个小点.
题目名为君の名は是因为这道题的主要思路就是寻找匿名函数的名字.

#### Write Ups

- [litsasuk的博客](https://www.cnblogs.com/Litsasuk/articles/18896993)
