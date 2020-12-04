package com.tcc.denguedetection.utils;

import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.util.Log;

import org.opencv.android.OpenCVLoader;
import org.opencv.android.Utils;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.imgproc.CLAHE;
import org.opencv.imgproc.Imgproc;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ImageProcessing {

    private  static  String TAG = "ImageProcessing";
    static {
        if (OpenCVLoader.initDebug()){
            Log.d(TAG, "Connected Successfully lol");
        }else{
            Log.d(TAG, "FAill!!!!!");
        }
    }

    private Bitmap bitmapProcessed;
    private Bitmap sourceBitImage;
    private Mat sourceMatImage = new Mat();

    public ImageProcessing(Bitmap sourceImage) {
        this.sourceBitImage  = getResizedBitmap( sourceImage.copy(Bitmap.Config.ARGB_8888, true), 32, 32 );
        Utils.bitmapToMat(this.sourceBitImage, this.sourceMatImage);
    }

    public ImageProcessing mainProcessing(){
        Bitmap moldBitmap = Bitmap.createBitmap(this.sourceBitImage.getWidth(), this.sourceBitImage.getHeight(), Bitmap.Config.ARGB_8888);
        Mat medianBlur = new Mat();
        Mat claheHistogram = new Mat();
        Imgproc.medianBlur(this.sourceMatImage, medianBlur, 5);

        claheHistogram = this.matClaheHistogram();

        Utils.matToBitmap(claheHistogram, moldBitmap);
        bitmapProcessed = getResizedBitmap(moldBitmap, 35, 35);
        return this;
    }

    public Bitmap getBitmapProcessed(){
        return this.bitmapProcessed;
    }


    public Mat matClaheHistogram(){
        Mat tmpMat = new Mat();
        Mat mergedChannels = new Mat();
        Mat brgMat = new Mat();

        Imgproc.cvtColor(this.sourceMatImage, tmpMat, Imgproc.COLOR_BGR2Lab);
        List<Mat> channels = new ArrayList<>();
        Core.split(tmpMat, channels);

        CLAHE clahe = new Imgproc().createCLAHE();
        clahe.setClipLimit(2.0);
        clahe.setTilesGridSize( new Size(8, 8) );

        Mat lightnessChannel = new Mat();
        clahe.apply(channels.get(0), lightnessChannel);

        Core.merge(new ArrayList<>(Arrays.asList(lightnessChannel, channels.get(1), channels.get(2))), mergedChannels);
        Imgproc.cvtColor(mergedChannels, brgMat, Imgproc.COLOR_Lab2BGR);

        return brgMat;
    }

    public static Bitmap getResizedBitmap(Bitmap bm, int newWidth, int newHeight) {
        int width = bm.getWidth();
        int height = bm.getHeight();
        float scaleWidth = ((float) newWidth) / width;
        float scaleHeight = ((float) newHeight) / height;
        Matrix matrix = new Matrix();
        matrix.postScale(scaleWidth, scaleHeight);
        Bitmap resizedBitmap = Bitmap.createBitmap(
                bm, 0, 0, width, height, matrix, false);
        return resizedBitmap;
    }

}
