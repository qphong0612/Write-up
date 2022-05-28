# AN 

- NativeActivity is an activity that includes with the Android SDK.
- In this challenge it is used as main activity so there's no java code in dex.


```XML
<?xml version="1.0" encoding="utf-8"?>
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1"
    android:versionName="1.0"
    package="com.geekerchina.an"
    platformBuildVersionCode="23"
    platformBuildVersionName="6.0-2438415">

    <uses-sdk
        android:minSdkVersion="15"
        android:targetSdkVersion="23" />

    <application
        android:label="@ref/0x7f060012"
        android:icon="@ref/0x7f030000"
        android:hasCode="false">

        <activity
            android:label="@ref/0x7f060012"
            android:name="android.app.NativeActivity"
            android:configChanges="0xa0">

            <meta-data
                android:name="android.app.lib_name"
                android:value="an-a" />

            <intent-filter>

                <action
                    android:name="android.intent.action.MAIN" />

                <category
                    android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

    <meta-data android:name="android.app.lib_name" android:value="an-a" />
