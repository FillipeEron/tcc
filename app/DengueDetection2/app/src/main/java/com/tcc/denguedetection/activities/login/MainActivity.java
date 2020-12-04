package com.tcc.denguedetection.activities.login;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.google.ar.core.ArCoreApk;
import com.tcc.denguedetection.R;
import com.tcc.denguedetection.activities.sceneform.ImageCapture;

public class MainActivity extends AppCompatActivity {

    private Button buttonId;
    private TextView textViewId;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonId = findViewById(R.id.buttonId);
        textViewId = findViewById(R.id.textViewId);

        maybeEnableArButton();



        buttonId.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, ImageCapture.class));
            }
        });
    }

    void maybeEnableArButton() {
        ArCoreApk.Availability availability = ArCoreApk.getInstance().checkAvailability(this);
        if (availability.isTransient()) {
            // Re-query at 5Hz while compatibility is checked in the background.
            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    maybeEnableArButton();
                }
            }, 200);
        }
        if (availability.isSupported()) {
            buttonId.setEnabled(true);
            textViewId.setText("Dispositivo apto para executar a aplicação");
            // indicator on the button.
        } else { // Unsupported or unknown.
            textViewId.setText("Seu dispositivo não possui recursos mínimos para executar a aplicação");
            buttonId.setEnabled(false);
        }
    }

}
