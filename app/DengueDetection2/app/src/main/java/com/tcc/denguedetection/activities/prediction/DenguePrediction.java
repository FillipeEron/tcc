package com.tcc.denguedetection.activities.prediction;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.TextureView;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.tcc.denguedetection.R;
import com.tcc.denguedetection.activities.login.MainActivity;
import com.tcc.denguedetection.utils.Filter;
import com.tcc.denguedetection.utils.ImageProcessing;

import org.tensorflow.lite.Interpreter;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URI;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public class DenguePrediction extends AppCompatActivity {

    private Button backButton;
    private Button predictButton;
    private ImageView imageView;
    private TextView predictText;
    private Bitmap bitmapPrecessed;


    // New variables
    private Classifier classifier;

    // Github variaveis
    private Executor executor = Executors.newSingleThreadExecutor();

    private static final String MODEL_PATH = "model.tflite";
    private static final boolean QUANT = false;
    private static final String LABEL_PATH = "labels.txt";
    private static final int INPUT_SIZE = 32;
    // github variaveis


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dengue_prediction);

        backButton = findViewById(R.id.backButtonId);
        imageView = findViewById(R.id.imageViewId);
        predictText = findViewById(R.id.predictTextViewId);
        predictButton = findViewById(R.id.predictButtonId);

        Uri cropImageUri = (Uri)getIntent().getParcelableExtra("cropImageUri");

        Bitmap bitmap = BitmapFactory.decodeFile(cropImageUri.getPath());

        Filter filter = new Filter(bitmap);
        filter.applyMedianBlur();
        filter.applyClaheHistogram();

        imageView.setImageBitmap(filter.getRenderedBitmap());

        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(DenguePrediction.this, MainActivity.class));
            }
        });

        predictButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final List<Classifier.Recognition> results = classifier.recognizeImage(filter.getRenderedBitmap());
                Classifier.Recognition recognition = results.get(0);

                float threshold = 0.5f;

                if (recognition.getConfidence() > threshold){
                    predictText.setText( "Positivo: com " + String.format("%.2f", recognition.getConfidence() * 100.0f) + "% de confidência");
                }else{
                    predictText.setText( "Negativo: com " + String.format("%.2f", 100 - (recognition.getConfidence() * 100.0f) ) + "% de confidência");
                }
            }
        });
        initTensorFlowAndLoadModel();

    }

    private void initTensorFlowAndLoadModel() {
        executor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    classifier = TensorFlowImageClassifier.create(
                            getAssets(),
                            MODEL_PATH,
                            LABEL_PATH,
                            INPUT_SIZE,
                            QUANT);
                } catch (final Exception e) {
                    throw new RuntimeException("Error initializing TensorFlow!", e);
                }
            }
        });
    }

}