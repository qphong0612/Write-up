# LoopAndLoop

     secret code: 236492408
     
<p align="center">
     <img src="https://user-images.githubusercontent.com/83420725/170835028-3d0eebe4-5c5c-45d6-b84b-6e4d856caf2e.png" >
     <img src="https://user-images.githubusercontent.com/83420725/170835029-dd0bfd3b-ad04-42b5-8512-7707789d85e0.png">
</p>

```java
package net.bluelotus.tomorrow.easyandroid;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

/* loaded from: classes-dex2jar.jar:net/bluelotus/tomorrow/easyandroid/MainActivity.class */
public class MainActivity extends AppCompatActivity {
    static {
        System.loadLibrary("lhm");
    }

    public native int chec(int i, int i2);

    public int check(int i, int i2) {
        return chec(i, i2);
    }

    public int check1(int i, int i2) {
        for (int i3 = 1; i3 < 100; i3++) {
            i += i3;
        }
        return chec(i, i2);
    }

    public int check2(int i, int i2) {
        int chec;
        if (i2 % 2 == 0) {
            for (int i3 = 1; i3 < 1000; i3++) {
                i += i3;
            }
            chec = chec(i, i2);
        } else {
            for (int i4 = 1; i4 < 1000; i4++) {
                i -= i4;
            }
            chec = chec(i, i2);
        }
        return chec;
    }

    public int check3(int i, int i2) {
        for (int i3 = 1; i3 < 10000; i3++) {
            i += i3;
        }
        return chec(i, i2);
    }

    public String messageMe(String str) {
        return "LoopOk" + str;
    }

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // android.support.v7.app.AppCompatActivity, android.support.v4.app.FragmentActivity, android.support.v4.app.BaseFragmentActivityDonut, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        Button button = (Button) findViewById(R.id.button);
        final TextView textView = (TextView) findViewById(R.id.textView2);
        final TextView textView2 = (TextView) findViewById(R.id.textView3);
        final EditText editText = (EditText) findViewById(R.id.editText);
        button.setOnClickListener(new View.OnClickListener() { // from class: net.bluelotus.tomorrow.easyandroid.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                try {
                    int parseInt = Integer.parseInt(editText.getText().toString());
                    if (MainActivity.this.check(parseInt, 99) == 1835996258) {
                        textView.setText("The flag is:");
                        textView2.setText("alictf{" + MainActivity.this.stringFromJNI2(parseInt) + "}");
                        return;
                    }
                    textView.setText("Not Right!");
                } catch (NumberFormatException e) {
                    textView.setText("Not a Valid Integer number");
                }
            }
        });
    }

    @Override // android.app.Activity
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override // android.app.Activity
    public boolean onOptionsItemSelected(MenuItem menuItem) {
        return menuItem.getItemId() == 2131492961 ? true : super.onOptionsItemSelected(menuItem);
    }

    public native String stringFromJNI2(int i);
}
```
> Flag: alictf{Jan6N100p3r}
# Reference 
[write up](http://www.4k8k.xyz/article/Onlyone_1314/108260014)
