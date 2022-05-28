# EasyRe


```java
package easyre.sjl.gossip.easyre;

import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.http.util.EncodingUtils;

/* loaded from: classes-dex2jar.jar:easyre/sjl/gossip/easyre/EasyRe.class */
public class EasyRe extends ActionBarActivity implements View.OnClickListener {
    Button bt1;
    EditText et1;
    ImageView iv1;

    public void init() {
        try {
            InputStream openRawResource = getResources().openRawResource(R.raw.flag);
            byte[] bArr = new byte[openRawResource.available()];
            openRawResource.read(bArr);
            FileOutputStream openFileOutput = openFileOutput("flag.txt", 0);
            openFileOutput.write(bArr);
            openRawResource.close();
            openFileOutput.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override // android.view.View.OnClickListener
    public void onClick(View view) {
        String str = "";
        try {
            FileInputStream openFileInput = openFileInput("flag.txt");
            byte[] bArr = new byte[openFileInput.available()];
            openFileInput.read(bArr);
            str = EncodingUtils.getString(bArr, "UTF-8");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if (str.equals(this.et1.getText().toString())) {
            Toast.makeText(getApplicationContext(), "That's the flag!", 0).show();
        } else {
            Toast.makeText(getApplicationContext(), "0ops!That's wrong!", 0).show();
        }
    }

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // android.support.v7.app.ActionBarActivity, android.support.v4.app.FragmentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        System.loadLibrary("antidebug");
        init();
        super.onCreate(bundle);
        setContentView(R.layout.activity_easy_re);
        this.bt1 = (Button) findViewById(R.id.button);
        this.iv1 = (ImageView) findViewById(R.id.imageView);
        this.et1 = (EditText) findViewById(R.id.editText);
        this.bt1.setOnClickListener(this);
    }

    @Override // android.app.Activity
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_easy_re, menu);
        return true;
    }

    @Override // android.app.Activity
    public boolean onOptionsItemSelected(MenuItem menuItem) {
        return menuItem.getItemId() == 2131296322 ? true : super.onOptionsItemSelected(menuItem);
    }
}
```

Flag contain in res/raw/flag.txt
> 0ctf{Too_Simple_Sometimes_Naive!!!}
