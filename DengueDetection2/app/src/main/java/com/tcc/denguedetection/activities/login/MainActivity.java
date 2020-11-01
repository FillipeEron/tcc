package com.tcc.denguedetection.activities.login;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

import com.tcc.denguedetection.R;
import com.tcc.denguedetection.activities.sceneform.ImageCapture;

public class MainActivity extends AppCompatActivity {

    private Button buttonId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonId = findViewById(R.id.buttonId);

        buttonId.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, ImageCapture.class));
            }
        });

    }

}
