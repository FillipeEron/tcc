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

public class DenguePrediction extends AppCompatActivity {

    private Button backButton;
    private Button predictButton;
    private ImageView imageView;
    private TextView predictText;
    private Bitmap bitmapPrecessed;

    private String  modelFile = "dengue_2.tflite";
    private static final int RESULTS_TO_SHOW = 3;
    private static final int IMAGE_MEAN = 128;
    private static final float IMAGE_STD = 128.0f;

    // int array to hold image data
    private int[] intValues;

    // Variavel responsavel por receber o modelo e opções de configurações
    private Interpreter tflite;
    // Variavel para guarda a imagem em formato de byte
    private ByteBuffer imgDataByte = null;
    // Opção para o carregamento do modelo
    private final Interpreter.Options tfliteOptions = new Interpreter.Options();
    // Lista de Labels
    private List<String> labelList = new ArrayList(Arrays.asList(new String[]{"Positibo", "Negativo"}));
    private int sizeLabel = labelList.size();
    // Array para guarda as probabilidades
    //private float[][] labelProbArray = new float[1][labelList.size()];
    private float[][] labelProbArray = new float[1][1];


    // input image dimensions for the Inception Model
    private int DIM_IMG_SIZE_X = 35;
    private int DIM_IMG_SIZE_Y = 35;
    private int DIM_PIXEL_SIZE = 3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dengue_prediction);

        backButton = findViewById(R.id.backButtonId);
        imageView = findViewById(R.id.imageViewId);
        predictText = findViewById(R.id.predictTextViewId);
        predictButton = findViewById(R.id.predictButtonId);


        // initialize array that holds image data
        intValues = new int[DIM_IMG_SIZE_X * DIM_IMG_SIZE_Y];

        // Preparação da classe "Interpreter" para carregar o modelo de predição
        try{
            tflite = new Interpreter(loadModelFile(), tfliteOptions);
            //labelList = loadLabelList();
            //labelList.add("Positivo");
            //labelList.add("Negativo");
        }catch (Exception e){
            e.printStackTrace();
        }

        imgDataByte = ByteBuffer.allocateDirect(4 * DIM_IMG_SIZE_X * DIM_IMG_SIZE_Y * DIM_PIXEL_SIZE);
        imgDataByte.order(ByteOrder.nativeOrder());

        Uri cropImageUri = (Uri)getIntent().getParcelableExtra("cropImageUri");

        Bitmap bitmap = BitmapFactory.decodeFile(cropImageUri.getPath());
        ImageProcessing imageProcessed  = new ImageProcessing(bitmap);
        bitmapPrecessed = imageProcessed.mainProcessing().getBitmapProcessed();
        imageView.setImageBitmap(bitmapPrecessed);


        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(DenguePrediction.this, MainActivity.class));
            }
        });

        predictButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                convertBitmapToByteBuffer(bitmapPrecessed);

                tflite.run(imgDataByte, labelProbArray);
                Float prob = 100 * labelProbArray[0][0];
                predictText.setText(prob.toString());
            }
        });
    }

    private MappedByteBuffer loadModelFile() throws IOException {
        AssetFileDescriptor fileDescriptor = this.getAssets().openFd(modelFile);
        FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor());
        FileChannel fileChannel = inputStream.getChannel();
        long startOffset = fileDescriptor.getStartOffset();
        long declaredLength = fileDescriptor.getDeclaredLength();
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength);
    }

    private void convertBitmapToByteBuffer(Bitmap bitmap) {
        if (imgDataByte == null) {
            return;
        }
        imgDataByte.rewind();
        bitmap.getPixels(intValues, 0, bitmap.getWidth(), 0, 0, bitmap.getWidth(), bitmap.getHeight());
        // loop through all pixels
        int pixel = 0;
        for (int i = 0; i < DIM_IMG_SIZE_X; ++i) {
            for (int j = 0; j < DIM_IMG_SIZE_Y; ++j) {
                final int val = intValues[pixel++];
                // get rgb values from intValues where each int holds the rgb values for a pixel.
                imgDataByte.putFloat((((val >> 16) & 0xFF)-IMAGE_MEAN)/IMAGE_STD);
                imgDataByte.putFloat((((val >> 8) & 0xFF)-IMAGE_MEAN)/IMAGE_STD);
                imgDataByte.putFloat((((val) & 0xFF)-IMAGE_MEAN)/IMAGE_STD);
            }

        }
    }


}