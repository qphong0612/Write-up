# vault-door-3
## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

> 200 points

## Hints
Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.


## Solution
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}
```

```python3

flag = 'jU5t_a_sna_3lpm18gb41_u_4_mfr340'
buffer = [''] * 32

for i in range(8):
    buffer[i] = flag[i]

for i in range(8, 16):
    buffer[i] = flag[23 - i]

for  i in range(16, 32, 2):
    buffer[i] = flag[46 - i]

for i in range(31, 16, -2):
    buffer[i] = flag[i]

print (''.join(buffer))
```

```node
Ξ ~ → node 
Welcome to Node.js v16.15.1.
Type ".help" for more information.
> var password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
undefined
> var i;
undefined
> var buffer = Array();
undefined
> for (i=0;i<8;i++) {
... buffer[i] = password.charAt(i);
... }
's'
> for (;i<16;i++) {
... buffer[i] = password.charAt(23 - i);
... }
'n'
> for (;i<32;i+=2) {
... buffer[i] = password.charAt(46 - i);
... }
'8'
> for (i=31;i>=17;i-=2) {
... buffer[i] = password.charAt(i);
... }
'g'
> console.log(buffer.join(""))
jU5t_a_s1mpl3_an4gr4m_4_u_1fb380
undefined
> 

```
