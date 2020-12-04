package com.tcc.denguedetection.activities.crop;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.FileProvider;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.widget.ImageView;
import android.widget.Toast;


import com.tcc.denguedetection.R;
import com.tcc.denguedetection.activities.login.MainActivity;
import com.tcc.denguedetection.activities.prediction.DenguePrediction;
import com.tcc.denguedetection.activities.sceneform.ImageCapture;
import com.yalantis.ucrop.UCrop;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
// https://github.com/Yalantis/uCrop
public class CropImage extends AppCompatActivity {

    private ImageView cropImageView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_crop);

        Bundle extra = getIntent().getExtras();
        String fileName = extra.getString("fileName");
        String cropFileName = extra.getString("cropFileName");

        File photoFile = new File(fileName);
        File cropFile = new File(cropFileName);

        Uri inputUri = Uri.fromFile(photoFile);
        Uri outPutUri = Uri.fromFile(cropFile);

        //Crop.of(inputUri, outPutUri).asSquare().start(CropImage.this);
        UCrop.of(inputUri, outPutUri)
                .withAspectRatio(0.5f, 0.5f)
                .withMaxResultSize(32, 32)
                .start(CropImage.this);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode == UCrop.REQUEST_CROP){
            handleCrop(resultCode, data);
        }
    }

    private void handleCrop(int resultCode, Intent result){
        if(resultCode == RESULT_OK){
            Uri cropImageUri = UCrop.getOutput(result);
            Intent intent = new Intent(CropImage.this, DenguePrediction.class);
            intent.putExtra("cropImageUri", cropImageUri);
            startActivity(intent);
        }else if( resultCode == UCrop.RESULT_ERROR){
            Toast.makeText(CropImage.this, UCrop.getError(result).getMessage(), Toast.LENGTH_SHORT).show();
        }
    }




}