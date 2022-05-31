# Timer

```java
package net.bluelotus.tomorrow.easyandroid;

import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

/* loaded from: classes-dex2jar.jar:net/bluelotus/tomorrow/easyandroid/MainActivity.class */
public class MainActivity extends AppCompatActivity {
    int now;
    int beg = ((int) (System.currentTimeMillis() / 1000)) + 200000;
    int k = 0;
    long t = 0;

    static {
        System.loadLibrary("lhm");
    }

    /* JADX WARN: Code restructure failed: missing block: B:22:0x003f, code lost:
        r6 = false;
     */
    /*
        Code decompiled incorrectly, please refer to instructions dump.
        To view partially-correct code enable 'Show inconsistent code' option in preferences
    */
    public static boolean is2(int r4) {
        /*
            r0 = 1
            r5 = r0
            r0 = r4
            r1 = 3
            if (r0 > r1) goto L15
            r0 = r4
            r1 = 1
            if (r0 <= r1) goto L10
            r0 = r5
            r6 = r0
        Le:
            r0 = r6
            return r0
        L10:
            r0 = 0
            r6 = r0
            goto Le
        L15:
            r0 = r4
            r1 = 2
            int r0 = r0 % r1
            if (r0 == 0) goto L21
            r0 = r4
            r1 = 3
            int r0 = r0 % r1
            if (r0 != 0) goto L26
        L21:
            r0 = 0
            r6 = r0
            goto Le
        L26:
            r0 = 5
            r7 = r0
        L28:
            r0 = r5
            r6 = r0
            r0 = r7
            r1 = r7
            int r0 = r0 * r1
            r1 = r4
            if (r0 > r1) goto Le
            r0 = r4
            r1 = r7
            int r0 = r0 % r1
            if (r0 == 0) goto L3f
            r0 = r4
            r1 = r7
            r2 = 2
            int r1 = r1 + r2
            int r0 = r0 % r1
            if (r0 != 0) goto L44
        L3f:
            r0 = 0
            r6 = r0
            goto Le
        L44:
            int r7 = r7 + 6
            goto L28
        */
        throw new UnsupportedOperationException("Method not decompiled: net.bluelotus.tomorrow.easyandroid.MainActivity.is2(int):boolean");
    }

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // android.support.v7.app.AppCompatActivity, android.support.v4.app.FragmentActivity, android.support.v4.app.BaseFragmentActivityDonut, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        final TextView textView = (TextView) findViewById(R.id.textView2);
        final TextView textView2 = (TextView) findViewById(R.id.textView3);
        final Handler handler = new Handler();
        handler.postDelayed(new Runnable() { // from class: net.bluelotus.tomorrow.easyandroid.MainActivity.1
            @Override // java.lang.Runnable
            public void run() {
                MainActivity.this.t = System.currentTimeMillis();
                MainActivity.this.now = (int) (MainActivity.this.t / 1000);
                MainActivity.this.t = 1500 - (MainActivity.this.t % 1000);
                textView2.setText("AliCTF");
                if (MainActivity.this.beg - MainActivity.this.now <= 0) {
                    textView.setText("The flag is:");
                    textView2.setText("alictf{" + MainActivity.this.stringFromJNI2(MainActivity.this.k) + "}");
                }
                if (MainActivity.is2(MainActivity.this.beg - MainActivity.this.now)) {
                    MainActivity.this.k += 100;
                } else {
                    MainActivity.this.k--;
                }
                textView.setText("Time Remaining(s):" + (MainActivity.this.beg - MainActivity.this.now));
                handler.postDelayed(this, MainActivity.this.t);
            }
        }, 0L);
    }

    @Override // android.app.Activity
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override // android.app.Activity
    public boolean onOptionsItemSelected(MenuItem menuItem) {
        return menuItem.getItemId() == 2131492959 ? true : super.onOptionsItemSelected(menuItem);
    }

    public native String stringFromJNI2(int i);
}
```
    iget v3, v3, Lnet/bluelotus/tomorrow/easyandroid/MainActivity;->k:I
    const v3, 1616384
And 
    
    if-eqz v0, :cond_1
    if-ltz v0, :cond_1

Decompile 
    
    apktool d Timer.apk
    
Build 
    
    apktool b -f -d aplication

Create key 
              
    keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

Then sign APK using

    jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore my_application.apk alias_name

Change value 

    iget v3, v3, Lnet/bluelotus/tomorrow/easyandroid/MainActivity;->k:I
    const v3, 1616384
And 
    
    if-gtz v0, :cond_0
    if-ltz v0, :cond_0






