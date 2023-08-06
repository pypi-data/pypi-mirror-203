from wonder_sdk.srgan.basicsr.archs.rrdbnet_arch import RRDBNet
from wonder_sdk.srgan.realesrgan import RealESRGANer

def configure_srgan(model_path, scale=2, half_precision=False):
    return RealESRGANer(
      scale=scale, model_path=model_path, 
      model=RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=scale),
      tile=0, tile_pad=10, pre_pad=0, half=half_precision
    )