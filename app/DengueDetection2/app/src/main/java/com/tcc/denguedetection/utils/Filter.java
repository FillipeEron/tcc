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

public class Filter {

    private  static  String TAG = "ImageProcessing";
    static {
        if (OpenCVLoader.initDebug()){
            Log.d(TAG, "Connected Successfully lol");
        }else{
            Log.d(TAG, "FAill!!!!!");
        }
    }

    private Bitmap renderedBitmap;
    private Bitmap originalBitmap;
    private Mat originalMat = new Mat();

    public Filter(Bitmap originalBitmap) {
        //this.originalBitmap = getResizedBitmap( originalBitmap.copy(Bitmap.Config.ARGB_8888, true), 32, 32 );
        this.originalBitmap = originalBitmap.copy(Bitmap.Config.ARGB_8888, true);
        this.renderedBitmap = this.originalBitmap;
        Utils.bitmapToMat(this.originalBitmap, this.originalMat);
    }

    public void applyMedianBlur(){
        //Bitmap temporaryBitmap = Bitmap.createBitmap(this.originalBitmap.getWidth(), this.originalBitmap.getHeight(), Bitmap.Config.ARGB_8888);
        Mat medianBlur = new Mat();
        Imgproc.medianBlur(this.originalMat, medianBlur, 5);

        Utils.matToBitmap(medianBlur, this.renderedBitmap);
    }

    public void applyClaheHistogram(){
        Mat tmpMat = new Mat();
        Mat mergedChannels = new Mat();
        Mat brgMat = new Mat();

        Imgproc.cvtColor(this.originalMat, tmpMat, Imgproc.COLOR_BGR2Lab);
        List<Mat> channels = new ArrayList<>();
        Core.split(tmpMat, channels);

        CLAHE clahe = new Imgproc().createCLAHE();
        clahe.setClipLimit(2.0);
        clahe.setTilesGridSize( new Size(8, 8) );

        Mat lightnessChannel = new Mat();
        clahe.apply(channels.get(0), lightnessChannel);

        Core.merge(new ArrayList<>(Arrays.asList(lightnessChannel, channels.get(1), channels.get(2))), mergedChannels);
        Imgproc.cvtColor(mergedChannels, brgMat, Imgproc.COLOR_Lab2BGR);

        Utils.matToBitmap(brgMat, renderedBitmap);

    }

    public Bitmap getOriginalBitmap(){
        return this.originalBitmap;
    }

    public Bitmap getRenderedBitmap(){
        return this.renderedBitmap;
    }


}
