package com.tcc.denguedetection.utils;

import android.Manifest;
import android.util.Log;

import com.google.ar.sceneform.ux.ArFragment;

public class WritingArFragment extends ArFragment {
    @Override
    public String[] getAdditionalPermissions() {
        String[] additionalPermissions = super.getAdditionalPermissions();
        int permissionLength = additionalPermissions != null ? additionalPermissions.length : 0;
        String[] permissions = new String[permissionLength + 1];
        permissions[0] = Manifest.permission.WRITE_EXTERNAL_STORAGE;
        //Log.d("DEBUG", permissions[0]);
        if (permissionLength > 0) {
            System.arraycopy(additionalPermissions, 0, permissions, 1, additionalPermissions.length);
        }
        //Log.d("DEBUG", String.valueOf(permissions.length));
        return permissions;
    }

}


