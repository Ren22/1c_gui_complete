class GlobalVars:
    def __init__(self):
        self.inp_path =  '/home/renat/EMBL/Sharaz_images/rhodamin'
        self.python_path =  '/home/renat/miniconda3/bin/python'
        self.stitchedImgPreMPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/pre/bf'
        self.stitchedImgPostMPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/post/bf'
        self.compositeImgPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/Composite.png'
        self.fijiPath = '/home/renat/EMBL/software/Fiji.app/ImageJ-linux64'
        self.cellprofilerPath = ''

    def set_inp_path(self, new_path):
        self.inp_path = new_path

    def set_python_path(self, new_path):
        self.python_path = new_path

    def set_pre_stitched_image_path(self, new_path):
        self.stitchedImgPreMPath = new_path

    def set_post_stitched_image_path(self, new_path):
        self.stitchedImgPostMPath = new_path

    def set_composite_path(self, new_path):
        self.compositeImgPath = new_path

    def set_fiji_path(self, new_path):
        self.fijiPath = new_path

    def set_cellprofiler_path(self, new_path):
        self.cellprofilerPath = new_path


global_vars = GlobalVars()