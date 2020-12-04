package com.tcc.denguedetection.activities.sceneform;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;

import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.ar.core.Anchor;
import com.google.ar.sceneform.AnchorNode;
import com.google.ar.sceneform.ArSceneView;
import com.google.ar.sceneform.assets.RenderableSource;
import com.google.ar.sceneform.rendering.ModelRenderable;
import com.google.ar.sceneform.ux.ArFragment;
import com.google.ar.sceneform.ux.ScaleController;
import com.google.ar.sceneform.ux.TransformableNode;
import com.google.firebase.FirebaseApp;
import com.google.firebase.storage.FileDownloadTask;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.tcc.denguedetection.R;
import com.tcc.denguedetection.activities.crop.CropImage;
import com.tcc.denguedetection.activities.prediction.DenguePrediction;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.content.FileProvider;

import android.os.Environment;
import android.os.Handler;
import android.os.HandlerThread;
import android.util.Log;
import android.view.PixelCopy;
import android.view.View;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ImageCapture extends AppCompatActivity {

    private ArFragment fragment;
    private ModelRenderable cubeRenderable;
    private AnchorNode currentAnchorNode;
    private Anchor currentAnchor;
    private TransformableNode node;
    private ModelRenderable renderable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_capture);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = findViewById(R.id.fab);
        fragment = (ArFragment) getSupportFragmentManager().findFragmentById(R.id.sceneform_fragment);
        fragment.getArSceneView().getPlaneRenderer().setEnabled(false);
        loadBuilModel();


        fragment.setOnTapArPlaneListener(((hitResult, plane, motionEvent) -> {
            Anchor anchor = hitResult.createAnchor();
            AnchorNode anchorNode = new AnchorNode(anchor);
            anchorNode.setParent(fragment.getArSceneView().getScene());
            clearAnchor();
            currentAnchor = anchor;
            currentAnchorNode = anchorNode;

            node = new TransformableNode(fragment.getTransformationSystem());
            node.setRenderable(renderable);
            node.setParent(anchorNode);
            node.getScaleController().setEnabled(false);
            node.select(); // Interessante aplicar esse método para garantir que a renderização do cubo -> aplica um circulo em torno do cubo
        }));

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                takePhoto();
            }
        });

    }

    private void clearAnchor(){
        currentAnchor = null; // Sem efeito aparente
        if(currentAnchorNode != null){
            fragment.getArSceneView().getScene().removeChild(currentAnchorNode);
            currentAnchorNode.getAnchor().detach(); // Sem efeito aparentecurrentAnchorNode.setParent(null); // Sem efeito aparente
            currentAnchorNode.setParent(null);
            currentAnchorNode = null; // Sem efeito aparente

        }
    }

    private String generateFilename(Boolean crop) {
        if(crop == false){
            String date =
                    new SimpleDateFormat("yyyyMMddHHmmss", java.util.Locale.getDefault()).format(new Date());
            return Environment.getExternalStoragePublicDirectory(
                    Environment.DIRECTORY_PICTURES) + File.separator + "Sceneform/" + date + "_screenshot.jpg";
        }else{
            String date =
                    new SimpleDateFormat("yyyyMMddHHmmss", java.util.Locale.getDefault()).format(new Date());
            return Environment.getExternalStoragePublicDirectory(
                    Environment.DIRECTORY_PICTURES) + File.separator + "Sceneform/" + date + "_screenshotCrop.jpg";
        }

    }


    private void saveBitmapToDisk(Bitmap bitmap, String filename) throws IOException {
        File out = new File(filename);
        if (!out.getParentFile().exists()) {
            out.getParentFile().mkdirs();
        }
        try (
                FileOutputStream outputStream = new FileOutputStream(filename);
                ByteArrayOutputStream outputData = new ByteArrayOutputStream()
        ) {
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, outputData);
            outputData.writeTo(outputStream);
            outputStream.flush();
            outputStream.close();
        } catch (IOException ex) {
            throw new IOException("Failed to save bitmap to disk", ex);
        } catch (SecurityException ex){
            throw  new SecurityException("Security Failed: ", ex);
        }
    }

    private void takePhoto() {
        final String filename = generateFilename(false);
        final String cropFileName = generateFilename(true);
        ArSceneView view = fragment.getArSceneView();
        // Create a bitmap the size of the scene view.
        final Bitmap bitmap = Bitmap.createBitmap(view.getWidth(), view.getHeight(),
                Bitmap.Config.ARGB_8888);

        // Create a handler thread to offload the processing of the image.
        final HandlerThread handlerThread = new HandlerThread("PixelCopierSecond");
        handlerThread.start();
        // Make the request to copy.
        PixelCopy.request(view, bitmap, (copyResult) -> {
            if (copyResult == PixelCopy.SUCCESS) {
                try {
                    saveBitmapToDisk(bitmap, filename);
                } catch (IOException e) {
                    Toast toast = Toast.makeText(ImageCapture.this, e.toString(),
                            Toast.LENGTH_LONG);
                    toast.show();
                    return;
                }
            } else {
                Toast toast = Toast.makeText(ImageCapture.this,
                        "Failed to copyPixels: " + copyResult, Toast.LENGTH_LONG);
                toast.show();
            }

            if(handlerThread.quitSafely() == true){
                Intent intent = new Intent(ImageCapture.this, CropImage.class);
                intent.putExtra("fileName", filename);
                intent.putExtra("cropFileName", cropFileName);
                startActivity(intent);
            }
        }, new Handler(handlerThread.getLooper()));
    }

    public void loadBuilModel(){
        FirebaseApp.initializeApp(this);

        FirebaseStorage storage = FirebaseStorage.getInstance();
        StorageReference modelRef = storage.getReference().child("area.glb");

        try {
            File file = File.createTempFile("area", "glb");

            modelRef.getFile(file).addOnSuccessListener(new OnSuccessListener<FileDownloadTask.TaskSnapshot>() {
                @Override
                public void onSuccess(FileDownloadTask.TaskSnapshot taskSnapshot) {
                    buildModel(file);
                }
            });

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void buildModel(File file) {

        RenderableSource renderableSource = RenderableSource
                .builder()
                .setSource(this, Uri.parse(file.getPath()), RenderableSource.SourceType.GLB)
                .setRecenterMode(RenderableSource.RecenterMode.ROOT)
                .build();

        ModelRenderable
                .builder()
                .setSource(this, renderableSource)
                .setRegistryId(file.getPath())
                .build()
                .thenAccept(modelRenderable -> {
                    Toast.makeText(this, "Model built", Toast.LENGTH_SHORT).show();;
                    renderable = modelRenderable;
                });
    }
}