from layered import layered_image_mask

# layered_image_mask(
#     path_image="/media/mohsen/My Passport/dataset/IBSI/ibsi_1_ct_radiomics_phantom/nifti/image/phantom.nii.gz",
#     path_mask="/media/mohsen/My Passport/dataset/IBSI/ibsi_1_ct_radiomics_phantom/nifti/mask/mask.nii.gz",
# )


# layered_image_mask(
#     path_image="dataset/phantom.nii.gz",
#     path_mask="dataset/mask.nii.gz",
# )


layered_image_mask(
    path_image="dataset/small_bowel.nii",
    path_mask="dataset/1-1-label.nii",
)
