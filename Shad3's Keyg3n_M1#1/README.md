
Decompiled check key Function: Note the comments. 

```c
undefined8 check_key(char *pcParm1)
{
    size_t sVar1;
    int local_20;
    int local_1c;

    local_1c = 0;
        // str length
    sVar1 = strlen(pcParm1);
        // str length larger than 7
    if (7 < sVar1) {
        sVar1 = strlen(pcParm1);
        // str length smaller than 11 0xb 
        if (sVar1 < 0xb) {
        local_20 = 0;
        while( true ) {
            sVar1 = strlen(pcParm1);
            if (sVar1 <= (ulong)(long)local_20) break;
                // ASCII sum of each charactor in char
            local_1c = local_1c + (int)pcParm1[(long)local_20];
            local_20 = local_20 + 1;
        }
        //ASCII sum of pcParm1 must be greater than 1000
        if (local_1c < 1000) {
            printf("Nope <3");
                        /* WARNING: SubroutQetuoine does not return */
            exit(0);
        }
        return 1;
        }
    }
    printf("Nope <3");
                        /* WARNING: Subroutine does not return */
    exit(0);
}
```

Therefore to construct our keygen the key has the following requirments. 
7 < length < 11
ASCII sum > 1000

Keygen script below:

```python
import random
import string

key = ""
ascii_sum = 0
for i in range(11):
    rnd_char = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase) - 1)]
    ascii_sum += ord(rnd_char)
    key += rnd_char
    if len(key) > 7 and len(key) < 11:
        if ascii_sum < 1000:
            pass
        else:
            print(key)
```

Test works!: 


parallels@parallels-Parallels-Virtual-Platform:/media/psf/Home/Desktop/Projects/re/Shad3's Keyg3n_M1#1$ ./keygen.bin
Give me a pass
vgigvbnchc
You made it, now keygen me!