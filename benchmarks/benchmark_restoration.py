import numpy as np
from skimage.data import camera
from skimage import restoration


class RestorationSuite:
    """Benchmark for restoration routines in scikit image."""
    def setup(self):
        nz = 32
        self.volume_f64 = np.stack([camera()[::2, ::2], ] * nz,
                                  axis=-1).astype(float) / 255

        self.sigma = .05
        self.volume_f64 += self.sigma * np.random.randn(*self.volume_f64.shape)
        self.volume_f32 = self.volume_f64.astype(np.float32)

    def peakmem_setup(self):
        pass

    def time_denoise_nl_means_f64(self):
        restoration.denoise_nl_means(self.volume_f64, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=False,
                                     multichannel=False)

    def time_denoise_nl_means_f32(self):
        restoration.denoise_nl_means(self.volume_f32, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=False,
                                     multichannel=False)

    def time_denoise_nl_means_fast_f64(self):
        restoration.denoise_nl_means(self.volume_f64, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=True,
                                     multichannel=False)

    def time_denoise_nl_means_fast_f32(self):
        restoration.denoise_nl_means(self.volume_f32, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=True)

    def peakmem_denoise_nl_means_f64(self):
        restoration.denoise_nl_means(self.volume_f64, patch_size=3,
                                     patch_distance=2,  sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=False,
                                     multichannel=False)

    def peakmem_denoise_nl_means_f32(self):
        restoration.denoise_nl_means(self.volume_f32, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=False)

    def peakmem_denoise_nl_means_fast_f64(self):
        restoration.denoise_nl_means(self.volume_f64, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=True,
                                     multichannel=False)

    def peakmem_denoise_nl_means_fast_f32(self):
        restoration.denoise_nl_means(self.volume_f32, patch_size=3,
                                     patch_distance=2, sigma=self.sigma,
                                     h=0.7 * self.sigma, fast_mode=True,
                                     multichannel=False)
